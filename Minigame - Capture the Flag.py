#-----import statements---------------------------------------------------------------------------
import turtle as trtl
import random as rand
#-----initialize turtle---------------------------------------------------------------------------
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
territories = trtl.Turtle()   #This turtle draws the user territory and the enemy territory.

start_button = trtl.Turtle()
score_writer = trtl.Turtle()

user = trtl.Turtle()
user_flag = trtl.Turtle()

enemy1 = trtl.Turtle()
enemy2 = trtl.Turtle()
enemy_flag = trtl.Turtle()
#-----game configuration-------------------------------------------------------------------------
#Setting up the User's Score
score = 0
font_setup = ("Arial", 30, "normal")
score_writer.speed(0)
score_writer.penup()
score_writer.shapesize(0.1)
score_writer.goto(-75,-190)
score_writer.write("Score: " + str(score), font=font_setup)

#Setting up the territories-turtle
territories.speed(0)
territories.penup()
territories.pensize(5)
territories.goto(-300,125)
territories.pendown()

#Drawing the boundary
angle = 270
for i in range(2):
  territories.forward(600)
  territories.setheading(angle)
  angle -= 90
  territories.forward(250)
  territories.setheading(angle)
  angle -= 90

#Dividing up the boundary into 2 opposing territories
territories.forward(300)
territories.setheading(270)
territories.forward(250)

#Seting up the user-turtle
user.speed(0)
user.penup()
user.shape("circle")
user.shapesize(1)
user.color("Grey")
user.goto(-20,0)

#Seting up the enemy-turtles
enemy1.speed(0)
enemy1.penup()
enemy1.shape("circle")
enemy1.shapesize(1)
enemy1.color("Red")
enemy1.goto(130,50)

enemy2.speed(0)
enemy2.penup()
enemy2.shape("circle")
enemy2.shapesize(1)
enemy2.color("Red")
enemy2.goto(130,-50)

#Setting up the opposing flags
user_flag.speed(0)
user_flag.penup()
user_flag.shape("square")
user_flag.shapesize(1)
user_flag.color("Grey")
user_flag.goto(-280,0)

enemy_flag.speed(0)
enemy_flag.penup()
enemy_flag.shape("square")
enemy_flag.shapesize(1)
enemy_flag.color("Red")
enemy_flag.goto(280,0)

#Setting up the start_button
font_setup = ("Arial", 60, "normal")
start_button.speed(0)
start_button.penup()
start_button.shapesize(2)
start_button.goto(-100, 150)
start_button.write("Start", font=font_setup)
#-----game functions------------------------------------------------------------------------------
#User sets difficulty
  #Allows the User to choose their difficulty (Changes the speed of the enemies). If user fails to enter the avaliable difficulties, the fucntion will start over.
def choose_difficulty():
  difficulty = input("- Easy:        Enemy Speed = 2 \n- Medium:      Enemy Speed = 4 \n- Hard:        Enemy Speed = 7 \n\nChoose your difficulty: ")
  print("------------------------------------------------------------------------------")
  if difficulty == "Easy":
    enemy1.speed(2)
    enemy2.speed(2)
  elif difficulty == "Medium":
    enemy1.speed(4)
    enemy2.speed(4)
  elif difficulty == "Hard":
    enemy1.speed(7)
    enemy2.speed(7)
  else:
    print("ERROR: That is not a selectable difficulty. \n")
    choose_difficulty()

#Pre-selected Team Color
    #The program will have 5 avaliable colors, and will randomly assign a color to the user's team. Each color has a score goal in which the user will need to get in order to win.
def user_team_color():
  colors_list = ["Pink", "Orange", "Green", "Blue", "Purple"]
  random_num = rand.randint(0, 4)

  #This function requires two lists in order for the user's flag and user's turtle to have the same color.
  chosen_color = []
  chosen_color.append(colors_list[random_num])

  user.color(chosen_color[0])
  user_flag.color(chosen_color[0])  

  if chosen_color[0] == "Pink":
    print("You are Pink! \n\nPink players need a score of 2 to win.")
    print("------------------------------------------------------------------------------")
    return 2
  if chosen_color[0] == "Orange":
    print("You are Orange! \n\nOrange players need a score of 3 to win.")
    print("------------------------------------------------------------------------------")
    return 3
  if chosen_color[0] == "Green":
    print("You are Green! \n\nGreen players need a score of 4 to win.")
    print("------------------------------------------------------------------------------")
    return 4
  if chosen_color[0] == "Blue":
    print("You are Blue! \n\nBlue players need a score of 5 to win.")
    print("------------------------------------------------------------------------------")
    return 5
  if chosen_color[0] == "Purple":
    print("You are Purple! \n\nPurple players need a score of 6 to win.")
    print("------------------------------------------------------------------------------")
    return 6

#User movement functions
def move_user_up():
  user.setheading(90)
  user.forward(10)
  check_boundary()

def move_user_down():
  user.setheading(90)
  user.backward(10)
  check_boundary()

def move_user_left():
  user.setheading(180)
  user.forward(10)
  check_boundary()

def move_user_right():
  user.setheading(180)
  user.backward(10)
  check_boundary()

