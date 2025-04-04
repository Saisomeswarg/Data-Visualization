import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource

#1.Create a scatter plot to visualize the relationship between two variables, by generating a synthetic dataset.
np.random.seed(45)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 2
plt.scatter(x, y, color = 'red', alpha = 0.7, edgecolors = 'black')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
plt.title('Scatter plot of Synehtic Dataset')
plt.grid(True, linestyle = '--', alpha = 0.6) 
plt.show()

#2. Generate a dataset of random numbers. Visualize the distribution of a numerical variable.
np.random.seed(45)
data = np.random.randn(1000)
plt.figure(figsize = (8, 5))
plt.hist(data, bins = 30, color = 'red', edgecolor = 'black', alpha = 0.7)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram - Distrubution of Numerical Variable')
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.show()

#3.Create a dataset representing categories and their corresponding values. Compare different categories based on numerical values.
categories = ['category A', 'category B', 'category C', 'category D', 'category E']
values = [50, 80, 60, 90, 70]
data1 = pd.DataFrame({'categories': categories, 'values': values})
plt.figure(figsize = (8, 5))
plt.bar(data1['categories'], data1['values'], color = ['blue', 'green', 'red', 'orange'], alpha = 0.7, edgecolor = 'black')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Comparison of Categories based on Values')
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.show()

#4.Generate a dataset with categories and numerical values. Visualize the distribution of a numerical variable across different categories.
np.random.seed(42)
num = 200  
categories1 = np.random.choice(['A', 'B', 'C', 'D', 'E'], num)  
values1 = np.random.randint(0, 100, num)  

print(f"Length of categories1: {len(categories1)}, Length of values1: {len(values1)}")

df1 = pd.DataFrame({'Category': categories1, 'Value': values1})

plt.figure(figsize=(8, 5))
sns.boxplot(x='Category', y='Value', data=df1, palette='rainbow')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot - Distribution of Numerical Variable Across Different Categories')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#5.Generate a synthetic dataset with correlated features. Visualize the correlation matrix of a dataset using a heatmap.
np.random.seed(42)
size = 200
x1 = np.random.randn(size)
x2 = x1 * 0.8 + np.random.randn(size) * 0.2
x3 = x1 * -0.5 + np.random.randn(size) * 0.3
x4 = np.random.randn(size)

df = pd.DataFrame({'Feature 1': x1, 'Feature 2': x2, 'Feature 3': x3, 'Feature 4': x4})
correlation = df.corr()

plt.figure(figsize=(8, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt = '.2f', linewidths=0.5)
plt.title('Heat Map - Correlation Matrix of Dataset')
plt.show()