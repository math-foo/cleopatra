#!/usr/bin/python

import unittest
from organism_parsing import *

# given A, b -> [AB, Ab, aB, ab]
def generate_genetic_pairs(a, b):
   if a > b:
     return generate_genetic_pairs(b,a)
   values = []
   values.append(a.upper()+b.upper())
   values.append(a.upper()+b.lower())
   values.append(b.upper()+a.lower())
   values.append(a.lower()+b.lower())
   return values

class TestSimpleOrganismTree(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    test_input = ['A, B -> C\n', # Two Parent organism
                  'D\n', # Lone organism
                  'E -> F\n'] # Single Parent organisms
    organism_parser = OrganismParser(test_input)
    self.organism_tree = organism_parser.produce_organisms()

  def test_ghost_organisms_generated(self):
    self.assertEqual(1, len(self.organism_tree.ghosts))
    self.assertEqual('F', self.organism_tree.ghosts['F#Ghost']['child'])

  def test_organisms_generate(self):
    self.assertItemsEqual(['A', 'B', 'C', 'D', 'E', 'F'],
                          self.organism_tree.organisms.keys())

  def test_isolated_organism(self):
    organism = self.organism_tree.organisms['D']
    genes = [gene_entry.gene for gene_entry in organism.genes]
    value = genes[0]
    filtered_genes = filter(lambda x: x != value, genes)
    self.assertEqual([], filtered_genes)

  def test_one_parent_organism(self):
    organism = self.organism_tree.organisms['F']
    genes = [gene_entry.gene for gene_entry in organism.genes]
    value_a = self.organism_tree.organisms['E'].genes[0].gene[0].lower()
    values = genes[0].lower()
    self.assertIn(value_a, values)
    value_b = values[1] if value_a == values[0] else values[0]
    values = generate_genetic_pairs(value_a, value_b)
    filtered_genes = filter(lambda x: x not in values, genes)
    self.assertEqual([], filtered_genes)

  def test_two_parent_organism(self):
    organism = self.organism_tree.organisms['C']
    genes = [gene_entry.gene for gene_entry in organism.genes]
    value_a = self.organism_tree.organisms['A'].genes[0].gene[0].lower()
    value_b = self.organism_tree.organisms['B'].genes[0].gene[0].lower()
    values = generate_genetic_pairs(value_a, value_b)
    filtered_genes = filter(lambda x: x not in values, genes)
    self.assertEqual([], filtered_genes)


class TestOrganismTreeSummary(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    test_input = ['A, B -> C\n', # Two Parent organism
                  'D\n', # Lone organism
                  'E -> F\n'] # Single Parent organisms
    organism_parser = OrganismParser(test_input)
    self.organism_tree = organism_parser.produce_organisms()
    self.summary = self.organism_tree.generate_summary()

  def test_no_parent_organisms_described(self):
    no_parents = ['A','B', 'D', 'E']
    for name in no_parents:
      desc = "{0} has no parents".format(name)
      index = self.summary.find(desc)
      self.assertGreater(index, -1)

  def test_one_parent_organisms_described(self):
    desc = "F is a child of E"
    index = self.summary.find(desc)
    self.assertGreater(index, -1)

  def test_two_parent_organisms_described(self):
    desc = "C is a child of A and B"
    index = self.summary.find(desc)
    self.assertGreater(index, -1)

  def test_parent_before_child(self):
    C_desc = "C is a child of A and B"
    C_index = self.summary.find(C_desc)
    A_desc = "A has no parents"
    A_index = self.summary.find(A_desc)
    self.assertGreater(C_index, A_index)


if __name__ == '__main__':
    unittest.main()