#Restricts the user's movement of traveling to any area outside the boundary.
def check_boundary():
  if -290 < user.xcor() < 290 and -115 < user.ycor() < 115:
    wn.onkeypress(move_user_up, "w")
    wn.onkeypress(move_user_down, "s")
    wn.onkeypress(move_user_left, "a")
    wn.onkeypress(move_user_right, "d")
    return
  #These conditionals are if the user tries to go beyond the corner.
  elif not user.xcor() > -290 and not user.ycor() < 115:
    wn.onkeypress(None, "w")
    wn.onkeypress(None, "a")
  elif not user.xcor() < 290 and not user.ycor() < 115:
    wn.onkeypress(None, "w")
    wn.onkeypress(None, "d")
  elif not user.xcor() > -290 and not user.ycor() > -115:
    wn.onkeypress(None, "s")
    wn.onkeypress(None, "a")
  elif not user.xcor() < 290 and not user.ycor() > -115:
    wn.onkeypress(None, "s")
    wn.onkeypress(None, "d")
  #These conditionals are if the user tries to go beyond a wall.
  else:
    if not user.ycor() < 115:
      wn.onkeypress(None, "w")
    elif not user.ycor() > -115:
      wn.onkeypress(None, "s")
    elif not user.xcor() > -290:
      wn.onkeypress(None, "a")
    elif not user.xcor() < 290:
      wn.onkeypress(None, "d")

#Collision detection function
def is_collided_with(turtle1, turtle2):
  #10 is the collision radius
  return abs(turtle1.xcor() - turtle2.xcor()) < 10 and abs(turtle1.ycor() - turtle2.ycor()) < 10 
  
#User steals enemy flag
    #After the User steals the enemy flag, the enemy flag dissapears.
def stole_flag():
  global flag_gone
  if is_collided_with(enemy_flag, user):
      enemy_flag.hideturtle()
      flag_gone = True
      caught_by_enemy()
      wn.ontimer(stole_flag, 1)      #Allows the turtles to move at the same time
  else:
      wn.ontimer(stole_flag, 1)

#User Captures enemy flag
    #After the User steals the enemy flag, this function plays. The score will only change when the enemy flag has been stolen and captured (returned to the user's side). The function will then repeat, but do the second condition to make the enemy flag re-appear.
def captured_flag():
  global score
  global stole_and_captured
  global flag_gone
  #This condition will play second everytime in the Function
  if stole_and_captured == True and flag_gone == True:
      update_score()
      stole_and_captured = False
      flag_gone = False
      wn.ontimer(stole_flag, 1)
      captured_flag()
  elif is_collided_with(user_flag, user):
      enemy_flag.showturtle()
      #The section below allows the user to capture the enemy flag, but First, The condition has to check if the user stole the enemy flag, and If True the function will then repeat and add 1 to the user's score. (This condition will play first everytime in the Function)
      if flag_gone == False:
        stole_and_captured = False
      else:  
        stole_and_captured = True
      captured_flag() 
  else:
      wn.ontimer(captured_flag, 1)   #Allows the turtles to move at the same time again

#Enemy movement
    #This function will make the enemies follow the user wherever they go. If the enemies collide with the user the game will end.
def caught_by_enemy():
  enemy1.setheading(enemy1.towards(user))
  enemy1.forward(min(enemy1.distance(user), 10))  #This enemy moves forward by 10
  
  enemy2.setheading(enemy2.towards(user))
  enemy2.forward(min(enemy2.distance(user), 15))  #This enemy moves forward by 15

  if is_collided_with(enemy1, user) or is_collided_with(enemy2, user):
      game_over(False)
  elif is_collided_with(user, enemy1) or is_collided_with(user, enemy2):
      game_over(False)
  else:
      wn.ontimer(caught_by_enemy, 1)

#Game Over Function
    #The user and the enemies will stop moving to indicate that the game has ended. A parameter will be assigned to function when the game ends to indicate a win or a loss. Either the user or the enemy team will dissapear to incidate which side has lost.
def game_over(win):
  if win == False:
    user.color("Grey")
    font_setup = ("Arial", 60, "normal")
    start_button.goto(-190, 150)
    start_button.clear()
    start_button.write("You Lose!", font=font_setup)
    wn.onkeypress(None, "w")
    wn.onkeypress(None, "s")
    wn.onkeypress(None, "a")
    wn.onkeypress(None, "d")
    user.hideturtle()
  elif win == True:
    font_setup = ("Arial", 60, "normal")
    start_button.goto(-180, 150)
    start_button.write("You Win!", font=font_setup)
  
    wn.onkeypress(None, "w")
    wn.onkeypress(None, "s")
    wn.onkeypress(None, "a")
    wn.onkeypress(None, "d")
    enemy1.hideturtle()
    enemy2.hideturtle()

#Update score function
def update_score():
  global score
  global score_goal
  score += 1
  #If the user has not reached the score goal, the game continues.
  if score < score_goal:
    score_writer.clear()
    font_setup = ("Arial", 30, "normal")
    score_writer.write("Score: " + str(score), font=font_setup)
  #If the has reached the score goal, the game ends and the user wins.
  elif score >= score_goal:
    score_writer.clear()
    font_setup = ("Arial", 30, "normal")
    score_writer.write("Score: " + str(score), font=font_setup)
    game_over(True)

#Starts the game after the user has clicked the start button.
def game_start(x,y):
  wn.onkeypress(move_user_up, "w")
  wn.onkeypress(move_user_down, "s")
  wn.onkeypress(move_user_left, "a")
  wn.onkeypress(move_user_right, "d")
  start_button.clear()
  caught_by_enemy()
  stole_flag()
  captured_flag()
  caught_by_enemy()
#-----events--------------------------------------------------------------------------------------
#Instructions for the user
print("Challenge: Capture as many red flags as you can before the enemies catch you!")
print("\nTip: Use the W, A, S, and D keys to move.")
print("------------------------------------------------------------------------------")

#The game algorithm will start here
score_goal = user_team_color()
choose_difficulty()
flag_gone = False
stole_and_captured = False
print("You may click the little triangle under the Start button to begin.")
start_button.onclick(game_start)

wn.listen()
wn.mainloop()
#-------------------------------------------------------------------------------------------------