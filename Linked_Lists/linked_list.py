"""
Basic Node class with getters and setters.
"""
class Node:
  """
  Node class constructor, accepting value and link_node.
  """
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
  
  """
  Value getter.
  """
  def get_value(self):
    return self.value

  """
  Value setter.
  """
  def set_value(self, value):
    self.value = value
  
  """
  Link node getter.
  """
  def get_next_node(self):
    return self.next_node
  
  """
  Link node setter.
  """
  def set_next_node(self, next_node):
    self.next_node = next_node

"""
Basic Linked List class.
"""
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  """
  Head node getter.
  """
  def get_head_node(self):
    return self.head_node
  
  """
  Insert node at the head of the list.
  """
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  """
  Return a string containing all node values in insertion order.
  """
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  """
  Removes the node containing the first instance of the given value.
  """
  def remove_node_containing_value(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  """
  Removes the node passed into the function.
  """
  def remove_node(self, node_to_remove):
    current_node = self.get_head_node()
    if current_node == node_to_remove:
        self.head_node = current_node.get_next_node()
    else:
        while current_node:
            next_node = current_node.get_next_node()
            if next_node == node_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                current_node = None
            else:
                current_node = next_node