import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("titanic_dataset.csv")

# Create scatter plot
plt.scatter(df["Age"], df["Fare"])

# Add axis labels
plt.xlabel("Age")
plt.ylabel("Fare")

# Add title
plt.title("Titanic Passengers: Age vs Fare")

plt.savefig("titanic_age_fare.pdf")

# Display the plot
plt.show()

