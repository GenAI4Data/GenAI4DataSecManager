from nicegui import ui

with ui.button('Open menu', icon='menu'):
    with ui.menu():
        ui.menu_item('Option 1')
        ui.menu_item('Option 2')
        with ui.menu_item('Option 3', auto_close=False):
            with ui.item_section().props('side'):
                ui.icon('keyboard_arrow_right')
            with ui.menu().props('anchor="top end" self="top start" auto-close'):
                ui.menu_item('Sub-option 1')
                ui.menu_item('Sub-option 2')
                ui.menu_item('Sub-option 3')

ui.run()