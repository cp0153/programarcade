# program template for Spaceship
import simplegui
import math
import random
 
# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
started = False
rock_group = set([])
missile_group = set([])
explosion_group = set([])
 
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
 
    def get_center(self):
        return self.center
    
    def get_size(self):
        return self.size
    
    def get_radius(self):
        return self.radius
    
    def get_lifespan(self):
        return self.lifespan
    
    def get_animated(self):
        return self.animated
 
# debris image - art created by Kim Lathrop
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/debris2_blue.png")
# nebula image
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/nebula.jpg")
# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/splash_image.png")
# ship image
ship_info = ImageInfo([57.5, 39], [115, 78], 48)
ship_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/spaceship.png")
# missile image
missile_info = ImageInfo([5,5], [10, 10], 3, 60)
missile_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/shot.png")
# asteroid images
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/asteroid.png")
dstar_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/d_star.png")
evil_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/evil.png")
# animated explosion
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/ost1.mp3")
missile_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/u/15465715/python_resources/ricerocks/shot.wav")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.set_volume(.5)
 
# helper functions
def angle_to_vector(ang):
    """ Returns direction vector from initial angle """
    return [math.cos(ang), math.sin(ang)]
 
def dist(p,q):
    """ Calculates distance from point p to point q """
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)
 
def process_sprite_group(canvas, sprites_set):
    for s in set(sprites_set):
        if s.update():
            sprites_set.remove(s)
        s.draw(canvas)
 
def group_collide(group, other_object):
    global explosion_group
    collisions = 0
    for g in set(group):
        if g.collide(other_object):
            explosion_group.add(Sprite(g.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound))
            explosion_sound.play()
            group.remove(g)
            collisions += 1
            
    return collisions
 
def group_group_collide(group, other_group):
    collisions = 0
    for g in set(group):
        if group_collide(other_group, g):
            group.remove(g)
            collisions += 1
            
    return collisions
 
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def draw(self,canvas):
        if not self.thrust:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)       
        else:
            canvas.draw_image(self.image, (self.image_center[0] * 3, self.image_center[1]), self.image_size, self.pos, self.image_size, self.angle)       
            
    def rotation(self,new_angle_vel):
        self.angle_vel = new_angle_vel    
    
    def thrusting(self):
        self.thrust = not self.thrust
        if self.thrust:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
    
    def shoot(self):
        global missile_group
 
        missile_group.add(Sprite([self.pos[0] + (self.forward[0] * self.radius), self.pos[1] + (self.forward[1] * self.radius)], 
                           [self.vel[0] + self.forward[0] * 5, self.vel[1] + self.forward[1] * 5], 
                           0, 0, missile_image, missile_info, missile_sound))
        
    def update(self):
        
        # updating ship position based on angle and velocity, within canvas edges
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        # adding friction, so that the ship will eventually stop when not thrusting
        friction = 0.01
        self.vel[0] *= (1 - friction)
        self.vel[1] *= (1 - friction)
        
        self.forward = angle_to_vector(self.angle)
        # adding thrust acceleration when thrust is active
        if self.thrust:
            self.vel[0] += self.forward[0] * 0.1
            self.vel[1] += self.forward[1] * 0.1
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, [self.image_center[0] + self.age * self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        return self.age >= self.lifespan
        
    def collide(self, other_object):
        return dist(self.pos, other_object.get_position()) < self.radius + other_object.get_radius()
          
def draw(canvas):
    global time, lives, score, started, rock_group
    
    # animate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])
 
    # updates and draws ship
    my_ship.draw(canvas)
    my_ship.update()
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())       
    else:
        timer.start()
        process_sprite_group(canvas, rock_group)
        
        if group_collide(rock_group, my_ship) > 0:
            lives -= 1
            explosion_group.add(Sprite(my_ship.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound))
            explosion_sound.play()
            if lives == 0:
                started = False
                timer.stop()
                rock_group = set([])
                soundtrack.pause()
                
        booms = group_group_collide(rock_group, missile_group)
        if booms > 0:
            score += 10 * booms
   
    # draws missiles, lives and score info
    process_sprite_group(canvas, missile_group)
    process_sprite_group(canvas, explosion_group)
    canvas.draw_text("Lives: " + str(lives), [WIDTH / 15, HEIGHT / 30], 20, "White")
    canvas.draw_text("Score: " + str(score), [WIDTH / 1.2, HEIGHT / 30], 20, "White")
        
     
# Keyboard handlers
def keydown(key):
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["a"]:
        my_ship.rotation(-.075)
    if key == simplegui.KEY_MAP["right"] or key == simplegui.KEY_MAP["d"]:
        my_ship.rotation(.075)
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["w"]:
        my_ship.thrusting()
    if key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
 
def keyup(key):
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"] or key == simplegui.KEY_MAP["a"] or key == simplegui.KEY_MAP["d"]:
        my_ship.rotation(0)
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["w"]:
        my_ship.thrusting()
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, score, lives
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        score = 0
        lives = 3
        soundtrack.rewind()
        soundtrack.play()
        
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
 
    rock_pos = [random.randrange(800), random.randrange(600)]
    while dist(rock_pos, my_ship.get_position()) < my_ship.get_radius() + 100:
        rock_pos = [random.randrange(800), random.randrange(600)]
        
    if len(rock_group) <= 12:
        rock_group.add(Sprite(rock_pos, [random.randrange(-10, 10) / 10, random.randrange(-10, 10) / 10], random.random() * 6.28, random.choice([-0.01, 0.01]), random.choice([asteroid_image, dstar_image, evil_image]), asteroid_info))
    
# initialize frame
frame = simplegui.create_frame("Asteroids Reloaded", WIDTH, HEIGHT)
 
# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
 
# register handlers
frame.add_label("ASTEROIDS RELOADED")
frame.add_label("Ship controls:")
frame.add_label("Left: A or left arrow:")
frame.add_label("Right: D or right arrow:")
frame.add_label("Thrust: W or up arrow")
frame.add_label("Fire: space")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000, rock_spawner)
 
# get things rolling
frame.start()
