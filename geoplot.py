from bokeh.io import curdoc
from pyproj import Proj, transform
import pandas as pd
import datetime as dt
from bokeh.models import Panel, DatePicker, Select, ColumnDataSource, ColorBar
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
from bokeh.layouts import widgetbox, row
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, WIKIMEDIA, CARTODBPOSITRON, STAMEN_TERRAIN, STAMEN_TONER, ESRI_IMAGERY, OSM

import warnings

def geoplot():
    data = pd.read_csv('./dataset/data_covid-19_indonesia.csv')
    data.set_index('Date', inplace=True)

    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')

    ind_lon1, ind_lat1 = transform(outProj,inProj,90,-15)
    ind_lon2, ind_lat2 = transform(outProj,inProj,150,20)
    cartodb = get_provider(CARTODBPOSITRON)

    df = data[data.index == '2020-03-01']

    nam = []
    for i in df.new_cases:
        nam.append("new_cases")

    source = ColumnDataSource(data={
        'x'         : df.MercatorX,
        'y'         : df.MercatorY,
        'dat'       : df.new_cases,
        'nama'      : nam,
        'province' : df.Province
    })

    mapper = linear_cmap('dat', Spectral6 , 0 , 849875)


    p = figure(plot_width=900, plot_height=700,
            x_range=(ind_lon1, ind_lon2), y_range=(ind_lat1, ind_lat2),
            x_axis_type="mercator", y_axis_type="mercator",
            tooltips=[
                        ("Data", "@nama"), ("Jumlah", "@dat"), ("Province", "@province")
                        ],
            title="Covid in Indonesia")

    p.add_tile(cartodb)

    p.circle(x='x', y='y',
            size=10,
            line_color=mapper, color=mapper,
            fill_alpha=1.0,
            source=source)

    color_bar = ColorBar(color_mapper=mapper['transform'], width=8)

    p.add_layout(color_bar, 'right')

    def update_plot(attr, old, new):
        df = data[data.index == str(dPicker.value)]
        nam = []
        for i in df.new_cases:
            nam.append(str(data_select.value))
        source.data = {
            'x'         : df.MercatorX,
            'y'         : df.MercatorY,
            'dat'       : df[data_select.value],
            'nama'      : nam,
            'province' : df.Province
        }

    dPicker = DatePicker(
        title = 'Date',
        value=dt.datetime(2020, 3, 1).date(),
        min_date= dt.datetime(2020, 3, 1).date(), max_date=dt.datetime(2021, 12, 3).date()
    )

    dPicker.on_change('value', update_plot)

    data_select = Select(
        options=['new_cases', 'new_deaths',	'new_recovered', 'new_activeCases', 'total_cases', 'total_deaths', 'total_recovered', 'total_activeCases'],
        value='new_cases',
        title='x-axis data'
    )

    data_select.on_change('value', update_plot)

    layout = row(widgetbox(dPicker, data_select), p)
    tab = Panel(child=layout, title = 'Covid 19 Case Number Geoplot')

    return tab
