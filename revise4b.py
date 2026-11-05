import pandas as pd


# Load the dataset
df = pd.read_csv("titanic_dataset.csv")

print(df.columns)

df.rename(
   columns= {
"SibSp": "siblings_spouses", 
"Parch": "parents_children"

   }
    , inplace= True

)

print(df.columns)


passenger_info = df[["Name", "Age", "Sex", "Pclass"]]
print(passenger_info.head(5))

df["family_members_aboard"] = df["siblings_spouses"] + df["parents_children"]
print(df.loc[:4, ["siblings_spouses", "parents_children", "family_members_aboard"]])

passenger_info_reduced = passenger_info.drop(columns = "Sex")

print("after drop", passenger_info_reduced.columns)

print("before drop", passenger_info.columns)

passenger_rows_reduced = passenger_info.drop(index=[0, 2, 4])
print(passenger_rows_reduced.head(6))

passengers_over_30 = passenger_info[passenger_info["Age"] > 30]
passengers_over_30 = df.loc[df["Age"] > 30, ["Name", "Age", "Sex", "Pclass"]]


female_passengers_over_30 = passenger_info.loc[(passenger_info["Sex"] == "female") & (passenger_info["Age"] > 30), ["Age"]]

print(female_passengers_over_30.head(10))


female_first_second_class = passenger_info.loc[(passenger_info["Sex"] == "female") & (passenger_info["Pclass"].isin([1, 2])), ["Name", "Age", "Pclass"]]
print(female_first_second_class.head(10))


not_first_class = passenger_info.loc[~passenger_info["Pclass"].isin([1]), ["Name", "Sex", "Pclass"]]
print(not_first_class.head(10))

passengers_known_age = passenger_info.dropna(subset=["Age"])
print(passengers_known_age.head(10))

print("before dropna", len(passenger_info))
print("after dropna", len(passengers_known_age))


complete_rows = df.dropna()
print(len(complete_rows))

df_threshold= df.dropna(thresh = 446, axis=1)

print(df_threshold.columns)

df_inplace = df.copy()
df_inplace.dropna(thresh = 446, inplace = True, axis= 1)

df_filled = df.copy()
median_age = df_filled["Age"].median()
print(median_age)


df_filled["Age"] = df_filled["Age"].fillna(median_age)

print(df_filled["Age"].isna().sum())

df_filled["Embarked"] = df_filled["Embarked"].fillna("Unknown")

print(df_filled["Embarked"].isna().sum())

print(df_filled.isna().sum())

print(df_filled["Embarked"].unique())


practice_df = pd.DataFrame(
    {
        "Score": [10, None, None, 40, None]
    }
)

print(practice_df.head(10))

forward_filled = practice_df.ffill(axis=0)
print(forward_filled.head(10))



practice_df = pd.DataFrame(
    {
        "Score": [10, None, None, 40, None]
    }
)

print(practice_df.head(10))

backward_filled = practice_df.bfill(axis=0)
print(backward_filled.head(10))


print(female_first_second_class.head(10))

female_class_reset = female_first_second_class.copy()

print(female_class_reset.head(10))

female_class_reset = female_class_reset.reset_index(drop=True)

print(female_class_reset.head(10))

print(df.dtypes)