import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro

def check_data_for_probability_analysis(df, column):
    print(f"\n Analyzing column: '{column}'")

    # Basic properties
    print("\n Data Type:", df[column].dtype)
    print(" Number of Unique Values:", df[column].nunique())
    print(" Sample Size:", df[column].dropna().shape[0])

    # Discrete or Continuous check (basic)
    unique_values = df[column].dropna().unique()
    if df[column].dtype in [int, 'int64'] and df[column].nunique() < 20:
        print(" Likely Discrete")
    elif df[column].dtype in [float, 'float64'] or df[column].nunique() > 20:
        print(" Likely Continuous")
    else:
        print(" Could be either — check domain knowledge")

# -----------------------------------------------------------------------------------
# Already checked the outliers we don't need it right now but if any new column 
# added so we can use it

    # # Check for outliers
    # Q1 = df[column].quantile(0.25)
    # Q3 = df[column].quantile(0.75)
    # IQR = Q3 - Q1
    # outliers = df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]
    # print(f" Outliers Detected: {len(outliers)}")
# ------------------------------------------------------------------------------------

    # Shapiro-Wilk Normality Test (for continuous data)
    if df[column].dtype in ['float64', 'int64'] and df[column].nunique() > 30:
        print("\n Normality Check (Shapiro-Wilk test):")
        stat, p = shapiro(df[column].sample(n=min(5000, len(df[column].dropna())), random_state=42))
        print(f"   W = {stat:.3f}, p-value = {p:.4f}")
        if p > 0.05:
            print("    Looks Normally Distributed (p > 0.05)")
        else:
            print("    Not Normally Distributed (p ≤ 0.05)")

    # Plot Histogram
    
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column].dropna(), kde=True, bins=20, edgecolor='black')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    print("\n Distribution Plot:")
    plt.show()
