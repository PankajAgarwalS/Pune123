# -*- coding: utf-8 -*-
"""Practical1(wrangling).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gaW5cPkLDuuxslnZFN2tXMCeK-LiEd5V

<a href="https://colab.research.google.com/github/pankajtries/TE-COMP-SEM-6/blob/main/DS%26BDAL/Untitled1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

import pandas as pd
import numpy as np
import seaborn as sns
titanic = sns.load_dataset('titanic')

titanic.head(5)

titanic.sample(5)

titanic.info()

print("\nData Dimensions:\n")
titanic.shape

print("\nData Description:\n")
titanic.describe()

print("\nVariable Descriptions:\n")
titanic.dtypes

"""### **Removing Null values**"""

print("Data Preprocessing - Missing Values:\n")
titanic.isnull()

print("Data Preprocessing -  Sum of Missing Values:\n")
titanic.isnull().sum()

titanic['age'] = titanic['age'].fillna(titanic['age'].mean())

print("Data Preprocessing -  Sum of Missing Values after removing null values of age:\n")
titanic.isnull().sum()

titanic=titanic.drop(columns=['deck'])
titanic.isnull().sum()

titanic['embarked']=titanic['embarked'].fillna(method='ffill')
titanic.isnull().sum()

titanic['embark_town']=titanic['embark_town'].fillna(method='bfill')
titanic.isnull().sum()

titanic=titanic.dropna()
titanic.isnull().sum()

"""### **Variable types**"""

titanic.dtypes

from sklearn.preprocessing import MinMaxScaler

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Select numerical columns for normalization
numerical_columns = ['age', 'fare']

# Apply Min-Max Scaling
titanic[numerical_columns] = scaler.fit_transform(titanic[numerical_columns])

# Check the normalized values
print(titanic.head())