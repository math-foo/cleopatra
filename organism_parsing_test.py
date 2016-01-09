#!/usr/bin/python

import unittest
import organism_parsing


class TestOrganismSimpleParsing(unittest.TestCase):
  def setUp(self):
    test_input = ['A, B -> C\n',
                  'D\n', # Lone organism
                  'E -> F\n',
                  'G, H -> I\n',
                  'G, J -> K\n',
                  'L, M -> N\n',
                  'L, M -> O\n',
                  'P -> Q\n',
                  'P -> R\n']
    organism_parser = organism_parsing.OrganismParser(test_input)
    self.organisms = organism_parser.produce_organisms()

  def test_lone_organism(self):
    self.assertIn('D', self.organisms)
    self.assertEqual([], self.organisms['D'])

  def test_single_parent_organism(self):
    self.assertTrue(False)

  def test_two_parent_organism(self):
    self.assertTrue(False)

  def test_different_parenting_pairs_organism(self):
    self.assertTrue(False)

  def test_two_parents_multiple_children_organism(self):
    self.assertTrue(False)

  def test_single_parent_multiple_children_organism(self):
    self.assertTrue(False)


class TestOrganismParsingComments(unittest.TestCase):
  def setUp(self):
    test_input = ['# A, B -> C\n', '# This is also a comment\n', '\n', '     \n']
    organism_parser = organism_parsing.OrganismParser(test_input)
    self.organisms = organism_parser.produce_organisms()

  def test_no_organisms(self):
    self.assertEqual(0, len(self.organisms))


class TestOrganismParsingOddNames(unittest.TestCase):
  def test_single_char_organism(self):
    self.assertTrue(False)

  def test_multi_char_organism(self):
    self.assertTrue(False)

  def test_char_and_nums_organisms(self):
    self.assertTrue(False)

  def test_symbols_organisms(self):
    self.assertTrue(False)

class TestOrganismParsingOddSpacing(unittest.TestCase):
  def test_bunched_organisms(self):
    self.assertTrue(False)

  def test_normal_organisms(self):
    self.assertTrue(False)

  def test_spaced_out_organisms(self):
    self.assertTrue(False)


class TestOrganismParsingBadName(unittest.TestCase):
  def test_special_symbol_comma(self):
    self.assertTrue(False)

  def test_special_symbol_gt(self):
    self.assertTrue(False)

  def test_special_symbol_dash(self):
    self.assertTrue(False)

  def test_special_symbol_space(self):
    self.assertTrue(False)


class TestOrganismParsingBadEntry(unittest.TestCase):
  def test_missing_child(self):
    self.assertTrue(False)

  def test_missing_child_single_parent(self):
    self.assertTrue(False)

  def test_missing_parent(self):
    self.assertTrue(False)

  def test_missing_second_parent(self):
    self.assertTrue(False)

  def test_missing_arrow(self):
    self.assertTrue(False)

  def test_bad_arrow(self):
    self.assertTrue(False)

class TestOrganismParsingBadTree(unittest.TestCase):
  def test_own_child(self):
    self.assertTrue(False)

  def test_own_great_grand_child(self):
    self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
