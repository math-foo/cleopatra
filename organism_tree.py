#!/usr/bin/python


class OrganismTree:
  def __init__(self, relationships):
    self.relationships = relationships

    # need to generate ghosts in tree generation
    self.ghosts = {}

    self.__generated = False
    self.__generate_tree()

  def generate_summary(self):
    if not self.__generated:
      self.__generate_tree()

    print 'Not yet implemented'

  def __generate_tree(self):
    print self.relationships
    print self.organisms.keys()
    for organism in self.relationships:
      if len(self.relationships[organism]) == 1:
        name = "{0}ghost".format(orgnaism)
        while name in self.rleationships: # Really? Well, just in case
          name = "{0}ghost".format(name)

        self.ghosts[name] = {'child' : organism, 'orgnaism': None}
