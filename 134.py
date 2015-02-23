class Ball():
	# class attributes
	# Ball position
	x = 0
	y = 0

	# Ball's vector
	change_x = 0
	change_y = 0

	# Ball size
	size = 10

	# ball color
	color = [255, 255, 255]

	# ---- class methods ----
	def move(self):
		self.x += self.change_x
		self.y += slef.change_y

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )

theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255,0,0]

