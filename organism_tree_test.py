#!/usr/bin/python

import unittest
from organism_parsing import *

class TestSimpleOrganismTree(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    test_input = ['A, B -> C\n', # Two Parent organism
                  'D\n', # Lone organism
                  'E -> F\n'] # Single Parent organisms
    organism_parser = OrganismParser(test_input)
    self.organism_tree = organism_parser.produce_organisms()
    self.organism_tree.generate_summary()

  def test_ghost_organisms_generated(self):
    self.assertTrue(False)

  def test_origin_organisms_list(self):
    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
