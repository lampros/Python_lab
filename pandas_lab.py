import pandas as pd
# Load the Dataset 
df = pd.read_csv(r"C:\Users\lampr\Documents\Python_lab\titanic_dataset.csv")
print(df.head(5))     
print(df.dtypes)    
df.info() 
print("Statisical Summary:")
print(df.describe())

# Data exploration
mean_age = df["Age"].mean()
print(f"The mean age of the passengers is {mean_age}")

min_age = df["Age"].min()
print(f"The minimun age of the passengers is {min_age}")

# Data selection with loc
print(df.loc[0:9, ["Name", "Age", "Survived"]])

not_survived = df[df["Survived"] == 0]
print(f"The passengers who did not survived are \n: {not_survived}")

percentage = len(not_survived) / len(df) * 100

print(f"The percentage of passengers who did not survive: {percentage:.2f}%")

print(not_survived[["Name", "Sex", "Pclass"]])

# Data selection with iloc 
print(df.iloc[0:5, 0:3])
print(df.iloc[-10:, ::-2])




