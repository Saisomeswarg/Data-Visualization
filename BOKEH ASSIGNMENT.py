import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar
from bokeh.transform import transform
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral4
from bokeh.palettes import Viridis256

#1. Create a Bokeh plot displaying a sine wave. Set x-values from 0 to 10 and y-values as the sine of x.
x = np.linspace(0, 10, 100)
y = np.sin(x)

output_file("sine_wave.html")

p = figure(title="Sine Wave", x_axis_label='X', y_axis_label='sin(X)', 
           width=700, height=400)
p.line(x, y, legend_label="sin(x)", line_width=2, color="blue")
show(p)

#2.Create a Bokeh scatter plot using randomly generated x and y values. Use different sizes and colors for the markers based on the 'sizes' and 'colors' columns.
np.random.seed(30)
num_points = 100
x = np.random.uniform(0, 10, num_points)
y = np.random.uniform(0, 10, num_points)

sizes = np.random.randint(10, 50, num_points)
colors = np.random.choice(['red', 'green', 'blue', 'orange'], num_points)

df = pd.DataFrame({'X' : x, 'Y' : y, 'sizes' : sizes, 'colors' : colors})
source = ColumnDataSource(df)
output_file("scatter_plot.html")

p1 = figure(title = "Bokeh Scatter Plot", x_axis_label = 'X', y_axis_label = 'Y', width = 700, height = 400)
p1.scatter('X', 'Y', size = 'sizes', color = 'colors', source = source, alpha = 0.6)

show(p1)

#3. Generate a Bokeh bar chart representing the counts of different fruits using the following dataset.
fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))
output_file("bar_chart.html") 

p2 = figure(x_range=fruits, title="Fruit Counts", 
            x_axis_label="Fruits Type", y_axis_label="Count", 
            width=700, height=400)
p2.vbar(x='fruits', top='counts', width=0.6, source=source,
     fill_color=factor_cmap('fruits', palette=Spectral4, factors=fruits))
show(p2)

#4.Create a Bokeh histogram to visualize the distribution of the given data.
np.random.seed(40)
data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)

source = ColumnDataSource(data = dict(hist = hist, edges = edges[:-1], right = edges [1:]))
output_file("histogram.html")

p3 = figure(title="Histogram", x_axis_label='Value', y_axis_label='Frequency', width=700, height=400)
p3.quad(top='hist', bottom=0, left='edges', right='right', source=source, fill_color="navy", line_color="white", alpha=0.5)
show(p3)

#5.. Create a Bokeh heatmap using the provided dataset.
np.random.seed(42)  
data_heatmap = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)


df = pd.DataFrame({'x': xx.flatten(), 'y': yy.flatten(), 'value': data_heatmap.flatten()})
output_file("heatmap.html")

color_mapper = LinearColorMapper(palette=Viridis256, low=df["value"].min(), high=df["value"].max())


p4 = figure(title="Bokeh Heatmap", x_axis_label="X", y_axis_label="Y",
            width=700, height=400, x_range=(0, 1), y_range=(0, 1))
p4.rect(x="x", y="y", width=0.1, height=0.1, source=df, 
        fill_color=transform('value', color_mapper), line_color=None)
color_bar = ColorBar(color_mapper=color_mapper, location=(0, 0))
p4.add_layout(color_bar, 'right')
show(p4)
