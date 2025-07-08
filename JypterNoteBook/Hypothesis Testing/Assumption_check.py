"""
We will create a function to check the Normality testing and the Equal variance 
checking of the different coloumn of the Dataframe 
"""
#import lib.
from scipy.stats import levene,shapiro

# Normality Test
def check_Normality(df,Group_name ='Group'):
  print(f'Checking the normality of the Group {Group_name}\n')

  stats,p = shapiro(df.dropna())
  print(f'Shapiro test result statisticcs:{stats:.4f} , p-value:{p:.4f}\n')

  if p > 0.05:
    print(' ✅ Likely normal distribution.')
    print("-"*60)
  else:
    print(' ❌ Not Likely normal distribution.')
    print("-"*60)
  

#Check Variablity
def check_equal_variance(g1,g2,label_1='group_1',label_2='group_2'):
  """
    Perform Levene Test for equal variance.
  """
  print(f'Checking the variance test btw {label_1} and {label_2}\n')
  stats,p = levene(g1,g2)
  print(f'Levene test result statisticcs:{stats:.4f} , p-value:{p:.4f}\n')

  if p > 0.05:
    print('✅ Likely equal var .')
    print("-"*60)
  else:
    print(' ❌ Not equal var. ')
    print("-"*60)
