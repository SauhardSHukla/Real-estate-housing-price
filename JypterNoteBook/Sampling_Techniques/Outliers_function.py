def tag_outliers(df, col, method='zscore', threshold=3):
    if method == 'zscore':
        z_scores = (df[col] - df[col].mean()) / df[col].std()
        mask = (z_scores > -threshold) & (z_scores < threshold)
        filtered_df = df[mask]

    elif method == 'iqr':
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        mask = (df[col] >= lower_bound) & (df[col] <= upper_bound)
        filtered_df = df[mask]

    print(f"{col}: Removed {len(df) - len(filtered_df)} outliers")
    return filtered_df
