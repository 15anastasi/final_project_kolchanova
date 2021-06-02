import numpy as np
import pandas as pd
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sn
import warnings
warnings.simplefilter('ignore')
from pylab import rcParams
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm 

df = pd.read_csv('hotel_bookings.csv', error_bad_lines = False)
df.head(5)

#Проверим данные на нормальность, используя тест Шапиро-Уилка
print('Shapiro Wilk test')
print('H0: Distribution is not Normal.')
print('H0:Distribution is Normal. \n')
def shapiro_wilk(df,col):
  print('Column Name:',col)
  stat, p = shapiro(df[col])
  alpha = 0.05
  print("p value:", p) 
  if p <= alpha: 
    print('Conclusion: Distribution is Normal(reject H0)') 
  else: 
    print('Conclusion: Distribution is not Normal(H0 holds true)') 
shapiro_wilk(df,'is_canceled')
shapiro_wilk(df,'lead_time')
shapiro_wilk(df,'stays_in_weekend_nights')
shapiro_wilk(df,'stays_in_week_nights')
shapiro_wilk(df,'adults')
shapiro_wilk(df,'children')
shapiro_wilk(df,'babies')
shapiro_wilk(df,'is_repeated_guest')
shapiro_wilk(df,'previous_cancellations')
shapiro_wilk(df,'previous_bookings_not_canceled')
shapiro_wilk(df,'booking_changes')
shapiro_wilk(df,'days_in_waiting_list')
shapiro_wilk(df,'required_car_parking_spaces')
shapiro_wilk(df,'total_of_special_requests')

#Проведем t-test для
