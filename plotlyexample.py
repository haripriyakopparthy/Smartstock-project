# Import required libraries
import plotly.graph_objects as go

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 170, 220, 180, 240]

# Create a line chart
fig = go.Figure()

# Add line trace
fig.add_trace(go.Scatter(
    x=months,
    y=sales,
    mode='lines+markers',  # Lines with markers
    name='Sales',
    line=dict(color='blue', width=2),
    marker=dict(size=8)
))

# Customize layout
fig.update_layout(
    title='Monthly Sales Trend',
    xaxis_title='Month',
    yaxis_title='Sales',
    template='plotly_dark'
)

# Show plot
fig.show()