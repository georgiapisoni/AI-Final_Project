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
print(f"Rows: {titanic.shape[0]}, Columns: {titanic.shape[1]}")

# 2. Column names
print(titanic.columns.tolist())

# 3. Detailed information
print(titanic.info())

# 4. Basic statistics (numeric columns only)
print(titanic.describe())

#5. Head and tail (first and last n rows)
print(titanic.head(3))
print(titanic.tail(2))

#accessing a specific feature
print(titanic["Survived"])

#iloc -> calls the nth row
print(titanic.iloc[1])
#loc -> calls the value in the nth row and kth column
print(titanic.loc[1, 'Name'])

##MASKING
mask = titanic['Age'] > 28
print(titanic[mask])

#combined conditions
# complex_mask = (titanic['Age'] > 27) & (titanic['Salary'] > 2800)
# city_mask = (titanic['City'] == 'Milan') | (titanic['City'] == 'Rome')

#MISSING VALUES
# how many missing values there are per column
print(titanic.isnull().sum())
# Percentage of missing values
print((titanic.isnull().sum() / len(titanic) * 100).round(2))
# Remove rows with missing values in a specific column
print(f"Rows with non-empty Cabin: {len(titanic.dropna(subset=['Cabin']))}")

#column operations
print("Ticket prices multiplied by 2:")
print((titanic['Fare'] * 2))
#custom functions also available


#MODIFIYING THE DATASET
## copy of the original dataset 
titanic_mod = titanic.copy()
## after modifying and adding or dropping columns:
# titanic.drop('Fare', axis=1)

## SAVING ON FILE SYSTEM
titanic.to_csv('titanic_modified.csv', index=False)
##good practice -> reload to verify; check a portion
titanic_loaded = pd.read_csv('titanic_modified.csv')
print(titanic_loaded.head())

##dataframe CONCAT
#vertical (axis=0); stacked with same features
#horizontal (axis=1); side by side, new features

##dataframe MERGE
# 

