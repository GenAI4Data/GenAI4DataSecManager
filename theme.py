from contextlib import contextmanager
from menu import menu
from nicegui import ui

@contextmanager
def frame(navtitle: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    ui.colors(primary='#4285F4', secondary='#AECBFA', accent='#1967D2', positive='#34A853', negative='#EA4335')

    # with ui.layout() as layout:  # Use ui.layout as the top-level container

    with ui.header(elevated=True).classes(replace='row items-center').classes('bg-blue-500') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.label('GenAI4Data - Security Manager').classes('font-bold text-white') #Added text-white

    with ui.left_drawer().classes('bg-white') as left_drawer:  # Removed 'white' - use bg-white
            menu()  # menu() should create its own ui elements.

    with ui.footer().classes('bg-blue-500 w-full') as footer:
        ui.label('Copyright 2024 CCW Latam - Concept Prototype').classes('font-bold text-white')

    with ui.column().classes('w-full p-4'):  # Main content area.  Removed absolute positioning
        yield  # Your stepper and other content will go HERE