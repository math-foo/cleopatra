#!/usr/bin/python

import unittest
from organism_generation import *

class TestOrganismGenerator(unittest.TestCase):
  def setUp(self):
    relationships = {'A' : [], 'B': [], 'C': ['A'], 'D' : ['A', 'B']}
    self.organisms = OrganismGenerator(relationships)
    self.organisms.generate_organisms()

  def test_isolated_organism(self):
    organism = self.organisms.organism_dict['A']
    genes = [gene_entry.gene for gene_entry in organism.genes]
    value = genes[0]
    filtered_genes = filter(lambda x: x != value, genes)
    self.assertEqual([], filtered_genes)

  def test_one_parent_organism(self):
    self.assertTrue(False)

  def test_two_parent_organism(self):
    self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
