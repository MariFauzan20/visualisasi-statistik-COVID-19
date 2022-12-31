import pandas as pd

import bokeh
from bokeh.io import curdoc, show, save, output_file
from bokeh.models import Tabs

from os.path import dirname, join

from lineplot import lineplot_tab
from table import table_tab
from geoplot import geoplot


# Read dataset from file
covid_data_line = pd.read_csv("./dataset/covid_19_indonesia_time_series_all.csv")
covid_data_table = pd.read_csv("./dataset/covid_19_indonesia_time_series_all.csv")

# Preprocessing
covid_data.columns = covid_data.columns.str.replace(" ", "_")
covid_data.columns= covid_data.columns.str.lower()
covid_data['date'] = pd.to_datetime(covid_data['date'], format='%m/%d/%Y')
tab1 = lineplot_tab(covid_data)

# covid_data.groupby("date").count()

tab2 = table_tab(covid_data)
tab3 = geoplot()
# tabs = Tabs(tabs = [tab1, tab2])
tabs = Tabs(tabs = [tab1, tab2, tab3])

curdoc().add_root(tabs)