#!/usr/bin/python

import unittest
from organism_parsing import *

class TestOrganismSimpleParsing(unittest.TestCase):
  def setUp(self):
    test_input = ['A, B -> C\n', # Two Parent organism
                  'D\n', # Lone organism
                  'E -> F\n', # Single Parent organisms
                  'G, H -> I\n', # Different parent pairs sharing a parent
                  'H, J -> K\n',
                  'L, M -> N\n', # Single parenting pair, multiple children
                  'L, M -> O\n',
                  'P -> Q\n', # Single Parent, multiple children
                  'P -> R\n']
    organism_parser = OrganismParser(test_input)
    self.organisms = organism_parser.produce_organisms()

  def test_lone_organism(self):
    self.assertIn('D', self.organisms)
    self.assertEqual([], self.organisms['D'])

  def test_single_parent_organism(self):
    self.assertIn('F', self.organisms)
    self.assertEqual(['E'], self.organisms['F'])

  def test_two_parent_organism(self):
    self.assertIn('C', self.organisms)
    self.assertEqual(['A', 'B'], self.organisms['C'])

  def test_different_parenting_pairs_organism(self):
    self.assertIn('I', self.organisms)
    self.assertIn('K', self.organisms)
    self.assertEqual(['G', 'H'], self.organisms['I'])
    self.assertEqual(['H', 'J'], self.organisms['K'])

  def test_two_parents_multiple_children_organism(self):
    self.assertIn('N', self.organisms)
    self.assertIn('O', self.organisms)
    self.assertEqual(['L', 'M'], self.organisms['N'])
    self.assertEqual(['L', 'M'], self.organisms['O'])

  def test_single_parent_multiple_children_organism(self):
    self.assertIn('Q', self.organisms)
    self.assertIn('R', self.organisms)
    self.assertEqual(['P'], self.organisms['Q'])
    self.assertEqual(['P'], self.organisms['R'])


class TestOrganismParsingOddSpacing(unittest.TestCase):
  def setUp(self):
    test_input = ['A,B->C\n', # Bunched
                  'D, E -> F\n', # Normal
                  '      G     ,     H      ->      I        \n'] # Spaced out
    organism_parser = OrganismParser(test_input)
    self.organisms = organism_parser.produce_organisms()

  def test_bunched_organisms(self):
    self.assertIn('C', self.organisms)
    self.assertEqual(['A', 'B'], self.organisms['C'])

  def test_normal_organisms(self):
    self.assertIn('F', self.organisms)
    self.assertEqual(['D', 'E'], self.organisms['F'])

  def test_spaced_out_organisms(self):
    self.assertIn('I', self.organisms)
    self.assertEqual(['G', 'H'], self.organisms['I'])


class TestOrganismParsingBadEntry(unittest.TestCase):
  def test_missing_child(self):
    test_input = ['A, B ->\n']
    organisms = OrganismParser(test_input)
    with self.assertRaises(MissingChildError):
      organisms.produce_organisms()

  def test_missing_child_single_parent(self):
    test_input = ['A ->\n']
    organisms = OrganismParser(test_input)
    with self.assertRaises(MissingChildError):
      organisms.produce_organisms()

  def test_missing_parent(self):
    test_input = ['-> A\n']
    organisms = OrganismParser(test_input)
    with self.assertRaises(MissingParentError):
      organisms.produce_organisms()

  def test_missing_second_parent(self):
    test_input = ['B, -> A\n']
    organisms = OrganismParser(test_input)
    with self.assertRaises(MissingParentError):
      organisms.produce_organisms()

  def test_missing_arrow(self):
    test_input = ['A, B  C\n']
    organisms = OrganismParser(test_input)
    with self.assertRaises(MalformedEntryError):
      organisms.produce_organisms()

  def test_bad_arrow(self):
    test_input = ['A, B - >  C\n']
    organisms = OrganismParser(test_input)
    with self.assertRaises(MalformedEntryError):
      organisms.produce_organisms()


class TestOrganismParsingOddTree(unittest.TestCase):
  def test_lone_entry_and_parents(self):
    self.assertTrue(False)

  def test_two_single_parents(self):
    self.assertTrue(False)

  def test_parents_after_children(self):
    self.assertTrue(False)


class TestOrganismParsingBadTree(unittest.TestCase):
  def test_own_child(self):
    self.assertTrue(False)

  def test_own_great_grand_child(self):
    self.assertTrue(False)

  def test_more_than_two_parents(self):
    self.assertTrue(False)


class TestOrganismParsingComments(unittest.TestCase):
  def setUp(self):
    test_input = ['# A, B -> C\n', '# This is also a comment\n', '\n', '     \n']
    organism_parser = OrganismParser(test_input)
    self.organisms = organism_parser.produce_organisms()

  def test_no_organisms(self):
    self.assertEqual(0, len(self.organisms))


class TestOddNames(unittest.TestCase):
  def test_single_char_organism(self):
    self.assertEqual('A', valid_organism_identifier('A'))

  def test_multi_char_organism(self):
    self.assertEqual('Anna', valid_organism_identifier('Anna'))

  def test_char_and_nums_organisms(self):
    self.assertEqual('Anna123', valid_organism_identifier('Anna123'))
    self.assertEqual('123Anna', valid_organism_identifier('123Anna'))
    self.assertEqual('A123nna', valid_organism_identifier('A123nna'))
    self.assertEqual('123', valid_organism_identifier('123'))

  def test_symbols_organisms(self):
    self.assertEqual('@#$%^&*', valid_organism_identifier('@#$%^&*'))

  def test_stripped_name_organisms(self):
    self.assertEqual('Anna', valid_organism_identifier('   Anna    \n'))


class TestOrganismParsingBadName(unittest.TestCase):
  def test_special_symbol_comma(self):
    self.assertFalse(valid_organism_identifier('An,na'))

  def test_special_symbol_gt(self):
    self.assertFalse(valid_organism_identifier('An>na'))

  def test_special_symbol_dash(self):
    self.assertFalse(valid_organism_identifier('An-na'))

  def test_special_symbol_space(self):
    self.assertFalse(valid_organism_identifier('An na'))


if __name__ == '__main__':
    unittest.main()
