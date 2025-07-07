def detect_outlier_zscore(df,col_name,threshold=3):
  df_copy = df.copy()
  mean = df_copy[col_name].mean()
  std = df_copy[col_name].std()
  z_score=(df[col_name] - mean)/std
  df[f'Outliers_{col_name}'] = z_score.abs()>threshold
  return df

def detect_outlier_IOR(df,col_names):
  df_copy =df.copy()
  Q1=  df[col_names].quantile(0.25)
  Q3=  df[col_names].quantile(0.75)
  IQR = Q3-Q1
  Lower = Q1-1.5*IQR
  Upper = Q3+1.5*IQR
  df[f'Outliers_{col_names}'] =~df[col_names].between(Lower,Upper)
  return df
  

