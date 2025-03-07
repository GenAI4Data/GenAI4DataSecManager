
from nicegui import ui

def menu() -> None:
    ui.button('Home', icon='home', on_click=lambda: ui.navigate.to('/')).props('align=left').style('width:250px')
    ui.button('Create Row Level Policy', icon='policy', on_click=lambda: ui.navigate.to('/createrls/')).props('align=left').style('width:250px')
    ui.button('Assign Filters to Policy', icon='filter_alt', on_click=lambda: ui.navigate.to('/assignfilters/')).props('align=left').style('width:250px')
    ui.button('Audit Logs', icon='gavel', on_click=lambda: ui.navigate.to('/reports/')).props('align=left').style('width:250px')
    