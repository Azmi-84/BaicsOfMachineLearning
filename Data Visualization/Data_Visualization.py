import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
# Plot a time-series line plot for a chosen feature
plt.figure(figsize=(14, 6))
plt.plot(data.index, data.iloc[:, 0])
plt.title('Time Series of Feature 1')
plt.xlabel('Time')
plt.ylabel('Feature Value')
plt.show()


# Assume the first few columns represent different measurements
fig = px.scatter_matrix(pd.DataFrame(data_scaled), dimensions=range(4), title="Feature Scatter Matrix")
fig.show()

# Plot distribution of a feature (choose a feature index to analyze)
sns.histplot(data.iloc[:, 0], kde=True)
plt.title('Distribution of Feature 1')
plt.show()


# Plot correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(pd.DataFrame(data_scaled).corr(), annot=False, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()


scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


# Base directory for file paths
base_dir = '/home/abdullahalazmi/PycharmProjects/BaicsOfMachineLearning/Data Visualization/secom/'

# Load the main data and labels files
data = pd.read_csv(f'{base_dir}secom.data', sep=" ", header=None)
labels = pd.read_csv(f'{base_dir}secom_labels.data', header=None)

# Load the names file as a plain text file to get column names
try:
    with open(f'{base_dir}secom.names', 'r') as file:
        feature_names = [line.strip() for line in file if line.strip()]  # Remove empty lines and strip whitespace
    print("Feature names loaded successfully:")
    print(feature_names[:10])  # Display first 10 feature names for verification

    # Assign names as column headers to the data DataFrame
    if len(feature_names) == data.shape[1]:  # Ensure number of names matches the number of columns
        data.columns = feature_names
    else:
        print("Warning: Number of feature names does not match the number of columns in data.")
except FileNotFoundError:
    print("File secom.names not found in the specified directory.")
except Exception as e:
    print(f"An error occurred while loading feature names: {e}")

# Display the first few rows of the data with feature names as headers (if applied)
print("Data sample with feature names:")
print(data.head())

# Display the labels sample
print("Labels sample:")
print(labels.head())

# Check for missing values
missing_data = data.isnull().sum()
print(missing_data[missing_data > 0])

# Impute missing values with column means
data = data.fillna(data.mean())
