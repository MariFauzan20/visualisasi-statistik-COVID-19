import pandas as pd

import bokeh
from bokeh.io import curdoc, show, save, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.models import Tabs

from os.path import dirname, join

from lineplot import lineplot_tab
from table import table_tab
from geoplot import geoplot


# Read dataset from file
covid_data_line = pd.read_csv("./dataset/covid_19_indonesia_time_series_all.csv")
covid_data_table = pd.read_csv("./dataset/covid_19_indonesia_time_series_all.csv")

# Preprocessing
covid_data_line['Date'] = pd.to_datetime(covid_data_line['Date'], format='%m/%d/%Y')
tab1 = lineplot_tab(covid_data_line)

tab2 = table_tab(covid_data_table)
tab3 = geoplot()
tabs = Tabs(tabs = [tab1, tab2, tab3])

# output_file("final_proj.html")
# save(tabs, "final_proj.html", title="Final")
curdoc().add_root(tabs)