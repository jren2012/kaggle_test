import plotly as py
import plotly.graph_objs as go

# Add data
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

loss = ['0.9870', '0.9658', '0.9512', '0.9356', '0.9198', '0.9057', '0.8927', '0.8818', '0.8667', '0.8550', '0.8442', '0.8326']
acc = ['0.9839', '0.9882', '0.9907', '0.9920', '0.9934', '0.9945', '0.9950', '0.9952', '0.9962', '0.9958', '0.9967', '0.9971']
val_loss = ['7.9559', '9.3613', '7.6987', '8.5847', '9.0178', '8.2430', '8.7687', '7.6371', '7.2045', '7.0197', '5.9465', '6.3140']
val_acc = ['0.1106', '0.1151', '0.1154', '0.1112', '0.1187', '0.0944', '0.0995', '0.0907', '0.0892', '0.1178', '0.0868', '0.0965']

# Create and style traces
trace0 = go.Scatter(
    x = month,
    y = loss,
    name = 'loss',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1 = go.Scatter(
    x = month,
    y = acc,
    name = 'acc',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace2 = go.Scatter(
    x = month,
    y = val_loss,
    name = 'val_loss',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x = month,
    y = val_acc,
    name = 'val_acc',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)

data = [trace0, trace1, trace2, trace3]

# Edit the layout
layout = dict(title = 'Average High and Low Temperatures in New York',
              xaxis = dict(title = 'Month'),
              yaxis = dict(title = 'Temperature (degrees F)'),
              )

fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename='styled-line.html')
