from tkinter import *
import random

GAME_HEIGHT = 600
GAME_WIDTH = 600
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

class Snake:
  def __init__(self):
    self.body_size = BODY_PARTS
    self.coordinates = []
    self.squares = []

    for i in range(0,BODY_PARTS):
      self.coordinates.append([0,0])
    
    for x,y in self.coordinates:
      square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
      self.squares.append(square)    

class Food:
  def __init__(self):

    # we are conceptually dividing game board into a grid where each cell is size of food item
    
    #if our height and width is 500 x 500, then if we divide by our food size 50 ,we have
    # 10 places or cells to put our food either on x axis or y axis, so we are getting random value out of
    # those 10 cells. and to get the pixel position we are multiplying with food size .so if 
    # to food place is 2nd cell then pixel position is 2*50 = 100 .On x axis it is 100 from left
    # every cell is filled with food
    x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
    y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
    
    self.coordinates = [x,y]
    # print('x is ',x)
    # print('y is',y)

    # we add space size so that our food is exactly based on the size we specified from
    canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")
    
def next_turn(snake,food):

  #unpacking 
  x, y = snake.coordinates[0]
  
  if direction == 'up':
    y -= SPACE_SIZE
  elif direction == 'down':
    y += SPACE_SIZE
  elif direction == 'left':
    x-= SPACE_SIZE
  elif direction == 'right':
    x+= SPACE_SIZE
  
  snake.coordinates.insert(0,(x,y))
  square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
  snake.squares.insert(0,square)

  if x == food.coordinates[0] and y == food.coordinates[1]:
    
    global score
    score += 1
    label.config(text='Score:{}'.format(score))

    canvas.delete("food")

    food = Food()

  else: 
    del snake.coordinates[-1]  
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

  if check_collisions(snake):
    game_over()
  else:
    # schedules function to execute after speed milli seconds.Here it is 50 ms similar to setTimeout
    window.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):
  global direction

  if new_direction == 'left':
    if direction != 'right': 
      direction = new_direction
  if new_direction == 'right':
    if direction != 'left':
      direction = new_direction
  if new_direction == 'up':
    if direction != 'down':
      direction = new_direction
  if new_direction == 'down':
    if direction != 'up':
      direction = new_direction  
    
def check_collisions(snake):

  x,y = snake.coordinates[0]  
  if x < 0 or x >= GAME_WIDTH:
    return True
  elif y < 0 or y >= GAME_HEIGHT:
    return True
  
  # if any of the body part coordinates matches(body collision)
  for body_part in snake.coordinates[1:]:
    if x == body_part[0] and y == body_part[1]:
      return True
  
def game_over():
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text='GAME OVER',fill='red',font=('consolas',50))



window = Tk() 
window.title('Snake game')
# window.resizable(False,False)

score = 0

# initial direction
direction = 'down'

label = Label(window,text="score:{}".format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window,height=GAME_HEIGHT,width=GAME_WIDTH,bg=BACKGROUND_COLOR)
canvas.pack()

window.update()

# get current width and height of the window
window_width = window.winfo_width()
window_height = window.winfo_height()

#get width and height of screen (computer)
screen_width = window.winfo_screenwidth()

screen_height = window.winfo_screenheight()



#calculate x and y coordinates to place window at starting position
#from half of the screen width subtracting half of the window width.same for height

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

# set window size and position it on the (x,y) coordinates
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda event:change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()