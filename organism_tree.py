#!/usr/bin/python


# Maybe I can put the display methods in here?
class OrganismTree:
  def __init__(self, relationships, organisms):
    self.relationships = relationships
    self.organisms = organisms
    # need to generate ghosts in tree generation
    self.ghosts = {}

  def generate_visualization(self):
    print 'Not yet implemented'
