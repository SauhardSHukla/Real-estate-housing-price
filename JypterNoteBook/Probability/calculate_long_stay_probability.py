from scipy.stats import binom

def calculate_long_stay_probability_function(df,duration_threshold =60,prob =0.4):
  
  #Step1: Estimate overall long stay probability from Dataset
  df['Long_stay'] = (df['Duration_min']>duration_threshold).astype(int)
  p=df['Long_stay'].mean().round(3)

   # Step 2: For each customer, compute P(X = k) where:
    # - n = Arrival_Count
    # - k = int(long_stay_percent * Arrival_Count)
  def compute_prob(row):
    n = row['Arrival_Count']
    k = int(prob * n)
    return binom.pmf(k,n,p)
  
  df['prob_long_stay'] =df.apply(compute_prob,axis =1)
  return df[['Arrival_Count', 'Duration_min', 'prob_long_stay']]