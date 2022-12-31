import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable

def table_tab(data):
    source = ColumnDataSource(data)

    columns = [
        TableColumn(field='Date', title='Date'),
        TableColumn(field='New Cases', title='New Cases'),
        TableColumn(field='Total Cases', title='Total Cases'),
        TableColumn(field='Location', title='Location'),
        ]
    
    table = DataTable(source=source, columns=columns, width = 1000)
    tab = Panel(child = table, title = 'Covid 19 Cases Number Table')
    
    return tab