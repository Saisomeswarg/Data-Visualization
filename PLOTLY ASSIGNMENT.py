import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

#1. Using the given dataset, to generate a 3D scatter plot to visualize the distribution of data points in a three dimensional space.
np.random.seed(30)
data = {
    'X': np.random.uniform(-10, 10, 300),
    'Y' : np.random.uniform(-10, 10, 300),
    'Z' : np.random.uniform(-10, 10, 300)
}

df = pd.DataFrame(data)
fig = px.scatter_3d(df, x='X', y='Y', z='Z', title = '3D Scatter Plot', color = df['Z'], color_continuous_scale = 'Viridis', opacity = 0.7)
#fig.show()

#2.Using the Student Grades, create a violin plot to display the distribution of scores across different grade categories.
np.random.seed(15)
data1 = {
    'Grade' : np.random.choice(['A', 'B', 'C', 'D', 'E'], 200),
    'Score' : np.random.randint(50, 100, 200)
}

df_grades = pd.DataFrame(data1)

plt.figure(figsize = (8, 5))
sns.violinplot(x='Grade', y='Score', data=df_grades, hue='Grade', palette='coolwarm', legend=False)
plt.xlabel('Grade Categories')
plt.ylabel('Scores')
plt.title('Violin Plot - Distribution of Scores Across Different Grade Categories')
plt.grid(True, linestyle = '--', alpha = 0.6)
#plt.show()

#3. Using the sales data, generate a heatmap to visualize the variation in sales across different months and days.
np.random.seed(20)

data2 = {
    'Month' : np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 1000),
    'Day' : np.random.choice(range(1, 31), 1000),
    'Sales' : np.random.randint(1000, 10000, 1000)
 }

df_sales = pd.DataFrame(data2)
sales_pivot = df_sales.pivot_table(index = 'Month', columns = 'Day', values = 'Sales', aggfunc = np.sum)
plt.figure(figsize = (10, 6))
sns.heatmap(sales_pivot, cmap = 'coolwarm', annot = True,  fmt = "0.1f", linewidths = 0.5)
plt.title('Heatmap - Variation in Sales Across Different Months and Days')
#plt.show()

#4.Using the given x and y data, generate a 3D surface plot to visualize the function
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
data3 = {
    'X': x.flatten(),
    'Y': y.flatten(),
    'Z': z.flatten()
}
df1 = pd.DataFrame(data3)

fig = plt.figure(figsize = (10, 7))
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x, y, z, cmap = 'viridis', edgecolor = 'k')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Surface Plot - Visualizing the Function of  z = sin(sqrt(x² + y²))')
#plt.show()

#5. Using the given dataset, create a bubble chart to represent each country's population (y-axis), GDP (x axis), and bubble size proportional to the population.
np.random.seed(25)
data4 = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),  # Population in millions
    'GDP': np.random.randint(500, 2000, 5)  # GDP in billions
}
df2 = pd.DataFrame(data4)
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df2['GDP'], df2['Population'], 
                      s=df2['Population'] * 10, 
                      alpha=0.5, c=np.arange(5), cmap='viridis', 
                      edgecolors='black', linewidth=1)
for i, country in enumerate(df2['Country']):
    plt.text(df2['GDP'][i], df2['Population'][i], country, fontsize=12, ha='right')

plt.xlabel('GDP (in billions)')
plt.ylabel('Population (in millions)')
plt.title('Bubble Chart: Population vs GDP')
plt.colorbar(scatter, label='Index of Country')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()