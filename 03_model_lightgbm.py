"""
MÔ HÌNH 3: LIGHTGBM CLASSIFIER CHO BÀI TOÁN HR ANALYTICS
- Dữ liệu đầu vào: 100% dạng số (Integer/Float), 0 NaN, 0 số âm (-1)
- Thuật toán: LightGBM (Gradient Boosting Decision Tree)
- Đánh giá: 5-Fold Stratified Cross Validation & Feature Importance
- Lưu trữ: Mô hình xuất ra models/model_lightgbm.pkl
- Dự đoán kiểm thử: Xuất file submissions/submission_lightgbm.csv
"""

import os
import sys

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.metrics import (
    roc_auc_score,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)

from src.data_preprocessing import get_train_data, get_test_data

def main():
    print("=" * 65)
    print("[BAT DAU] HUAN LUYEN MO HINH 3: LIGHTGBM (100% NUMERIC)")
    print("=" * 65)
    
    # 1. Đường dẫn
    train_path = os.path.join(CURRENT_DIR, "aug_train.csv")
    test_path = os.path.join(CURRENT_DIR, "aug_test.csv")
    models_dir = os.path.join(CURRENT_DIR, "models")
    subs_dir = os.path.join(CURRENT_DIR, "submissions")
    figs_dir = os.path.join(CURRENT_DIR, "figures")
    
    for d in [models_dir, subs_dir, figs_dir]:
        os.makedirs(d, exist_ok=True)

    # 2. Đọc dữ liệu sạch dạng số 100%
    print("[INFO] Dang tai va chuyen doi 100% du lieu sang dang so (khong NaN, khong -1)...")
    X, y, df_clean, stats = get_train_data(train_path)
    print(f"   - So luong mau: {X.shape[0]:,} dong")
    print(f"   - So luong thuoc tinh dau vao (100% so): {X.shape[1]} dac trung")
    print(f"   - Kiem tra NaN: {X.isna().sum().sum()} | Kiem tra -1: {(X == -1).sum().sum()}")

    # 3. Pipeline LightGBM
    clf = LGBMClassifier(
        n_estimators=150,
        learning_rate=0.05,
        num_leaves=31,
        max_depth=6,
        scale_pos_weight=3.0,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        verbose=-1
    )
    
    model_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', clf)
    ])

    # 4. Đánh giá chéo 5-Fold Stratified Cross-Validation
    print("\n[EVAL] Dang thuc hien 5-Fold Stratified Cross-Validation...")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scoring = {
        'roc_auc': 'roc_auc',
        'f1': 'f1',
        'precision': 'precision',
        'recall': 'recall',
        'accuracy': 'accuracy'
    }
    cv_results = cross_validate(model_pipeline, X, y, cv=skf, scoring=scoring, n_jobs=-1)
    
    print("-" * 50)
    print("KET QUA DANH GIA CHEO (5-FOLD CROSS VALIDATION):")
    print(f"   • ROC-AUC Score : {cv_results['test_roc_auc'].mean():.4f} (+/- {cv_results['test_roc_auc'].std():.4f})")
    print(f"   • F1 Score (Lop 1): {cv_results['test_f1'].mean():.4f} (+/- {cv_results['test_f1'].std():.4f})")
    print(f"   • Precision     : {cv_results['test_precision'].mean():.4f}")
    print(f"   • Recall        : {cv_results['test_recall'].mean():.4f}")
    print(f"   • Accuracy      : {cv_results['test_accuracy'].mean():.4f}")
    print("-" * 50)

    # 5. Huấn luyện trên Holdout Test Set (80/20) để đánh giá chi tiết
    print("\n[EVAL] Danh gia chi tiet tren tap kiem dinh doc lap (Hold-out 20%)...")
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model_pipeline.fit(X_train, y_train)
    
    y_val_pred = model_pipeline.predict(X_val)
    y_val_proba = model_pipeline.predict_proba(X_val)[:, 1]
    
    print("\nBAO CAO PHAN LOP CHI TIET (CLASSIFICATION REPORT):")
    print(classification_report(y_val, y_val_pred, target_names=["O lai (0)", "Doi viec (1)"]))

    # Vẽ và lưu Confusion Matrix
    cm = confusion_matrix(y_val, y_val_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["O lai (0)", "Doi viec (1)"])
    fig, ax = plt.subplots(figsize=(6, 5))
    disp.plot(cmap="Oranges", ax=ax, values_format="d")
    ax.set_title("Confusion Matrix - LightGBM (All Numeric)")
    plt.tight_layout()
    cm_path = os.path.join(figs_dir, "confusion_matrix_lightgbm.png")
    plt.savefig(cm_path, dpi=300)
    plt.close()
    print(f"   [PLOT] Da luu bieu do Confusion Matrix vao: {cm_path}")

    # 6. Trích xuất Feature Importance
    print("\n[FEATURE] Dang phan tich muc do quan trong cua dac trung (Feature Importance)...")
    fitted_lgb = model_pipeline.named_steps['classifier']
    feature_names = X.columns
    importances = fitted_lgb.feature_importances_
    
    feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    feat_imp.sort_values().plot(kind='barh', color='#ff7f0e')
    plt.title("Feature Importance - LightGBM (All 12 Numeric Features)")
    plt.xlabel("Split Importance Score")
    plt.tight_layout()
    feat_path = os.path.join(figs_dir, "feature_importance_lightgbm.png")
    plt.savefig(feat_path, dpi=300)
    plt.close()
    print(f"   [PLOT] Da luu bieu do Feature Importance vao: {feat_path}")
    print(f"   Top 3 dac trung anh huong manh nhat: {list(feat_imp.head(3).index)}")

    # 7. Huấn luyện toàn diện và lưu file pkl
    print("\n[SAVE] Dang huan luyen lai tren 100% du lieu train va luu mo hinh...")
    model_pipeline.fit(X, y)
    model_save_path = os.path.join(models_dir, "model_lightgbm.pkl")
    joblib.dump(model_pipeline, model_save_path)
    print(f"   [OK] Da luu mo hinh hoan chinh vao: {model_save_path}")

    # 8. Dự đoán trên tập aug_test.csv
    print("\n[PREDICT] Dang du doan tren tap kiem thu aug_test.csv...")
    X_test, test_ids = get_test_data(test_path, stats)
    test_preds_proba = model_pipeline.predict_proba(X_test)[:, 1]
    
    submission_df = pd.DataFrame({
        'enrollee_id': test_ids,
        'target': np.round(test_preds_proba, 4)
    })
    
    sub_path = os.path.join(subs_dir, "submission_lightgbm.csv")
    submission_df.to_csv(sub_path, index=False)
    print(f"   [OK] Da xuat ket qua du doan vao: {sub_path}")
    print(f"   - So luong ung vien duoc du doan: {len(submission_df):,} nguoi")
    print(f"   - 5 dong du doan dau tien:\n{submission_df.head()}")
    print("\n" + "=" * 65)
    print("[HOAN TAT] HUAN LUYEN VA DU DOAN MO HINH 3 (LIGHTGBM) THANH CONG!")
    print("=" * 65)

if __name__ == "__main__":
    main()
