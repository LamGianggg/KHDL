# HR ANALYTICS: JOB CHANGE OF DATA SCIENTISTS
## Dự Án Machine Learning Hoàn Chỉnh (CSE3040 - Khoa học Dữ liệu)

Thư mục này chứa toàn bộ mã nguồn, mô hình, sổ tay phân tích và kết quả dự đoán hoàn chỉnh cho bài toán **Dự đoán ứng viên Data Scientist nhảy việc**.

---

### 📂 Cấu Trúc Thư Mục

```text
HR Analytics/
├── aug_train.csv                             # Dữ liệu huấn luyện gốc (19.158 dòng)
├── aug_test.csv                              # Dữ liệu kiểm thử gốc (2.129 dòng)
├── sample_submission.csv                     # File mẫu nộp bài Kaggle gốc
├── hr-analytics-...metadata.json             # Metadata gốc của dataset
│
├── train_cleaned_numeric.csv                 # Dữ liệu train đã làm sạch & số hóa 100% (0 NaN, 0 số âm)
├── test_cleaned_numeric.csv                  # Dữ liệu test đã làm sạch & số hóa 100% (0 NaN, 0 số âm)
│
├── Bao_Cao_Do_An_HR_Analytics.docx           # BÁO CÁO ĐỒ ÁN WORD (.DOCX) CHUẨN ĐẠI HỌC (CÓ SẴN HÌNH & BẢNG)
├── BAO_CAO_DO_AN_HR_ANALYTICS.md             # Báo cáo đồ án chi tiết định dạng Markdown
├── generate_docx_report.py                   # Script tự động tạo lại file Word báo cáo
│
├── Kich_Ban_Thuyet_Trinh_HR_Analytics.docx   # KỊCH BẢN THUYẾT TRÌNH WORD (.DOCX) 4 PHẦN CHUẨN ĐẠI HỌC
├── KICH_BAN_THUYET_TRINH_HR_ANALYTICS.md     # Kịch bản thuyết trình & bảo vệ chi tiết (Markdown)
├── generate_hr_script_docx.py                # Script tự động biên dịch kịch bản sang Word
│
├── 01_model_logistic_regression.py           # Mô hình 1: Logistic Regression độc lập
├── 02_model_random_forest.py                 # Mô hình 2: Random Forest độc lập
├── 03_model_lightgbm.py                      # Mô hình 3: LightGBM độc lập
├── 04_compare_models.py                      # Script so sánh đối đầu cả 3 mô hình & vẽ ROC
│
├── src/
│   ├── __init__.py
│   └── data_preprocessing.py                 # Module tiền xử lý, điền khuyết & mã hóa đặc trưng
│
├── notebooks/
│   └── HR_Analytics_Exploration_and_Modeling.ipynb # Sổ tay Jupyter trực quan toàn diện (EDA + Models)
│
├── models/                                   # Nơi lưu các mô hình đã huấn luyện (.pkl)
│   ├── model_logistic_regression.pkl
│   ├── model_random_forest.pkl
│   └── model_lightgbm.pkl
│
├── submissions/                              # Nơi lưu file dự đoán cho tập test (2.129 dòng)
│   ├── submission_logistic_regression.csv
│   ├── submission_random_forest.csv
│   └── submission_lightgbm.csv
│
├── figures/                                  # Nơi lưu biểu đồ ROC, Confusion Matrix, Feature Importance
│   ├── confusion_matrix_logistic_regression.png
│   ├── confusion_matrix_random_forest.png
│   ├── confusion_matrix_lightgbm.png
│   ├── feature_importance_random_forest.png
│   ├── feature_importance_lightgbm.png
│   └── roc_curves_comparison.png
│
├── requirements.txt                          # Danh sách thư viện Python cần thiết
└── README.md                                 # Hướng dẫn chi tiết dự án
```

---

### 🚀 Cách Chạy Từng Mô Hình Độc Lập

Mỗi file mô hình được thiết kế độc lập, chỉ cần chạy trực tiếp từ dòng lệnh:

#### 1. Huấn luyện Mô hình 1 (Logistic Regression)
```powershell
python "01_model_logistic_regression.py"
```
* **Mô tả:** Mô hình tuyến tính Baseline có điều chỉnh trọng số mẫu (`class_weight='balanced'`).
* **Đầu ra:** 
  * Điểm 5-Fold CV ROC-AUC: ~0.792
  * Mô hình lưu tại `models/model_logistic_regression.pkl`
  * Dự đoán lưu tại `submissions/submission_logistic_regression.csv`
  * Biểu đồ Confusion Matrix tại `figures/confusion_matrix_logistic_regression.png`

#### 2. Huấn luyện Mô hình 2 (Random Forest Classifier)
```powershell
python "02_model_random_forest.py"
```
* **Mô tả:** Mô hình Ensemble Bagging (150 cây quyết định, giới hạn độ sâu để chống overfitting).
* **Đầu ra:**
  * Điểm 5-Fold CV ROC-AUC: ~0.796
  * Mô hình lưu tại `models/model_random_forest.pkl`
  * Dự đoán lưu tại `submissions/submission_random_forest.csv`
  * Biểu đồ Confusion Matrix và Feature Importance tại `figures/`

#### 3. Huấn luyện Mô hình 3 (LightGBM Classifier - Tối ưu nhất)
```powershell
python "03_model_lightgbm.py"
```
* **Mô tả:** Mô hình Gradient Boosting tốc độ cao, hỗ trợ tối ưu trên dữ liệu dạng bảng và mất cân bằng lớp.
* **Đầu ra:**
  * Điểm 5-Fold CV ROC-AUC: **~0.800** (cao nhất trong cả 3 mô hình)
  * Mô hình lưu tại `models/model_lightgbm.pkl`
  * Dự đoán lưu tại `submissions/submission_lightgbm.csv`
  * Biểu đồ Feature Importance tại `figures/feature_importance_lightgbm.png`

#### 4. So sánh đối đầu cả 3 mô hình
```powershell
python "04_compare_models.py"
```
* Xuất bảng so sánh tổng hợp các chỉ số (ROC-AUC, F1, Accuracy, Precision, Recall).
* Tự động vẽ và lưu biểu đồ so sánh đường cong ROC tại `figures/roc_curves_comparison.png`.

---

### 📊 Xem Sổ Tay Phân Tích (Jupyter Notebook)
Mở file `notebooks/HR_Analytics_Exploration_and_Modeling.ipynb` trong Visual Studio Code hoặc Jupyter Notebook để theo dõi đầy đủ từng bước thực hiện từ EDA, trực quan hóa biểu đồ phân bố đến đánh giá mô hình.
