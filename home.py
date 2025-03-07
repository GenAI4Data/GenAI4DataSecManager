from nicegui import ui

def content() -> None:
# Use a container for the entire page content to manage overall centering and max-width.
    with ui.row().classes('w-full justify-center'):
        with ui.column().classes('w-full max-w-5xl items-center'):  # Responsive width, centered content

            ui.label('Welcome to GenAI4Data Security Manager').classes('text-4xl font-bold text-center my-4 text-primary') # Larger title, spacing, color
            ui.label('A tool to simplify Row-Level Security (RLS) creation in BigQuery.').classes('text-xl text-center text-bold text-gray-700 mb-8') # Subtitle, color, spacing

            with ui.card().classes('mt-8 p-6 rounded-lg shadow-xl w-full md:w-3/4 lg:w-2/3'):  # Responsive card width, rounded corners, better shadow
                ui.label('Key Features').classes('text-2xl font-semibold mb-6 text-center')  # Centered title

                with ui.grid(columns=3).classes('gap-8 w-full justify-center'):  # Use ui.grid for responsive columns
                    with ui.column().classes('items-center text-center'): # Center column content
                        ui.icon('shield', size='3em', color='#3b82f6')  # Nice blue color (Tailwind's blue-500)
                        ui.label('Enhanced Security').classes('text-lg font-medium mt-2') # Spacing
                        ui.label('Easily define row-level access control.').classes('text-sm text-gray-600 px-4') # Added padding for better readability

                    with ui.column().classes('items-center text-center'):
                        ui.icon('speed', size='3em', color='#3b82f6')
                        ui.label('Streamlined Workflow').classes('text-lg font-medium mt-2')
                        ui.label('Intuitive interface for quick RLS setup.').classes('text-sm text-gray-600 px-4')

                    with ui.column().classes('items-center text-center'):
                        ui.icon('link', size='3em', color='#3b82f6')
                        ui.label('BigQuery Integration').classes('text-lg font-medium mt-2')
                        ui.label('Seamlessly connects with your BigQuery datasets.').classes('text-sm text-gray-600 px-4')
