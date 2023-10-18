import anvil.server
from anvil.js import get_dom_node

def set_test_id(component, test_id):
    get_dom_node(component).setAttribute("data-testid", test_id)