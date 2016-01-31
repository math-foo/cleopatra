#!/usr/bin/python

import unittest
from organism_generation import *

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

class TestOrganismGenerator(unittest.TestCase):
  @classmethod
  def setUpClass(self):
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
    organism = self.organisms.organism_dict['C']
    genes = [gene_entry.gene for gene_entry in organism.genes]
    value_a = self.organisms.organism_dict['A'].genes[0].gene[0].lower()
    values = genes[0].lower()
    self.assertIn(value_a, values)
    value_b = values[1] if value_a == values[0] else values[0]
    values = generate_genetic_pairs(value_a, value_b)
    filtered_genes = filter(lambda x: x not in values, genes)
    self.assertEqual([], filtered_genes)

  def test_two_parent_organism(self):
    organism = self.organisms.organism_dict['D']
    genes = [gene_entry.gene for gene_entry in organism.genes]
    value_a = self.organisms.organism_dict['A'].genes[0].gene[0].lower()
    value_b = self.organisms.organism_dict['B'].genes[0].gene[0].lower()
    values = generate_genetic_pairs(value_a, value_b)
    filtered_genes = filter(lambda x: x not in values, genes)
    self.assertEqual([], filtered_genes)

if __name__ == '__main__':
    unittest.main()
