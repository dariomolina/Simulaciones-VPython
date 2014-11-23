import visual
# caja=visual.box(pos=visual.vector(4,2,3), size=(8.,4.,6.), color=visual.color.red)
# bola=visual.sphere(pos=visual.vector(0,0,0), radius=3, color=visual.color.green)
# flecha=visual.arrow(pos=visual.vector(0,0,0), axis=(-3,-5,-1), color=visual.color.white)

class Ball(visual.sphere):
	def __init__(self):
		visual.sphere.__init__(self,radius=0)
		self.velocity=(0,0,0)
		self.masa=0

	def setPos(self, vector):
		self.pos=vector

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
		self.masa=0

	def setPos(self, vector):
		self.pos=vector

	def setSize(self, size):
		self.size=size

	def setColor(self, color):
		self.color=color

	def setVelocity(self, velocity):
		self.velocity=velocity

ball1=Ball()
box1=Box()
ball1.setRadius(1)
ball1.setPos((1,4,5))

box1.setSize((8.,4.,6))

		