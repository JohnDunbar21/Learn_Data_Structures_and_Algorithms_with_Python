"""
Basic Node class with getters and setters.
"""
class Node:
  """
  Node class constructor, accepting value and link_node.
  """
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  """
  Link node setter.
  """
  def set_link_node(self, link_node):
    self.link_node = link_node

  """
  Value setter.
  """
  def set_value(self, value):
    self.value = value
  
  """
  Link node getter.
  """
  def get_link_node(self):
    return self.link_node
  
  """
  Value getter.
  """
  def get_value(self):
    return self.value