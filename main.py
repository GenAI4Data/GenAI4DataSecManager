import home
import allpages
import theme
from nicegui import app, ui



# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
         home.content()

# this call shows that you can also move the whole page creation into a separate file

allpages.create()

ui.run(title='Getting Started with NiceGUI')
