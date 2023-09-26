from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..TestHooks import set_test_id

class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    set_test_id(self.user_label, 'user_label')
    
  def form_show(self, **event_args):
    user = anvil.users.get_user()
    
    self.user_label.text = anvil.users.get_user()['email']

