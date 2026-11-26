import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Danh sách toàn bộ 12 thuộc tính đầu vào (đều là dạng số 100%, không còn text, không còn NaN, không còn -1)
ALL_NUMERIC_FEATURE_COLS = [
    'city',
    'city_development_index',
    'gender',
    'relevent_experience',
    'enrolled_university',
    'education_level',
    'major_discipline',
    'experience',
    'company_size',
    'company_type',
    'last_new_job',
    'training_hours'
]

# Ánh xạ các thuộc tính danh nghĩa và thứ bậc sang số nguyên không âm (>= 0)
GENDER_MAP = {'Female': 0, 'Male': 1, 'Other': 2}
RELEVENT_EXP_MAP = {'No relevent experience': 0, 'Has relevent experience': 1}
UNIV_MAP = {'no_enrollment': 0, 'Part time course': 1, 'Full time course': 2}
EDU_MAP = {'Primary School': 0, 'High School': 1, 'Graduate': 2, 'Masters': 3, 'Phd': 4}
MAJOR_MAP = {'STEM': 0, 'Business Degree': 1, 'Arts': 2, 'Humanities': 3, 'No Major': 4, 'Other': 5}
EXP_MAP = {'<1': 0, '>20': 21}
COMP_SIZE_MAP = {
    '<10': 0, '10/49': 1, '10-49': 1, '10 - 49': 1, 'Oct-49': 1, '50-99': 2, '100-500': 3,
    '500-999': 4, '1000-4999': 5, '5000-9999': 6, '10000+': 7
}
COMP_TYPE_MAP = {
    'Pvt Ltd': 0, 'Funded Startup': 1, 'Early Stage Startup': 2,
    'Public Sector': 3, 'NGO': 4, 'Other': 5
}
JOB_MAP = {'never': 0, '1': 1, '2': 2, '3': 3, '4': 4, '>4': 5}

def clean_and_convert_all_to_numeric(df_input: pd.DataFrame, is_train: bool = True, train_stats: dict = None):
    """
    Chuyển đổi 100% dữ liệu sang dạng số (int / float):
    - Xóa sạch 100% giá trị NaN (điền bằng Mode cho phân loại, Median cho số thực).
    - Xóa sạch 100% giá trị âm như -1 (chỉ dùng các số nguyên không âm: 0, 1, 2, ...).
    - Chuyển toàn bộ các chuỗi văn bản (text/categories) thành số nguyên.
    """
    df = df_input.copy()
    stats = {} if train_stats is None else train_stats.copy()

    # 1. city: trích xuất số nguyên từ mã 'city_103' -> 103
    df['city'] = df['city'].astype(str).str.replace('city_', '', regex=False).astype(int)

    # 2. gender: 'Female'->0, 'Male'->1, 'Other'->2
    if is_train:
        stats['gender_mode'] = df['gender'].mode()[0]
    df['gender'] = df['gender'].fillna(stats['gender_mode']).map(GENDER_MAP).astype(int)

    # 3. relevent_experience: 'No'->0, 'Has'->1
    df['relevent_experience'] = (df['relevent_experience'] == 'Has relevent experience').astype(int)

    # 4. enrolled_university: 'no_enrollment'->0, 'Part time'->1, 'Full time'->2
    if is_train:
        stats['univ_mode'] = df['enrolled_university'].mode()[0]
    df['enrolled_university'] = df['enrolled_university'].fillna(stats['univ_mode']).map(UNIV_MAP).astype(int)

    # 5. education_level: 0 -> 4
    if is_train:
        stats['edu_mode'] = df['education_level'].mode()[0]
    df['education_level'] = df['education_level'].fillna(stats['edu_mode']).map(EDU_MAP).astype(int)

    # 6. major_discipline: 0 -> 5
    if is_train:
        stats['major_mode'] = df['major_discipline'].mode()[0]
    df['major_discipline'] = df['major_discipline'].fillna(stats['major_mode']).map(MAJOR_MAP).astype(int)

    # 7. experience: '<1'->0, '1'..'20'->1..20, '>20'->21
    def parse_exp(val):
        if pd.isna(val):
            return np.nan
        if str(val) in EXP_MAP:
            return EXP_MAP[str(val)]
        try:
            return float(val)
        except Exception:
            return np.nan

    df['experience'] = df['experience'].apply(parse_exp)
    if is_train:
        stats['exp_median'] = int(df['experience'].median())
    df['experience'] = df['experience'].fillna(stats['exp_median']).astype(int)

    # 8. company_size: 0 -> 7
    if is_train:
        stats['comp_size_mode'] = df['company_size'].mode()[0]
    df['company_size'] = df['company_size'].fillna(stats['comp_size_mode']).map(COMP_SIZE_MAP).astype(int)

    # 9. company_type: 0 -> 5
    if is_train:
        stats['comp_type_mode'] = df['company_type'].mode()[0]
    df['company_type'] = df['company_type'].fillna(stats['comp_type_mode']).map(COMP_TYPE_MAP).astype(int)

    # 10. last_new_job: 0 -> 5
    if is_train:
        stats['job_mode'] = df['last_new_job'].mode()[0]
    df['last_new_job'] = df['last_new_job'].fillna(stats['job_mode']).map(JOB_MAP).astype(int)

    # 11. training_hours: int
    df['training_hours'] = df['training_hours'].astype(int)

    # 12. city_development_index: float
    df['city_development_index'] = df['city_development_index'].astype(float)

    # Biến mục tiêu target (nếu có)
    if 'target' in df.columns:
        df['target'] = df['target'].astype(int)

    return df, stats

def get_train_data(train_csv_path: str):
    """
    Đọc dữ liệu train và trả về dạng số 100% (không có NaN, không có -1)
    """
    df_raw = pd.read_csv(train_csv_path)
    df_clean, stats = clean_and_convert_all_to_numeric(df_raw, is_train=True)
    
    X = df_clean[ALL_NUMERIC_FEATURE_COLS]
    y = df_clean['target']
    
    return X, y, df_clean, stats

def get_test_data(test_csv_path: str, train_stats: dict):
    """
    Đọc dữ liệu test và trả về dạng số 100% sử dụng thống kê Mode/Median từ tập train
    """
    df_raw = pd.read_csv(test_csv_path)
    df_clean, _ = clean_and_convert_all_to_numeric(df_raw, is_train=False, train_stats=train_stats)
    
    X_test = df_clean[ALL_NUMERIC_FEATURE_COLS]
    test_ids = df_raw['enrollee_id']
    
    return X_test, test_ids
