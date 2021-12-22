import pandas as pd
import plotly.figure_factory as ff
import csv


data_file = pd.read_csv("data.csv")
fig = ff.create_distplot([data_file["Avg Rating(Average)"].tolist()],["Avg Rating"], show_hist=True)
fig.show()