import turtle
import random

# Screen Setup
screen = turtle.Screen()
screen.title("Space Shooter Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off automatic screen updates for better performance

# Player (Spaceship)
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)  # Pointing upwards

# Player Movement
player_speed = 15

# Bullet Setup
bullets = []
bullet_speed = 100  

# Enemy Setup
enemies = []
enemy_speed = 10

# Score Setup
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 250)
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Functions to move the spaceship
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -390:
        x = -390
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 390:
        x = 390
    player.setx(x)

def shoot_bullet():
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.shapesize(stretch_wid=0.2, stretch_len=1)  # Bullet shape (elongated rectangle)
    bullet.setposition(player.xcor(), player.ycor() + 10)
    bullet.setheading(90)  # Shoot upwards
    bullets.append(bullet)

# Key bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(shoot_bullet, "space")

# Create enemies
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-380, 380)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    enemies.append(enemy)

# Move enemies
def move_enemies():
    global score
    for enemy in enemies:
        enemy.sety(enemy.ycor() - enemy_speed)
        # Check for collision with the player
        if enemy.ycor() < -250 and enemy.distance(player) < 20:
            game_over()
        # Check if the enemy goes off-screen
        if enemy.ycor() < -300:
            enemy.hideturtle()
            enemies.remove(enemy)
            create_enemy()
        
        # Check if the enemy is hit by a bullet
        for bullet in bullets:
            if bullet.distance(enemy) < 20:
                bullet.hideturtle()
                enemy.hideturtle()
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                update_score()
                create_enemy()

# Update the score on screen
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Game Over
def game_over():
    global score
    score_display.clear()
    score_display.goto(0, 0)
    score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 24, "normal"))
    screen.update()
    screen.bye()  # Closes the window

# Main game loop
def game_loop():
    move_enemies()

    # Move bullets
    for bullet in bullets:
        bullet.sety(bullet.ycor() + bullet_speed)
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullets.remove(bullet)

    screen.update()
    screen.ontimer(game_loop, 20)  # Continuously update the screen every 20ms

# Create initial enemies
for _ in range(5):  # Create 5 enemies
    create_enemy()

# Start the game loop
game_loop()

# Keep the window open
screen.mainloop()
















       

       



