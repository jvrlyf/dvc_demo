import pandas as pd
import numpy as np
import os

df = pd.read_csv('/Volumes/JV-R/Projects/MLOps/Compus X/Ecommerce Customers.csv')

df = df.iloc[:, 3:]

df = df[df['Length of Membership'] > 3]

df.to_csv(os.path.join('data','customer.csv'))