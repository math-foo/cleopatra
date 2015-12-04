#!/usr/bin/python

import random

number_of_genes = 10000
genotype_dict = {}

class Gene:
  def __init__(self, gene):
    self.gene = gene

  def duplicated(self):
    return self.gene[0] == self.gene[1]

  def cross(self, other_gene):
    if self.gene > other_gene.gene:
      gene_code = other_gene.gene + '_' + self.gene
    else:
      gene_code = self.gene + '_' + self.gene

    if gene_code in genotype_dict:
      new_genes = genotype_dict[gene_code]
    else:
      new_genes = []
      for gene_a in self.gene:
        for gene_b in other_gene.gene:
          if gene_a > gene_b:
            new_genes.append(gene_b+gene_a)
          else:
            new_genes.append(gene_a+gene_b)

      genotype_dict[gene_code] = new_genes

    i = random.randint(0,3)
	 
    return Gene(new_genes[i])

class GeneFactory:
  def __init__(self):
    self.current_gene = 'A'

  def fetch_gene(self):
     gene_string = self.current_gene +  self.current_gene.lower()
     self.current_gene = chr(ord(self.current_gene) + 1)
     return Gene(gene_string)

gene_factory = GeneFactory()


class Organism:
  def __init__(self, name, mother=None, father=None ):
    self.name = name

    if not mother and not father:
      new_gene = gene_factory.fetch_gene()
      self.genes = [new_gene for i in xrange(number_of_genes)]
    else:
      self.genes = []

      for i in xrange(number_of_genes):
        self.genes.append(father.genes[i].cross(mother.genes[i]))

  def show(self):
    duplicated_genes = len([gene for gene in self.genes if gene.duplicated()])

    total = duplicated_genes*100.0/number_of_genes

    print self.name + " was " + str(total) + "% inbred"
