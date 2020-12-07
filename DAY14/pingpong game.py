import turtle 

sc = turtle.Screen() 
sc.title("AJAY RAM PING PONG GAME") 
sc.bgcolor("green") 
sc.setup(width=1000, height=600) 

player1_pad = turtle.Turtle() 
player1_pad.speed(0) 
player1_pad.shape("square") 
player1_pad.color("blue") 
player1_pad.shapesize(stretch_wid=6, stretch_len=2) 
player1_pad.penup() 
player1_pad.goto(-400, 0) 

right_pad = turtle.Turtle() 
right_pad.speed(0) 
right_pad.shape("square") 
right_pad.color("black") 
right_pad.shapesize(stretch_wid=6, stretch_len=2) 
right_pad.penup() 
right_pad.goto(400, 0) 

hit_ball = turtle.Turtle() 
hit_ball.speed(40) 
hit_ball.shape("circle") 
hit_ball.color("red") 
hit_ball.penup() 
hit_ball.goto(0, 0) 
hit_ball.dx = 5
hit_ball.dy = -5
 
player1 = 0
player2 = 0

sketch = turtle.Turtle() 
sketch.speed(0) 
sketch.color("white") 
sketch.penup() 
sketch.hideturtle() 
sketch.goto(0, 260) 
sketch.write("Player_1 : 0 Player_2: 0",
			align="center", font=("Courier", 24, "normal")) 

def paddleaup(): 
	y = player1_pad.ycor() 
	y += 20
	player1_pad.sety(y) 

def paddleadown(): 
	y = player1_pad.ycor() 
	y -= 20
	player1_pad.sety(y) 

def paddlebup(): 
	y = right_pad.ycor() 
	y += 20
	right_pad.sety(y) 

def paddlebdown(): 
	y = right_pad.ycor() 
	y -= 20
	right_pad.sety(y) 

sc.listen() 
sc.onkeypress(paddleaup, "w") 
sc.onkeypress(paddleadown, "s") 
sc.onkeypress(paddlebup, "Up") 
sc.onkeypress(paddlebdown, "Down") 

while True: 
	sc.update() 

	hit_ball.setx(hit_ball.xcor()+hit_ball.dx) 
	hit_ball.sety(hit_ball.ycor()+hit_ball.dy) 

	if hit_ball.ycor() > 280: 
		hit_ball.sety(280) 
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280: 
		hit_ball.sety(-280) 
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500: 
		hit_ball.goto(0, 0) 
		hit_ball.dy *= -1
		player1 += 1
		sketch.clear() 
		sketch.write("Player_1 : {} Player_2: {}".format( 
					player1, player2), align="center", 
					font=("Courier", 24, "normal")) 

	if hit_ball.xcor() < -500: 
		hit_ball.goto(0, 0) 
		hit_ball.dy *= -1
		player2 += 1
		sketch.clear() 
		sketch.write("Player1 : {} Palyer2: {}".format( 
								player1, player2), align="center", 
								font=("Courier", 24, "normal")) 

	if (hit_ball.xcor() > 360 and
						hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40): 
		hit_ball.setx(360) 
		hit_ball.dx*=-1
		
	if (hit_ball.xcor()<-360 and
					hit_ball.xcor()>-370) and (hit_ball.ycor()<player1_pad.ycor()+40 and hit_ball.ycor()>player1_pad.ycor()-40): 
		hit_ball.setx(-360) 
		hit_ball.dx*=-1
