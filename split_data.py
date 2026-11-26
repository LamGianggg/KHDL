# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

data_dir = os.path.dirname(os.path.abspath(__file__))
train_path = os.path.join(data_dir, "aug_train.csv")

print(f"[INFO] Doc du lieu tu: {train_path}")
df = pd.read_csv(train_path)
total_len = len(df)
print(f"[INFO] Tong so dong trong aug_train.csv: {total_len}")

# Tach 60% train va 40% tam thoi (Stratified ngau nhien theo target)
train_df, temp_df = train_test_split(df, test_size=0.40, random_state=42, stratify=df['target'])

# Tach 40% thanh 20% val va 20% test
val_df, test_df = train_test_split(temp_df, test_size=0.50, random_state=42, stratify=temp_df['target'])

train_out = os.path.join(data_dir, "train_60.csv")
val_out = os.path.join(data_dir, "val_20.csv")
test_out = os.path.join(data_dir, "test_20.csv")

train_df.to_csv(train_out, index=False)
val_df.to_csv(val_out, index=False)
test_df.to_csv(test_out, index=False)

print(f"[OK] Tap Train (60%): {len(train_df):,} dong ({len(train_df)/total_len:.1%}) -> {train_out}")
print(f"     Ty le target: {dict(train_df['target'].value_counts())} ({dict(train_df['target'].value_counts(normalize=True).round(4))})")

print(f"[OK] Tap Validation (20%): {len(val_df):,} dong ({len(val_df)/total_len:.1%}) -> {val_out}")
print(f"     Ty le target: {dict(val_df['target'].value_counts())} ({dict(val_df['target'].value_counts(normalize=True).round(4))})")

print(f"[OK] Tap Test (20%): {len(test_df):,} dong ({len(test_df)/total_len:.1%}) -> {test_out}")
print(f"     Ty le target: {dict(test_df['target'].value_counts())} ({dict(test_df['target'].value_counts(normalize=True).round(4))})")

print(f"[XAC NHAN] Tong cong: {len(train_df) + len(val_df) + len(test_df):,} / {total_len:,} dong. Khong mat mat bat ky ban ghi nao!")
