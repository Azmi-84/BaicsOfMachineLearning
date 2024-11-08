import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import BoxAnnotation, Div, RangeSlider, Spinner
from bokeh.layouts import gridplot, column
from bokeh.io import curdoc
from bokeh.themes import Theme

# Apply a material-like theme
curdoc().theme = Theme(json={
    "attrs": {
        "Figure": {
            "background_fill_color": "#FAFAFA",
            "border_fill_color": "#FFFFFF",
            "outline_line_color": "#E0E0E0"
        },
        "Axis": {
            "major_label_text_color": "#424242",
            "axis_label_text_color": "#424242",
            "major_tick_line_color": "#BDBDBD",
            "minor_tick_line_color": "#EEEEEE",
            "axis_line_color": "#BDBDBD"
        },
        "Grid": {
            "grid_line_color": "#E0E0E0"
        },
        "Legend": {
            "background_fill_color": "#F5F5F5",
            "label_text_color": "#424242",
            "border_line_color": "#BDBDBD"
        }
    }
})

# Define x values and random y values for bar chart data
np.random.seed(42)
x = np.arange(1, 6)
y1 = np.random.randint(1, 10, size=5)
y2 = np.random.randint(1, 10, size=5)
y3 = np.random.randint(1, 10, size=5)
y4 = np.random.randint(1, 10, size=5)

# Create the bar chart figure
p1 = figure(
    title="Data Series with Highlighted Ranges",
    x_axis_label="X-Axis",
    y_axis_label="Y-Axis",
    width=800,
    height=600,
    x_range=(0, 6),
    y_range=(0, 15)
)

# Plotting the bar chart with random data series
p1.vbar(x, width=0.2, bottom=0, top=y1, legend_label="Series 1", color="#1976D2", alpha=0.8)
p1.vbar([i + 0.25 for i in x], width=0.2, bottom=0, top=y2, legend_label="Series 2", color="#D32F2F", alpha=0.8)
p1.vbar([i + 0.5 for i in x], width=0.2, bottom=0, top=y3, legend_label="Series 3", color="#388E3C", alpha=0.8)
p1.vbar([i + 0.75 for i in x], width=0.2, bottom=0, top=y4, legend_label="Series 4", color="#FBC02D", alpha=0.8)

# Adding BoxAnnotations to the bar chart
low_box = BoxAnnotation(bottom=0, top=5, fill_color="#BBDEFB", fill_alpha=0.3)
mid_box = BoxAnnotation(bottom=5, top=10, fill_color="#FFCDD2", fill_alpha=0.3)
high_box = BoxAnnotation(bottom=10, top=15, fill_color="#C8E6C9", fill_alpha=0.3)
p1.add_layout(low_box)
p1.add_layout(mid_box)
p1.add_layout(high_box)

# Customize legend appearance
p1.legend.title = "Data Series"
p1.legend.location = "top_left"

# Define additional data for mathematical functions
y_x = x
y_x2 = x ** 2
y_x3 = x ** 3
y_exp = np.exp(x)
y_log = np.log(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the mathematical functions figure
p2 = figure(
    title="Mathematical Functions",
    x_axis_label="X-Axis",
    y_axis_label="Y-Axis",
    width=800,
    height=600,
    x_range=(1, 5)
)

# Plotting mathematical functions in the new figure
p2.line(x, y_x, line_width=2, legend_label="y = x", color="#5C6BC0")
p2.line(x, y_x2, line_width=2, legend_label="y = x^2", color="#42A5F5")
p2.line(x, y_x3, line_width=2, legend_label="y = x^3", color="#FF7043")
p2.line(x, y_exp, line_width=2, legend_label="y = e^x", color="#66BB6A")
p2.line(x, y_log, line_width=2, legend_label="y = log(x)", color="#FFA726")
p2.line(x, y_sin, line_width=2, legend_label="y = sin(x)", color="#AB47BC")
p2.line(x, y_cos, line_width=2, legend_label="y = cos(x)", color="#26A69A")

# Customize legend appearance
p2.legend.title = "Mathematical Curves"
p2.legend.location = "top_left"

# Widgets for interactivity
description = Div(text="<h3>Interactive Data Visualization</h3><p>Use the range slider and spinner to adjust plot ranges.</p>")
range_slider = RangeSlider(start=0, end=15, value=(0, 15), step=1, title="Y-Axis Range")
spinner = Spinner(low=0, high=10, step=1, value=5, title="Bar Width")

# Update function for widgets
def update(attr, old, new):
    p1.y_range.start = range_slider.value[0]
    p1.y_range.end = range_slider.value[1]
    p2.y_range.start = range_slider.value[0]
    p2.y_range.end = range_slider.value[1]
    for r in p1.renderers:
        if hasattr(r, 'glyph') and hasattr(r.glyph, 'width'):
            r.glyph.width = spinner.value

# Add event listeners
range_slider.on_change("value", update)
spinner.on_change("value", update)

# Arrange plots and widgets
layout = column(description, range_slider, spinner, gridplot([[p1, p2]]))

# Display the layout
show(layout)
