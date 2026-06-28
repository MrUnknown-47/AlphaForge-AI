import os
import pandas as pd
import numpy as np

def audit_datasets():
    data_dir = "data"
    splits = ["train", "validation", "test"]
    
    print("\n" + "=" * 60)
    print("DATASET SPLITS AUDIT RESULTS")
    print("=" * 60)
    
    for split in splits:
        path = os.path.join(data_dir, f"{split}.parquet")
        if not os.path.exists(path):
            # Check for CSV fallback
            path = os.path.join(data_dir, f"{split}.csv")
            if not os.path.exists(path):
                print(f"File not found: {split}")
                continue

        df = pd.read_parquet(path) if path.endswith(".parquet") else pd.read_csv(path)
        rows = len(df)
        
        # Calculate nulls and infs
        null_count = df.isnull().sum().sum()
        total_elements = df.size
        null_pct = (null_count / total_elements) * 100 if total_elements > 0 else 0
        
        # Numeric columns only for inf check
        num_cols = df.select_dtypes(include=[np.number])
        inf_count = np.isinf(num_cols.values).sum()
        inf_pct = (inf_count / num_cols.size) * 100 if num_cols.size > 0 else 0
        
        # Duplicates check
        time_dup = df["time"].duplicated().sum()
        pair_dup = df.duplicated(subset=["time", "ticker"]).sum()
        
        print(f"\n[{split.upper()} SPLIT]")
        print(f"  - Rows: {rows}")
        print(f"  - Null %: {null_pct:.4f}% ({null_count} null elements)")
        print(f"  - Inf %: {inf_pct:.4f}% ({inf_count} inf elements)")
        print(f"  - Duplicate Timestamps: {time_dup}")
        print(f"  - Duplicate Ticker/Time Pairs: {pair_dup}")
        
        # Targets distribution
        for target in ["target_1d", "target_5d", "target_20d"]:
            if target in df.columns:
                t_mean = df[target].mean()
                t_std = df[target].std()
                t_min = df[target].min()
                t_max = df[target].max()
                print(f"  - {target}: Mean={t_mean:.6f}, Std={t_std:.6f}, Min={t_min:.6f}, Max={t_max:.6f}")

if __name__ == "__main__":
    audit_datasets()
