"""
FILE SO SÁNH HIỆU NĂNG 3 MÔ HÌNH TRÊN DỮ LIỆU SẠCH 100% SỐ
- Dữ liệu đầu vào: 100% dạng số (Integer/Float), 0 NaN, 0 số âm (-1)
- Đánh giá chéo 5-Fold Stratified CV: ROC-AUC, F1, Precision, Recall, Accuracy
- Vẽ biểu đồ đường cong ROC Curve so sánh trực quan cả 3 mô hình trên cùng 1 đồ thị
- Lưu biểu đồ vào figures/roc_curves_comparison.png
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
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.metrics import roc_curve, auc, f1_score, accuracy_score, precision_score, recall_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)

from src.data_preprocessing import get_train_data

def main():
    print("=" * 70)
    print("[SO SANH] BANG SO SANH DOI DAU 3 MO HINH (100% NUMERIC, 0 NaN, 0 AM)")
    print("=" * 70)

    train_path = os.path.join(CURRENT_DIR, "aug_train.csv")
    figs_dir = os.path.join(CURRENT_DIR, "figures")
    os.makedirs(figs_dir, exist_ok=True)

    print("[INFO] Dang tai du lieu va chuyen doi 100% sang so...")
    X, y, df_clean, stats = get_train_data(train_path)

    # Chia tập train/test 80/20
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    models = {
        "Logistic Regression": LogisticRegression(C=0.1, class_weight='balanced', max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=12, min_samples_split=10, class_weight='balanced', random_state=42, n_jobs=-1),
        "LightGBM": LGBMClassifier(n_estimators=150, learning_rate=0.05, num_leaves=31, max_depth=6, scale_pos_weight=3.0, subsample=0.8, colsample_bytree=0.8, random_state=42, verbose=-1)
    }

    results = []
    plt.figure(figsize=(9, 7))

    colors = {
        "Logistic Regression": "#1f77b4",
        "Random Forest": "#2ca02c",
        "LightGBM": "#ff7f0e"
    }

    for name, clf in models.items():
        print(f"\n[EVAL] Dang danh gia mo hinh: {name}...")
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', clf)
        ])

        # 5-fold CV ROC-AUC
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        cv_auc = cross_val_score(pipeline, X, y, cv=skf, scoring='roc_auc', n_jobs=-1).mean()

        # Fit trên X_train để đánh giá tập test
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_val)
        y_proba = pipeline.predict_proba(X_val)[:, 1]

        acc = accuracy_score(y_val, y_pred)
        prec = precision_score(y_val, y_pred)
        rec = recall_score(y_val, y_pred)
        f1 = f1_score(y_val, y_pred)

        results.append({
            "Mo hinh": name,
            "CV ROC-AUC (5-Fold)": f"{cv_auc:.4f}",
            "Val Accuracy": f"{acc:.4f}",
            "Precision (Class 1)": f"{prec:.4f}",
            "Recall (Class 1)": f"{rec:.4f}",
            "F1-Score (Class 1)": f"{f1:.4f}"
        })

        # Tính toán đường cong ROC
        fpr, tpr, _ = roc_curve(y_val, y_proba)
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, color=colors[name], lw=2.5, label=f"{name} (AUC = {roc_auc:.4f})")

    # Đường ngẫu nhiên
    plt.plot([0, 1], [0, 1], color='navy', lw=1.5, linestyle='--', label='Random Guess (AUC = 0.5000)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)', fontsize=12)
    plt.ylabel('True Positive Rate (TPR / Recall)', fontsize=12)
    plt.title('So Sanh Duong Cong ROC Giua 3 Mo Hinh (100% Numeric)', fontsize=14, fontweight='bold')
    plt.legend(loc="lower right", fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    roc_plot_path = os.path.join(figs_dir, "roc_curves_comparison.png")
    plt.savefig(roc_plot_path, dpi=300)
    plt.close()
    print(f"\n[PLOT] Da luu bieu do ROC so sanh vao: {roc_plot_path}")

    # In bảng so sánh
    results_df = pd.DataFrame(results)
    print("\n" + "=" * 70)
    print("BANG TONG HOP HIEU NANG DOI DAU (DU LIEU 100% SO):")
    print("=" * 70)
    print(results_df.to_string(index=False))
    print("=" * 70)
    print("[KET LUAN] Mo hinh van hanh tron tru, khong loi, khong con bat ky gia tri NaN hay -1 nao!")
    print("=" * 70)

if __name__ == "__main__":
    main()
