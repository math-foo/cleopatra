#!/usr/bin/python

import sys

class OrganismParser(object):

  def __init__(self, entries):
    self.entries = entries

  def produce_organisms(self):
    #TODO: implement this.
    parsed_entries = []

    for entry in self.entries:
      # Skipping commented out lines
      if entry[0] != '#' and entry.strip():
        parsed_entries.append(entry)

    return parsed_entries


if __name__ == '__main__':
    input_file_contents = open(sys.argv[1], 'r').readlines()
    new_parser = OrganismParser(input_file_contents)
    print new_parser.produce_organisms()
