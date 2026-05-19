#libraries
import pandas as pd          
import matplotlib.pyplot as plt  

print(f"Pandas version: {pd.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")

#data import

#from url
url = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv'
titanic = pd.read_csv(url)

#local
#uploaded_file_name = "/content/sample_data/california_housing_train.csv"
#uploaded_csv = pd.read_csv(uploaded_file_name)

#description
# 1. Shape of the dataset (rows, columns)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# 2. Column names
print(df.columns.tolist())

# 3. Detailed information
print(df.info())

# 4. Basic statistics (numeric columns only)
print(df.describe())