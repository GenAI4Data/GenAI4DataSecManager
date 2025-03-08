import theme
from config import  Config
from nicegui import ui
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from google.api_core.exceptions import GoogleAPIError

    
config = Config()

# Initialize BigQuery client globally, it's good
client = bigquery.Client(project=config.PROJECT_ID)


class RLSCreateforGroups:

    def __init__(self):
        self.project_id = config.PROJECT_ID
        self.table_list = None
        self.field_list = None

        self.page_title = "Create Row Level Policy - Groups"
        self.headers()

        self.stepper = ui.stepper().props("vertical").classes("w-full")

        self.step1_title = "Select Dataset"
        self.step2_title = "Select Table"
        self.step3_title = "Select Field"
        self.step4_title = "Enter the Group"
        self.step5_title = "Review and Run"

        # Initialize selected values properly
        self.selected_dataset = None
        self.selected_table = None
        self.selected_field = None
        self.group_assignment = None

    # Simplified update functions with early return
    def _update_selected_dataset(self, e):
        if not e.value:
            return  # Early exit if no value
        self.selected_dataset = e.value
        self.step1_next_button.set_visibility(True)  # Simplified visibility

    def _update_selected_table(self, e):
        self.selected_table = e.value
        self.step2_next_button.set_visibility(bool(e.value)) #show next button when table is selected

    def _update_selected_field(self, e):
        self.selected_field = e.value
        self.step3_next_button.set_visibility(bool(e.value))#show next button when field is selected

    def _update_group_assignment(self, e):
        self.group_assignment = e.value
        self.step4_next_button.set_visibility(bool(e.value))#show next button when field is selected

    def _step1_next_button_visibility(self):
         self.step1_next_button.set_visibility(bool(self.selected_dataset)) # simplified


    def headers(self):
        ui.page_title(self.page_title)
        ui.label('Create Row Level Security for Groups').classes('text-primary text-center text-bold') # Subtitle, color, spacing
        # ui.markdown(f"#{self.page_title}")  # Optional: Keep if you want a larger heading

    def get_datasets(self):
        try:
            datasets = list(client.list_datasets())
            return [dataset.dataset_id for dataset in datasets]
        except GoogleAPIError as e:
            ui.notify(f"Error fetching datasets: {e}", type="negative")
            return []  # Return empty list on error
        except Exception as e:
            ui.notify(f"An unexpected error occurred: {e}", type="negative")
            return []


    def get_tables_in_dataset(self):
        if not self.selected_dataset:
            ui.notify("Please select a dataset first.", type="warning")
            return

        try:
            tables = client.list_tables(self.selected_dataset)
            table_ids = [table.table_id for table in tables]
            self.table_list.options = table_ids
            self.table_list.value = None  # Clear previous selection, VERY IMPORTANT
            self.table_list.update()
            self.stepper.next()
            self.step2_next_button.set_visibility(False)#hide next button in step2
        except NotFound:
            ui.notify(f"Dataset not found: {self.selected_dataset}", type="negative")
        except GoogleAPIError as e:
            ui.notify(f"Error fetching tables: {e}", type="negative")
        except Exception as e:
            ui.notify(f"An unexpected error occurred: {e}", type="negative")



    def get_fields_in_table(self):
        if not self.selected_table:
            ui.notify("Please select a table first.", type="warning")
            return

        try:
            table_ref = client.dataset(self.selected_dataset).table(self.selected_table)
            table = client.get_table(table_ref)
            fields = [[schema_field.name, schema_field.field_type, schema_field.description] for schema_field in table.schema]
            self.field_list.options = fields
            self.field_list.value = None  # Clear previous selection, VERY IMPORTANT
            self.field_list.update()
            self.stepper.next()
            self.step3_next_button.set_visibility(False) #hide next button in step3
        except NotFound:
            ui.notify(f"Table not found: {self.selected_table}", type="negative")
        except GoogleAPIError as e:
            ui.notify(f"Error fetching fields: {e}", type="negative")
        except Exception as e:
            ui.notify(f"An unexpected error occurred: {e}", type="negative")

    def get_resume(self):
        if not self.selected_field:
            ui.notify("Please select a field first.", type="warning")
            return

        # Use f-strings for better readability
        self.resume.content = f""" 
            ###**The following Row Level Security Policy will be created:**<br>

            **Project ID**: {self.project_id}<br>
            **Dataset ID**: {self.selected_dataset}<br>
            **Table ID**: {self.selected_table}<br>
            **Field ID**: {self.selected_field[0]}<br>
            **Group Email**: {self.group_assignment}<br>
            <br>
            **Code**:

        """

        self.code.content = (
            f"CREATE OR REPLACE ROW ACCESS POLICY\n"
            f"  `{self.selected_dataset}_{self.selected_table}_{self.selected_field[0]}`\n"
            f"ON\n"
            f"  `{self.project_id}.{self.selected_dataset}.{self.selected_table}`\n"
            f"GRANT TO (\"group:{self.group_assignment}\")\n"  #Consider making the GRANT TO configurable
            f"FILTER USING ({self.selected_field[0]} IN\n"
            f"  (SELECT CAST(filter_value AS {self.selected_field[1]})\n"
            f"   FROM `{config.FILTER_TABLE}`\n"  #use config value
            f"   WHERE rls_type = 'group'\n"
            f"   AND policy_name = '{self.selected_dataset}_{self.selected_table}_{self.selected_field[0]}'\n"
            f"   AND project_id = '{self.project_id}'\n"
            f"   AND dataset_id = '{self.selected_dataset}'\n"
            f"   AND table_id = '{self.selected_table}'\n"
            f"   AND field_id = '{self.selected_field[0]}'\n"
            f"   AND username = SESSION_USER()));"
        )
        self.stepper.next()

    def run_creation_policy(self):
        try:
            query_job = client.query(self.code.content)
            query_job.result()  # Wait for the query to complete

            with ui.dialog() as dialog, ui.card():
                ui.label(f'Row Level Policy Created on {self.selected_table}.{self.selected_field[0]} successfully!').classes(replace = 'text-positive').classes('font-bold')
                with ui.row().classes('w-full justify-center'):  # Key change: Row and justification
                    ui.button('Close', on_click=ui.navigate.reload)  # or dialog.close
            dialog.open()

        except GoogleAPIError as error:
            ui.notify(f"Error creating row-level access policy: {error}", type="negative")
        except Exception as error:
            ui.notify(f"An unexpected error occurred: {error}", type="negative")

            

    def step1(self):
        with ui.step(self.step1_title):
            dataset_list = self.get_datasets()
            ui.select(dataset_list, label="Select Dataset", on_change=self._update_selected_dataset)
            with ui.stepper_navigation():
                self.step1_next_button = ui.button("NEXT", icon="arrow_forward_ios", on_click=self.get_tables_in_dataset)
                self.step1_next_button.set_visibility(False)

    def step2(self):
        with ui.step(self.step2_title):
            self.table_list = ui.select([], label="Select Table", on_change=self._update_selected_table)
            with ui.stepper_navigation():
                ui.button("BACK", icon="arrow_back_ios", on_click=self.stepper.previous)
                self.step2_next_button = ui.button("NEXT", icon="arrow_forward_ios", on_click=self.get_fields_in_table)
                # Initialize visibility to False; it will become visible when a table is selected.
                self.step2_next_button.set_visibility(False)
            return
        
    def step3(self):
        with ui.step(self.step3_title):
            self.field_list = ui.select([], label="Select Field", on_change=self._update_selected_field)
            with ui.stepper_navigation():
                ui.button("BACK", icon="arrow_back_ios", on_click=self.stepper.previous)
                self.step3_next_button = ui.button("NEXT", icon="arrow_forward_ios", on_click=self.stepper.next)
                # Initialize visibility to False.
                self.step3_next_button.set_visibility(False)
            return

    def step4(self):
        with ui.step(self.step4_title):
            self.group_assignment = ui.input(placeholder="Enter the group email", on_change=self._update_group_assignment)
            with ui.stepper_navigation():
                ui.button("BACK", icon="arrow_back_ios", on_click=self.stepper.previous)
                self.step4_next_button = ui.button("NEXT", icon="arrow_forward_ios", on_click=self.get_resume)
                # Initialize visibility to False.
                self.step4_next_button.set_visibility(False)
            return
        
    def step5(self):
        with ui.step(self.step5_title):
            self.resume = ui.markdown().classes(replace='text-primary')
            self.code = ui.code(content='', language="SQL")  # Consider highlighting
            with ui.stepper_navigation():
                ui.button("BACK", icon="arrow_back_ios", on_click=self.stepper.previous)
                ui.button("CREATE", icon="policy", on_click=self.run_creation_policy)
            return

    def run(self):
        with theme.frame('Create'):
            with self.stepper:
                self.step1()
                self.step2()
                self.step3()
                self.step4()
                self.step5()