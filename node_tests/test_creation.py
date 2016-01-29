#These are the tests that you should use.


#the three lines that follow were unscrupuously plagarized from stackoverflow:
#see the answer posted on 6.28/09 from 
# http://stackoverflow.com/questions/1054271/how-to-import-a-python-class-that-is-in-a-directory-above
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import unittest
from list_node import SausageLinkNode

class TestSausageLinkNodeMethods(unittest.TestCase):
  
  def test_create_node(self):
    n = SausageLinkNode("meat", None, None)
    self.assertEqual(n.next_node, None)
    self.assertEqual(n.prev_node, None)


  def test_set_next_node(self):
    n = SausageLinkNode("emu", None, None)
    o = SausageLinkNode("pork", None, None)

    n.set_next_node(o)
    self.assertEqual(n.next_node, o)

  def test_set_prev_node(self):
    n = SausageLinkNode("emu", None, None)
    o = SausageLinkNode("pork", None, None)
    n.set_prev_node(o)
    self.assertEqual(n.prev_node, o)
 

  def test_print_something_simple(self):
    self.assertEqual (True, True)
    print "fuck you!"



print "Beginning procedure..."



if __name__ == '__main__':
    unittest.main()


#tslnm = TestSausageLinkNodeMethods()
#tslnm.test_print_something_simple
print "completed the call..."
