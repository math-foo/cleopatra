#!/usr/bin/python

import random

gene_names = ['A', 'B', 'a', 'b']
number_of_genes = 100000 
genotype_dict = {}

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
  def __init__(self, gene_list, name):
        self.genes = gene_list
        self.name = name


  def breed(self, other, new_name):
    new_gene_list = []

    for i in xrange(number_of_genes):
      new_gene_list.append(cross(self.genes[i], other.genes[i]))

    return Organism(new_gene_list, new_name)

  def show(self):
    r_dict = {'AA': 0, 'aa': 0, 'BB': 0, 'bb': 0}

    for gene in self.genes:
       if gene in r_dict:
         r_dict[gene] += 1

    total = sum(r_dict.values())*100.0/number_of_genes

    print self.name + " was " + str(total) + "% inbred"

         

Pt5 = Organism(['Aa' for i in xrange(number_of_genes)], "Ptolemy V")
Pt5.show()
Cl1 = Organism(['Bb' for i in xrange(number_of_genes)], "Cleopatra I")
Cl1.show()

Pt6 = Pt5.breed(Cl1, "Ptolemy VI")
Pt6.show()
Pt8 = Pt5.breed(Cl1, "Ptolmey VIII")
Pt8.show()
Cl2 = Pt5.breed(Cl1, "Cleopatra II")
Cl2.show()

print "----"

Cl3 = Pt6.breed(Cl2, "Cleopatra III")
Cl3.show()

print "------"

Cl4 = Pt8.breed(Cl3, "Cleopatra IV")
Cl4.show()
Pt9 = Pt8.breed(Cl3, "Ptolmey IX")
Pt9.show()
Pt10 = Pt8.breed(Cl3, "Ptolmey X")
Pt10.show()
Cs1 = Pt8.breed(Cl3, "Cleopatra Selene I")
Cs1.show()

print "---------"

Pt12 = Pt9.breed(Cl4, "Ptomley XII")
Pt12.show()
Br3 = Pt9.breed(Cs1, "Bernice III")
Br3.show()

print "------"

Cl5 = Pt10.breed(Br3, "Cleopatra V")
Cl5.show()

print "------"

Cl6 = Pt12.breed(Cl5, "Cleopatra VII")
Cl6.show()
