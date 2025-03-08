
from nicegui import ui

def menu() -> None:
    # ui.button('Home', icon='home', on_click=lambda: ui.navigate.to('/')).props('align=left').style('width:250px')
    # ui.button('Create Row Level Policy', icon='policy', on_click=lambda: ui.navigate.to('/createrls/')).props('align=left').style('width:250px')
    # ui.button('Assign Filters to Policy', icon='filter_alt', on_click=lambda: ui.navigate.to('/assignfilters/')).props('align=left').style('width:250px')
    # ui.button('Audit Logs', icon='gavel', on_click=lambda: ui.navigate.to('/reports/')).props('align=left').style('width:250px')

    with ui.list():#.props('dense separator'):
        with ui.item(on_click=lambda: ui.navigate.to('/')):
            with ui.item_section().props('avatar'):
                ui.icon('home', color='blue-500')
            with ui.item_section():
                ui.item_label('Home').classes(replace = 'text-primary text-bold').style('font-size:16px')
        with ui.expansion('Row Level Security', caption='Click to Expand', icon='policy').classes('w-full text-primary text-bold').style('font-size:16px'):
            with ui.item(on_click=lambda: ui.navigate.to('/createrlsusers/')):
                with ui.item_section().props('avatar'):
                    ui.icon('person', color='blue-500')
                with ui.item_section():
                    ui.item_label('Create RLS for Users').classes(replace = 'text-primary text-bold').style('font-size:14px')
            with ui.item(on_click=lambda: ui.navigate.to('/createrlsgroups/')):
                with ui.item_section().props('avatar'):
                    ui.icon('groups', color='blue-500')
                with ui.item_section():
                    ui.item_label('Create RLS for Groups').classes(replace = 'text-primary text-bold').style('font-size:14px')
            with ui.item(on_click=lambda: ui.navigate.to('/assignuserstopolicy/')):
                with ui.item_section().props('avatar'):
                    ui.icon('assignment_ind', color='blue-500')
                with ui.item_section():
                    ui.item_label('Assign Users to Policy').classes(replace = 'text-primary text-bold').style('font-size:14px')
            with ui.item(on_click=lambda: ui.navigate.to('/')):
                with ui.item_section().props('avatar'):
                    ui.icon('assignment', color='blue-500')
                with ui.item_section():
                    ui.item_label('Assign Values to Groups').classes(replace = 'text-primary text-bold').style('font-size:14px')
        with ui.item(on_click=lambda: ui.navigate.to('/')):
            with ui.item_section().props('avatar'):
                ui.icon('gavel', color='blue-500')
            with ui.item_section():
                ui.item_label('Audit Logs').classes(replace = 'text-primary text-bold').style('font-size:16px')
                ui.item_label('Coming Soon!').props('caption')