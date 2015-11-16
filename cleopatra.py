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
  def __init__(self, name, genelist=[], mother=None, father=None ):
    self.name = name

    if genelist:
      self.genes = genelist
    elif mother and father:
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

         
Pt5 = Organism("Ptolmey V", genelist=['Aa' for i in xrange(number_of_genes)])
Pt5.show()
Cl1 = Organism("Cleopatra", genelist=['Bb' for i in xrange(number_of_genes)])
Cl1.show()

Pt6 = Organism("Ptolemy VI", mother=Cl1, father=Pt5)
Pt6.show()
Pt8 =  Organism("Ptolemy VIII", mother=Cl1, father=Pt5)
Pt8.show()
Cl2 =  Organism("Cleopatra II", mother=Cl1, father=Pt5)
Cl2.show()

print "----"

Cl3 = Organism("Cleopatra III", mother=Cl2, father=Pt6)
Cl3.show()

print "------"

Cl4 = Organism("Cleopatra IV", mother=Cl3, father=Pt8)
Cl4.show()
Pt9 = Organism("Ptolmey IX", mother=Cl3, father=Pt8)
Pt9.show()
Pt10 = Organism("Ptolmey X", mother=Cl3, father=Pt8)
Pt10.show()
Cs1 = Organism("Cleopatra Selene I", mother=Cl3, father=Pt8)
Cs1.show()

print "---------"

Pt12 = Organism("Ptomley XII", mother=Cl4, father=Pt9)
Pt12.show()
Br3 = Organism("Bernice III", mother=Cs1, father=Pt9)
Br3.show()

print "------"

Cl5 = Organism("Cleopatra V", mother=Br3, father=Pt10)
Cl5.show()

print "------"

Cl6 = Organism("Cleopatra VII", mother=Cl5, father=Pt12)
Cl6.show()
