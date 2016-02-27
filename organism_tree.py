#!/usr/bin/python

from organism import Organism

class OrganismTree:
  def __init__(self, relationships):
    self.relationships = relationships

    # need to be generated in tree generation
    self.ghosts = {}
    self.organisms = {}

    self.__generated = False
    self.__generate_tree()

  def generate_summary(self):
    if not self.__generated:
      self.__generate_tree()

    summary_string = ""
    processed_organisms = []

    for organism_name in self.relationships:
      if len(self.relationships[organism_name]) == 0:
        summary_string += "{0} has no parents\n".format(organism_name)
        processed_organisms.append(organism_name)

    while len(processed_organisms) < len(self.relationships):
      for organism_name in self.relationships:
        if organism_name in processed_organisms:
          continue
        parents_found = True
        parents = self.relationships[organism_name]
        for parent in parents:
          parents_found &= (parent in processed_organisms)

        if parents_found:
          processed_organisms.append(organism_name)
          parents.sort()
          if len(parents) == 1:
            summary_string += "{0} is a child of {1}\n".format(organism_name, parents[0])
          else:
            summary_string += "{0} is a child of {1} and {2}\n".format(organism_name, parents[0], parents[1])

    return summary_string

  def __generate_tree(self):
    unprocessed_relationships = self.relationships.copy()

    while unprocessed_relationships:
      to_remove = []

      for entry in unprocessed_relationships:
        parents = unprocessed_relationships[entry]
        if not parents:
          self.organisms[entry] = Organism(entry)
          to_remove.append(entry)
        else:
          ready_to_process = True
          for parent in parents:
            if parent not in self.organisms:
              ready_to_process = False

          if ready_to_process:
            if len(parents) == 1:
              ghost_name = entry

              while ghost_name in self.relationships:
                ghost_name = "{0}#Ghost".format(ghost_name)

              temp_organism = Organism("unknown")
              self.ghosts[ghost_name] = {'child': entry, 'organism': temp_organism}
              known_organism = self.organisms[parents[0]]
              self.organisms[entry] = Organism(entry, mother=known_organism, father=temp_organism)
            elif len(parents) == 2:
              known_organism_0 = self.organisms[parents[0]]
              known_organism_1 = self.organisms[parents[1]]
              self.organisms[entry] = Organism(entry, mother=known_organism_0, father=known_organism_1)

            to_remove.append(entry)

      for entry in to_remove:
        del unprocessed_relationships[entry]

    self.__generated = True
