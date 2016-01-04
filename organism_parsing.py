#!/usr/bin/python

import organism
import sys

class OrganismParser(object):

  def __init__(self, file_name):
    self.entries = open(file_name, 'r').readlines()

  def produce_organisms(self):
    #TODO: implement this.
    return []

if __name__ == '__main__':
    new_parser = OrganismParser(sys.argv[1])
    print new_parser.produce_organisms()
