#! /usr/bin/env python
import cairo
from cleopatra import Cl6

Cl6.show()

class OrganismVisualization:
  def __init__(self, organism):
    self.surface = cairo.SVGSurface("simple.svg", 100, 100)
    self.context = cairo.Context(self.surface)
    self.organism = organism


  def to_png(self):
    gene_copy = self.organism.genes[:]
    gene_copy.sort(key=lambda gene: "" if gene.duplicated() else gene.gene)
    for i in xrange(0,100):
      for j in xrange(0,100):
        self.context.rectangle(j, i, 1 + j, 1 + i)
        gene = gene_copy[i*100+j]
        if gene.duplicated():
          self.context.set_source_rgb(0, 1, 0)
        else:
          self.context.set_source_rgb(1, 0, 0)
        self.context.fill()

    self.surface.write_to_png("simple.png")
    self.context.show_page()
    self.surface.finish()

visualizer = OrganismVisualization(Cl6)
visualizer.to_png()
