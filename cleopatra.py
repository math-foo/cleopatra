#!/usr/bin/python

from organism_parsing import OrganismParser
import sys

if __name__ == '__main__':
    input_file_contents = open(sys.argv[1], 'r').readlines()
    new_parser = OrganismParser(input_file_contents)
    organism_tree = new_parser.produce_organisms()
    print organism_tree.generate_summary()
