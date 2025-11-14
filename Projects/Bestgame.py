# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
# TODO - create your player character
s1 =  create_sprite("dog", 100,200)
set_background("castle")
# TODO - set the starting value for your variable

# Section 3: Controls
def move_up(): 
	s1.setheading(90)
	s1.forward (200)
window.onkeypress(move_up,"Up")
def move_down(): 
	s1.setheading(270)
	s1.forward (200)
window.onkeypress(move_down,"Down")

# Section 4: Game Loop
window.listen()
timer = 0
lives = 3
obstacles=[]
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 # automaticly create basketballs every 1 seconds

	if timer % 10 == 0:
		y_position = random.randint(-250, 250)
		s2 = create_sprite("basketball",300,y_position)
		s2.setheading(180)
		obstacles.append(s2) 

	# move each ball 
	for s2 in obstacles:
		s2.forward(10)

# if you collide, lose a life  
		if get_distance(s1,s2) < 50:
			lives -= 1 
			s2.hideturtle()
			obstacles.remove(s2) 







	window.update()

	# if :
	# 	break
	

print("Game Over")