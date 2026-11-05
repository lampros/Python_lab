import pandas as pd


# Load the dataset
df = pd.read_csv("titanic_dataset.csv")

print(df.columns())


# Rename all columns to lowercase
df.columns = df.columns.str.lower()


# Rename specific columns
df.rename(
    columns={
        "sibsp": "siblings_spouses_aboard",
        "parch": "parents_children"
    },
    inplace=True
)


# Display the last 5 rows to verify the column changes
print("Last 5 rows after renaming columns:")
print(df.tail(5))


# Display information about the DataFrame
print("\nDataFrame information:")
df.info()


# Advanced filtering:
# First or second class, did not survive, and age greater than 30
filtered_df = df.loc[
    (df["pclass"].isin([1, 2]))
    & (df["survived"] == 0)
    & (df["age"] > 30),
    ["name", "age", "pclass", "fare", "survived"]
]

print("\nFiltered passengers:")
print(filtered_df.head())


# Additional filtering:
# Female passengers in third class with at least one
# sibling or spouse aboard
additional_filtered_df = df[
    (df["sex"] == "female")
    & (df["pclass"] == 3)
    & (df["siblings_spouses_aboard"] >= 1)
]

print("\nAdditionally filtered passengers:")
print(additional_filtered_df.head())

# new column family_size
df["family_size"] = df["siblings_spouses_aboard"] + df["parents_children"]

print(
    df[
        [
            "siblings_spouses_aboard",
            "parents_children",
            "family_size"
        ]
    ].head()
)

print(df.isna().sum())
# filling age colmun with median.


