#!/usr/bin/python

from organism import Organism

def count_genes(gene_list):
  gene_count = {}

  for gene in gene_list:
    for g in gene:
      x = g.upper()
      if x not in gene_count:
        gene_count[x] = 1
      else:
        gene_count[x] += 1

  return gene_count

class OrganismTree:
  GENE_TOTAL = 20000.0

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
    genetic_dict = {}

    for organism_name in self.relationships:
      if len(self.relationships[organism_name]) == 0:
        gene = self.organisms[organism_name].genes[0].gene[0].upper()
        genetic_dict[gene] = organism_name
        summary_string += "{0} has no parents\n\n".format(organism_name)
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
            ghost_name = "{0}#Ghost".format(organism_name)
            ghost_gene = self.ghosts[ghost_name]['organism'].genes[0].gene[0].upper()
            genetic_dict[ghost_gene] = "unknown parent of {0}".format(organism_name)
            summary_string += "{0} is a child of {1}\n".format(organism_name, parents[0])
          else:
            summary_string += "{0} is a child of {1} and {2}\n".format(organism_name, parents[0], parents[1])

          organism = self.organisms[organism_name]
          genes = [x.gene for x in organism.genes]
          gene_frequency = count_genes(genes)
          summary_string += "Genetically, {0} is:\n".format(organism_name)
          for gene in gene_frequency:
            name = genetic_dict[gene]
            percent = (gene_frequency[gene]/self.GENE_TOTAL) * 100
            summary_string += "{0}% {1}\n".format(percent, name)
          summary_string += "\n"

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
