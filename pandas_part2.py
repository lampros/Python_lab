import pandas as pd

# df = pd.read_csv(r"C:\Users\lampr\Documents\Python_lab\titanic_dataset.csv")
df = pd.read_csv('titanic_dataset.csv')

df.columns = df.columns.str.lower()
print("The size of the dataframe is ", len(df))

df_new = df[["age", "survived"]]

print(df_new.head(10))

df.rename(columns={"sibsp": "siblings_spouses_aboard", "parch":"parents_children"}, inplace=True)
df.info()
print(df.tail(5))


filtered_df = df.loc[(df["pclass"].isin([1,2])) & (df["survived"] == 0) & (df["age"] > 30), 
                    ["name", "age", "pclass", "fare", "survived"]]

print(filtered_df)



additional_filtered_df = df.loc[(df["sex"] == "female") & (df["pclass"] == 3) 
                                & (df["siblings_spouses_aboard"] >= 1)]
print(additional_filtered_df)


df["family_size"] = (df["siblings_spouses_aboard"] + df["parents_children"])
print(df)
df.info()

# check for null values 
missing_values = df.isna()
print(missing_values)

missing_values_sum = df.isna().sum()
print(missing_values_sum)

# For the Age column: Fill missing values with the median.
median_age = df["age"].median()
print(median_age)
df["age"] = df["age"].fillna(median_age)
print(df["age"].isna().sum())

# Drop any rows where the Embarked column is missing.
df.dropna(subset=['embarked'], axis = 0, inplace= True)
print(df.isna().sum())
print("The new size of df is", len(df))

# Drop any column where more than 50% of its values are missing 889 / 2 = 444.5
df.dropna(thresh= 445, axis= 1, inplace= True)
print("the sum of missing values after applying the threshold is: \n ", df.isna().sum())
print("Final DataFrame shape:", df.shape)


# Display the first 5 rows after handling missing data.
print(df.columns)
print(df.head(5))