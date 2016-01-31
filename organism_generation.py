#!/usr/bin/python

from organism import Organism

class OrganismGenerator:
  def __init__(self, relationship_dict):
    self.relationships = relationship_dict

  def generate_organisms(self):
    # Proceed down the tree, creating a dict of label to organism object
    self.organism_dict = {}
    unprocessed_relationships = self.relationships.copy()

    while unprocessed_relationships:
      to_remove = []

      for entry in unprocessed_relationships:
        parents = unprocessed_relationships[entry]
        if not parents:
          self.organism_dict[entry] = Organism(entry)
          to_remove.append(entry)
        else:
          ready_to_process = True
          for parent in parents:
            if parent not in self.organism_dict:
              ready_to_process = False

          if ready_to_process:
            if len(parents) == 1:
              temp_organism = Organism('unknown parent')
              known_organism = self.organism_dict[parents[0]]
              self.organism_dict[entry] = Organism(entry, mother=known_organism, father=temp_organism)
            elif len(parents) == 2:
              known_organism_0 = self.organism_dict[parents[0]]
              known_organism_1 = self.organism_dict[parents[1]]
              self.organism_dict[entry] = Organism(entry, mother=known_organism_0, father=known_organism_1)

            to_remove.append(entry)

      for entry in to_remove:
        del unprocessed_relationships[entry]
