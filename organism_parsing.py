#!/usr/bin/python

from organism_generation import OrganismGenerator

import re
import sys

def valid_organism_identifier(organism_name):
  organism_name = organism_name.strip()
  if not re.search('[>, -]', organism_name):
    return organism_name
  else:
    return False


def check_for_cycles(relationships):
    verified_relationships = {}
    root_organisms = []

    for organism in relationships:
      if not relationships[organism]:
        verified_relationships[organism] = []
        root_organisms.append(organism)

    for organism in root_organisms:
      del relationships[organism]

    while relationships:
      new_verified = []
      for organism in relationships:
        parents = relationships[organism]
        verified = True
        for parent in parents:
          if parent not in verified_relationships:
            verified = False

        if verified:
          new_verified.append(organism)

      if len(new_verified) == 0:
        raise OwnChildError("One of {0} is its own child".format(relationships.keys()))

      for organism in new_verified:
        verified_relationships[organism] = relationships[organism]
        del relationships[organism]

    return True


# Root exception for parsing
class OrganismParseError(Exception):
  pass


# Parsing related exceptions
class MalformedEntryError(OrganismParseError):
  pass


class MissingChildError(OrganismParseError):
  pass


class OwnChildError(OrganismParseError):
  pass


class MissingParentError(OrganismParseError):
  pass


class TooManyParentsError(OrganismParseError):
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
              for parent in parents:
                if parent not in relationships:
                  relationships[parent] = []

              if child not in relationships:
                relationships[child] = parents
              else:
                existing_parents = relationships[child]
                if len(existing_parents) + len(parents) > 2:
                  raise TooManyParentsError("Organism {0} has parent(s) {1} and {2}".format(child, existing_parents, parents))
                else:
                  existing_parents += parents
                  relationships[child] = existing_parents
            elif not child:
              raise MissingChildError("Child missing from line: {0}".format(entry))
            elif not parents:
              raise MissingParentError("Parent missing from line: {0}".format(entry))

          else:
            raise MalformedEntryError("Entry: {0} is malformed - missing or malformed: ->".format(entry))

    check_for_cycles(relationships.copy())
    generator = OrganismGenerator(relationships)
    return generator.generate_organisms()


if __name__ == '__main__':
    input_file_contents = open(sys.argv[1], 'r').readlines()
    new_parser = OrganismParser(input_file_contents)
    print new_parser.produce_organisms()
