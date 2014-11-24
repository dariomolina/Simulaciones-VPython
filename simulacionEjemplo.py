#!/usr/bin/python
# -*- coding: <encoding name> -*-
# Ejemplo de simulacion de movimiento de dos cuerpos geometricos aplicando vpython

import visual
# flecha=visual.arrow(pos=visual.vector(0,0,0), axis=(-3,-5,-1), color=visual.color.white)
suelo=visual.box(pos=visual.vector(0,-1,0), size=(10,0.1,10), color=visual.color.red)
# bola=visual.sphere(pos=visual.vector(-3,0,0), radius=0.5, color=visual.color.green)

class Ball(visual.sphere):
	def __init__(self):
 		visual.sphere.__init__(self,radius=0)
 		self.velocity=(0,0,0)
 		self.acceleration=(0,0,0)
 		self.masa=0

 	def setPos(self, pos):
 		self.pos=pos

 	def setRadius(self, radius):
 		self.radius=radius

 	def setColor(self, color):
 		self.color=color

 	def setVelocity(self, velocity):
 		self.velocity=velocity


class Box(visual.box):
 	def __init__(self, size=(0.,0.,0.)):
 		visual.box.__init__(self)
 		self.velocity=(0,0,0)
 		self.acceleration=(0,0,0)
 		self.masa=0

 	def setPos(self, vector):
 		self.pos=vector

 	def setSize(self, size):
 		self.size=size

 	def setColor(self, color):
 		self.color=color

 	def setVelocity(self, velocity):
 		self.velocity=velocity

ball1=Ball() #create ball
box1=Box() #create box
box1.setSize((0.1,0.1,0.1))
ball1.setRadius(0.05)
r=visual.vector(-1,0,0) #initial position of the ball
h=visual.vector(3,0,0) #initial position of the box
z=-100
while(z<100):
 	visual.rate(100)
 	ball1.setPos(r)
 	box1.setPos(h)
 	r.x=r.x+0.001
 	h.x=h.x-0.001
	print ball1.pos.x