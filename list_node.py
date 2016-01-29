class SausageLinkNode:

  food_category  = 'meat_snack'     #class variable shared by all instances of SausageLinkNode

  def __init__(self, sausage_filling, prev_sausage_node, next_sausage_node):
     #note that instance variables are defined as well as assigned in the constructor
     self.filling = sausage_filling
     self.prev_node = prev_sausage_node
     self.next_node = next_sausage_node


  def is_first_node(self):
    self.prev_node == self 

  def is_last_node(self):
     self.next_node == self 

  def set_next_node(self, new_next):
     self.next_node = new_next 
  

  def set_prev_node(self, new_prev):
     self.prev_node = new_prev


  def contains_a_specific_filling(self, filling_to_check_for):
    return filling_to_check_for == self.filling


   

#there are no "end" keywords to put ends on your blocks, so if you are like
#me, you will probably want to use comments to show ends of blocks.

#everything works by indentation. Get used to using really good form....

  


  #here's how we do initialization of classes in Python:
  #The sausage can be filled with a value of arbitrary type, but we will eventually
  #restrict the filling to meats. 
   
 
