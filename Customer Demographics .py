import pandas as pd
import matplotlib.pyplot as plt

# Sample Customer Data
data = {
    "Customer_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Age": [22, 35, 28, 45, 31, 24, 40, 29],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Data
print("Customer Data")
print(df)

# Average Age
avg_age = df["Age"].mean()
print("\nAverage Age:", round(avg_age, 2))

# Gender Count
gender_count = df["Gender"].value_counts()
print("\nGender Distribution:")
print(gender_count)

# Gender Distribution Pie Chart
plt.figure(figsize=(6,6))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
plt.title("Customer Gender Distribution")
plt.show()

# Age Distribution Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=5)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()