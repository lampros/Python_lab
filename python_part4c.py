import pandas as pd
df = pd.read_csv('titanic_dataset.csv')
print(df.head(10))

class_counts = df["Pclass"].value_counts().sort_index()
print(class_counts)
print(type(class_counts))

survived_counts = df['Survived'].value_counts().sort_index()
print(survived_counts)

embarked_counts = df["Embarked"].value_counts(dropna=False).sort_index()
print(embarked_counts)

def double_fare(num):
    return num * 2 

print(df["Fare"].head(10))
df["DoubleFare"] = df["Fare"].apply(double_fare)

print(df[["Fare","DoubleFare"]].head(10))


def calculate_survival_score(row):
    if row["Sex"] == "female":
        return 3
    else:
        return 0

df["SurvivalScore"] = df.apply(
    calculate_survival_score,
    axis=1
)

print(
    df[["Name", "Sex", "SurvivalScore"]].head(10)
)

def calculate_priority_score(row):
    if row["Sex"] == "female" and row["Pclass"] == 1:
        return 5
    elif row["Sex"] == "female" and row["Pclass"] != 1:
        return 3
    else:
        return 0

df["PriorityScore"] = df.apply(calculate_priority_score, axis=1)

print(df.loc[:, ["Name", "Sex", "Pclass", "PriorityScore"]].head(10))

customers = pd.DataFrame({
"customer_id" : [1, 2, 3],
"name": ["Lampros", "Maria", "Helen"]
})

orders = pd.DataFrame({

"order_id" : [101, 102, 103],
"customer_id" : [1, 2, 1],
"amount" : [200, 350, 150]
})

merged_df = pd.merge(customers, orders, on="customer_id", how="inner")

print(merged_df)

left_merged_df = pd.merge(customers, orders, on="customer_id", how="left")

print(left_merged_df)