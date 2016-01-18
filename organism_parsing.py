#!/usr/bin/python

import re
import sys

def valid_organism_identifier(organism_name):
  organism_name = organism_name.strip()
  if not re.search('[>, -]', organism_name):
    return organism_name
  else:
    return False

class OrganismParseError(Exception):
  pass


class MalformedEntryError(Exception):
  pass


class MissingChildError(OrganismParseError):
  pass


class MissingParentError(OrganismParseError):
  pass


class OrganismParser(object):

  def __init__(self, entries):
    self.entries = entries

  def produce_organisms(self):
    relationships = {}

    for entry in self.entries:
      # Skipping commented out lines
      if entry[0] != '#' and entry.strip():
        if valid_organism_identifier(entry):
          valid_entry = valid_organism_identifier(entry)
          if not re.match('[->, ]', valid_entry):
            if valid_entry not in relationships:
              relationships[valid_entry] = []
        else:
          entry = entry.strip()
          if '->' in entry:
            parents_string, child_string = entry.split('->')

            child = valid_organism_identifier(child_string)

            parents = []
            if ',' not in parents_string:
              valid_parent = valid_organism_identifier(parents_string)
              if valid_parent:
                parents = [valid_parent]
            else:
              if parents_string.count(',') == 1:
                parent_a_string, parent_b_string = parents_string.split(',')
                parent_a = valid_organism_identifier(parent_a_string)
                parent_b = valid_organism_identifier(parent_b_string)

                if parent_a and parent_b:
                  parents = [parent_a, parent_b]

            if parents and child:
              if child not in relationships:
                relationships[child] = parents
            elif not child:
              raise MissingChildError("Child missing from line: {0}".format(entry))
            elif not parents:
              raise MissingParentError("Parent missing from line: {0}".format(entry))

          else:
            raise MalformedEntryError("Entry: {0} is malformed - missing or malformed: ->".format(entry))

    return relationships


if __name__ == '__main__':
    input_file_contents = open(sys.argv[1], 'r').readlines()
    new_parser = OrganismParser(input_file_contents)
    print new_parser.produce_organisms()
