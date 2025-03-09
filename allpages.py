from nicegui import ui
from pages.create_rls_users import RLSCreateforUsers
from pages.create_rls_groups import RLSCreateforGroups
from pages.assign_users_to_policy import RLSAssignUserstoPolicy
from pages.assign_values_to_group import RLSAssignValuestoGroup

def create() -> None:
    def create_rls_page_for_users():
        rls_instance = RLSCreateforUsers()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/createrlsusers/')(create_rls_page_for_users)  # Pass the function to ui.page

    def create_rls_page_for_groups():
        rls_instance = RLSCreateforGroups()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/createrlsgroups/')(create_rls_page_for_groups)  # Pass the function to ui.page

    def assign_users_to_policy():
        rls_instance = RLSAssignUserstoPolicy()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/assignuserstopolicy/')(assign_users_to_policy) 

    def assign_values_to_group():
        rls_instance = RLSAssignValuestoGroup()  # Create an INSTANCE of RLSCreate
        rls_instance.run()          # Call the run method on the INSTANCE
    ui.page('/assignvaluestogroup/')(assign_values_to_group) 

if __name__ == '__main__':
    create()
