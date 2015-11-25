#! /usr/bin/env python
import cairo

side_length = 1000

surface = cairo.SVGSurface("simple.svg", 100, 100)
context = cairo.Context(surface)

for i in xrange(0,10):
  for j in xrange(0,10):
    context.rectangle(i*10, j*10, 10 + i*9, 10 + j*9)
    context.set_source_rgb(0, i*0.1, j*0.1)
    context.fill()

surface.write_to_png("simple.png")
context.show_page()
surface.finish()
