#!/usr/bin/python

from organism import *
         
Pt5 = Organism("Ptolmey V")
Pt5.show()
Cl1 = Organism("Cleopatra")
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
