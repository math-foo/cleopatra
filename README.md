# cleopatra
Cleopatra is a command line script that takes a file describing the genetic relationships between set of organisms, runs a Monte Carlo simulation, and returns the genetic makeup of each organism, including how inbred they are.

Inspired by the family tree of Cleopatra VI, the eponymous Cleopatra of Anthony & Cleopatra

Note: Since this is a Monte Carlo simulation, values can and will differ between multiple runs.

# How to Use
`./cleopatra name_of_file`

# Sample Input
For contents of sample input file see `cleopatra_family_tree` included in this repository.

# Sample output

`CleopatraVII is a child of CleopatraV and PtolemyXIIAuletes`

`Genetically, CleopatraVII is:`

`52.44% CleopatraI`

`47.56% PtolemyV`

`And 42.72% inbred`
