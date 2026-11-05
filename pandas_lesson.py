import pandas as pd

df = pd.read_csv('titanic_dataset.csv')

print(df.describe())

# mean_age = df["Age"].mean()
# print(f"The average age of the dataset  is {mean_age}")

print(round(df.loc[:, ["Age"]].describe().loc["mean"], 2))
breakpoint()

minimum_age = df["Age"].min()
print(f"The min age of the dataset  is {minimum_age}")

df_new = df.loc[:10, ["Name", "Age", "Survived"]]

print(df_new)

df_survived = df[df["Survived"] == 1]
df_not_survived = df[df["Survived"] == 0]
print(df_survived)
print(f"The percentage of not surived is {len(df_not_survived)/len(df)*100:.2f}%")

df_not_survived = df_not_survived.loc[:, ["Name", "Sex", "Pclass"]]
print(df_not_survived)

df_2 = df.iloc[0:5, 0:3]
print(df_2)

df_3 = df.iloc[-10:, :-2]
print(df_3)