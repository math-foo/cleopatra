#!/usr/bin/python

import random

number_of_genes = 100000 
genotype_dict = {}

class GeneFactory:
  def __init__(self):
    self.current_gene = 'A'

  def fetch_gene(self):
     gene_string = self.current_gene +  self.current_gene.lower()
     self.current_gene = chr(ord(self.current_gene) + 1)
     return gene_string

gene_factory = GeneFactory()

def cross(genotype, other_genotype):
    if genotype > other_genotype:
      genotype_code = other_genotype + '_' + genotype
    else:
      genotype_code = genotype + '_' + other_genotype

    if genotype_code in genotype_dict:
      new_genotypes = genotype_dict[genotype_code]
    else:
      new_genotypes = []
      for gene_a in [genotype[0],genotype[1]]:
        for gene_b in [other_genotype[0],other_genotype[1]]:
          if gene_a > gene_b:
            new_genotypes.append(gene_b+gene_a)
          else:
            new_genotypes.append(gene_a+gene_b)

      genotype_dict[genotype_code] = new_genotypes

    i = random.randint(0,3)
	 
    return new_genotypes[i]

class Organism:
  def __init__(self, name, mother=None, father=None ):
    self.name = name

    if not mother and not father:
      new_gene = gene_factory.fetch_gene()
      self.genes = [new_gene for i in xrange(number_of_genes)]
    else:
      self.genes = []

      for i in xrange(number_of_genes):
        self.genes.append(cross(father.genes[i], mother.genes[i]))

  def show(self):
    r_dict = {'AA': 0, 'aa': 0, 'BB': 0, 'bb': 0}

    for gene in self.genes:
       if gene in r_dict:
         r_dict[gene] += 1

    total = sum(r_dict.values())*100.0/number_of_genes

    print self.name + " was " + str(total) + "% inbred"
