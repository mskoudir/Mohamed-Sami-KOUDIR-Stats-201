import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('../data/adult_income.csv')

# Basic Exploratory Data Analysis (EDA)
print("Dataset Info:")
print(data.info())  # Information about the dataset (e.g., data types, null values)
print("\nDataset Description:")
print(data.describe(include='all'))  # Descriptive statistics for both numerical and categorical data

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())  # Summing up missing values per column

# Check data types of columns
print("\nData Types:")
print(data.dtypes)

# Visualizations

# 1. Income distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='income', data=data, palette='Set2')
plt.title('Income Distribution (<=50K vs >50K)')
plt.xlabel('Income Level')
plt.ylabel('Count')
plt.show()

# 2. Visualize the distribution of numerical features
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns

plt.figure(figsize=(12, 10))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(3, 3, i)  # Creating subplots to show distributions of numerical features
    sns.histplot(data[col], kde=True, color='blue')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 3. Categorical feature distribution
categorical_cols = data.select_dtypes(include=['object']).columns

plt.figure(figsize=(12, 12))
for i, col in enumerate(categorical_cols, 1):
    plt.subplot(3, 3, i)  # Creating subplots to show categorical feature distributions
    sns.countplot(x=col, data=data, palette='Set3')
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)
    plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 4. Correlation matrix for numerical features
correlation_matrix = data[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# 5. Boxplots for numerical columns grouped by income
plt.figure(figsize=(14, 8))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(x='income', y=col, data=data, palette='Set2')
    plt.title(f'Boxplot of {col} by Income')
    plt.ylabel(col)
    plt.xlabel('Income Level')
plt.tight_layout()
plt.show()

# 6. Pairplot of selected features
selected_features = ['age', 'hours-per-week', 'education-num', 'capital-gain', 'capital-loss', 'income']
sns.pairplot(data[selected_features], hue='income', palette='Set2')
plt.suptitle('Pairplot of Selected Features by Income', y=1.02)
plt.show()

# 7. Heatmap to detect missing values in the dataset
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('Missing Values Heatmap')
plt.show()
