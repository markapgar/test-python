from ._anvil_designer import StartupFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..TestHooks import set_test_id



class StartupForm(StartupFormTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)
    set_test_id(self.login_button, 'show_login')


    # Any code you write here will run before the form opens.

  def login_button_click(self, **event_args):
    anvil.users.login_with_form()

    if anvil.users.get_user() is not None:
      open_form('MainForm')
    else:
      alert('Login failed')
    pass

