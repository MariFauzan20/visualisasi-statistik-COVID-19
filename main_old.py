# from bokeh.io import curdoc, save, output_file, show
# from pyproj import Proj, transform
# import pandas as pd
# import datetime as dt
# from bokeh.models import DatePicker, Select, ColumnDataSource, ColorBar
# from bokeh.palettes import Spectral6
# from bokeh.transform import linear_cmap
# from bokeh.layouts import column, row
# from bokeh.plotting import figure
# # from bokeh.tile_providers import get_provider, WIKIMEDIA, CARTODBPOSITRON, STAMEN_TERRAIN, STAMEN_TONER, ESRI_IMAGERY, OSM
# df = pd.read_csv("./dataset/covid_19_indonesia_time_series_all.csv")

# df.columns = df.columns.str.replace(" ", "_")
# df.columns= df.columns.str.lower()
# df.set_index('date', inplace=True)

# df.head()

# #define beberapa variabel untuk membuat peta dengan cartodbpositron
# inProj = Proj(init='epsg:3857')
# outProj = Proj(init='epsg:4326')

# ind_lon1, ind_lat1 = transform(outProj,inProj,90,-15)
# ind_lon2, ind_lat2 = transform(outProj,inProj,150,20)
# # cartodb = get_provider(CARTODBPOSITRON)

# #define variabel 'df' dengan data pada tanggal 2020-03-01 
# data = df[df.index == '3/1/2020']

# #define variabel nam untuk menampung nama kolom yang di select
# nam = []
# for i in data.new_cases:
#     nam.append("new_cases")

# #source digunakan untuk menampilkan data yang akan ditampilkan (data awal)
# source = ColumnDataSource(data={
#     'x'         : df.latitude, #define x dengan kolom mercatorX dari data dengan index tanggal 2020-03-01
#     'y'         : df.longitude, #define y dengan kolom mercatorY dari data dengan index tanggal 2020-03-01
#     'dat'       : df.new_cases, #define dat dengan kolom new_cases dari data dengan index tanggal 2020-03-01
#     'nama'      : nam #define nama dengan nama kolom new_cases 
# })

# mapper = linear_cmap('dat', Spectral6 , 0 , 849875)

# #menampilkan peta pada visualisasi data
# p = figure(min_width=900, min_height=700,
#            x_range=(ind_lon1, ind_lon2), y_range=(ind_lat1, ind_lat2),
#            x_axis_type="mercator", y_axis_type="mercator",
#            tooltips=[
#                     ("Data", "@nama"), ("Jumlah", "@dat") #menampilkan data tiap kolom/data yang diselect
#                     ],
#            title="Covid in Indonesia 2023")

# # p.add_tile(cartodb)
# #plotting scatter plot (circle)
# p.circle(x='x', y='y',
#          size=10,
#          line_color=mapper, color=mapper,
#          fill_alpha=1.0,
#          source=source)
# #menampilkan color bar
# color_bar = ColorBar(color_mapper=mapper['transform'], width=8)

# p.add_layout(color_bar, 'right')

# def update_plot(attr, old, new):
#     data = df[df.index == str(dPicker.value)] #update 'df' dengan data dari index date yang di select oleh fitur datepicker
#     nam = []
#     for i in data.new_cases:
#         nam.append(str(data_select.value)) #update var nam
#     source.data = {
#         'x'         : data.MercatorX, #update x dengan kolom mercatorX dari data index date yang di select oleh fitur datepicker
#         'y'         : data.MercatorY, #define y dengan kolom mercatorY dari data index date yang di select oleh fitur datepicker
#         'dat'       : data[data_select.value], #update dat dengan kolom new_cases dari data kolom yang diselect pada fitur dropdwon select
#         'nama'      : nam #update nama dengan nama kolom sesuai dengan kolom yang diselect
#     }

#     #define fitur interaktif date picker
# dPicker = DatePicker(
#     title = 'Date',
#     value=dt.datetime(2020, 3, 1).date(), 
#     min_date= dt.datetime(2020, 3, 1).date(), max_date=dt.datetime(2021, 12, 3).date()
# )

# dPicker.on_change('value', update_plot)

# #define fitur interaktif dropdown dan select
# data_select = Select(
#     options=['new_cases', 'new_deaths',	'new_recovered', 'new_activeCases', 'total_cases', 'total_deaths',	'total_recovered', 'total_activeCases'],
#     value='new_cases',
#     title='x-axis data'
# )

# data_select.on_change('value', update_plot)

# #memasukan seluruh fitur interaktif dan juga plotingan kedalam layout
# layout = row(column(dPicker, data_select), p) 
# curdoc().add_root(layout)
# # show the results
# output_file("final_proj.html")
# save(p, "final_proj.html", title="Final")
# show(p)