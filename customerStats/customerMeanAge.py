import pandas as pd
import numpy as np

# %matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Read in data into a dataframe
df = pd.read_csv('customer.csv')

# Show the first 5 (or 10) rows of the table
# df.tail(10)

df = df.iloc[:,:4]
# df = df.iloc[:,:]
# df.head()

desc = df.describe()

print(desc)
