import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("titanic_dataset.csv")

# Count passengers in each class
passenger_counts = df["Pclass"].value_counts().sort_index()

# Create bar plot
plt.bar(passenger_counts.index, passenger_counts.values)

# Add axis labels
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

# Add title
plt.title("Number of Titanic Passengers by Class")

# Set x-axis ticks
plt.xticks([1, 2, 3])

# Display the plot
plt.show()

