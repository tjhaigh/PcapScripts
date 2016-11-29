import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

labels = []
values = []

with open("countries.txt", "r") as f:
    for line in f:
        line = line.strip()
        count = line[4:]
        country = line[:2]

        labels.append(country)
        values.append(int(count))
        
trace = go.Pie(labels=labels, values=values)

plot([trace])
