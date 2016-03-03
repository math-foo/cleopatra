#!/usr/bin/python

from organism_parser import OrganismParser

if __name__ == '__main__':
    input_file_contents = open(sys.argv[1], 'r').readlines()
    new_parser = OrganismParser(input_file_contents)
    organism_tree = new_parser.produce_organisms()
    organism_tree.generate_summary()
