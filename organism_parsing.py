#!/usr/bin/python

import re
import sys

class OrganismParser(object):

  def __init__(self, entries):
    self.entries = entries

  def produce_organisms(self):
    #TODO: implement this.
    relationships = {}

    for entry in self.entries:
      # Skipping commented out lines
      if entry[0] != '#' and entry.strip():
        entry = entry.strip()
        if '->' in entry:
          parents_string, child_string = entry.split('->')
        else:
          if not re.match('[->, ]', entry):
            if entry not in relationships:
              relationships[entry] = []

    return relationships


if __name__ == '__main__':
    input_file_contents = open(sys.argv[1], 'r').readlines()
    new_parser = OrganismParser(input_file_contents)
    print new_parser.produce_organisms()
