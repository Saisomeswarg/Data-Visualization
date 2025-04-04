import matplotlib.pyplot as plt
import numpy as np
# 1. . Create a scatter plot using Matplotlib to visualize the relationship between two arrays, x and y for the given data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]
plt.scatter(x, y, color = 'blue', marker = 'o')
plt.title('Scatter Plot of x vs y')
plt.xlabel('X values')
plt.ylabel('y Values')
plt.grid(True)
plt.show()

# 2. Generate a line plot to visualize the trend of values for the given data.
data = np.array([3, 7, 9, 15, 22, 29, 35])
x1 = np.arange(len(data))

plt.plot(x1, data, color = 'green', marker = 'o')
plt.title('Line Plot of Data')
plt.xlabel('Index')
plt.ylabel('Values')
plt.grid(True)
plt.show()

# 3. Display a bar chart to represent the frequency of each item in the given array categories
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]

plt.bar(categories, values, color = 'orange')
plt.title('Bar Chart of Categories')
plt.xlabel('Categories')
plt.ylabel('Frequency') 
plt.show()

# 4.Create a histogram to visualize the distribution of values in the array data.
data1 = np.random.normal(0, 1, 1000)
plt.hist(data1, bins = 30, color = 'purple', alpha = 0.7)
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 5. how a pie chart to represent the percentage distribution of different sections in the array `sections`.
sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]
plt.pie(sizes, labeldistance=1.1, labels = sections, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.axis('equal')  
plt.title('Pie Chart of Sections')
plt.show()
