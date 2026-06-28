import numpy as np
import pandas as pd
from app.modules.feature_store.exceptions import FeatureValidationFailed

class FeatureValidator:
    def validate_features_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Validates computed features against data quality constraints.
        Cleans or raises validation exception on failure.
        """
        # Exclude key identification columns for values check
        val_cols = df.select_dtypes(include=[np.number]).columns
        
        # 1. Assert no NaN values
        # If NaN exists, we fill with 0.0 or raise if too many nulls
        for col in val_cols:
            null_count = df[col].isnull().sum()
            if null_count > 0:
                null_ratio = null_count / len(df)
                if null_ratio > 0.05: # Reject if more than 5% null values
                    raise FeatureValidationFailed(f"Feature column '{col}' has high null ratio: {null_ratio:.2%}")
                df[col] = df[col].fillna(0.0)

        # 2. Assert no infinite values (inf / -inf)
        for col in val_cols:
            if np.isinf(df[col]).any():
                # Replace infinite values with 0.0 or threshold bounds
                df[col] = df[col].replace([np.inf, -np.inf], 0.0)

        # 3. Outlier detection & Winsorization capping (limit outliers to 5 standard dev boundaries)
        for col in val_cols:
            col_mean = df[col].mean()
            col_std = df[col].std()
            if col_std > 0:
                # Cap values exceeding +/- 5 standard deviations
                lower_limit = col_mean - 5 * col_std
                upper_limit = col_mean + 5 * col_std
                df[col] = np.clip(df[col], lower_limit, upper_limit)

        return df
