import tkinter as tk
import random

# Game window setup
root = tk.Tk()
root.title("Alien Invasion Game")
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

# Player setup
player = canvas.create_polygon(290, 550, 310, 550, 300, 530, fill="white")

# Alien setup
alien_x = random.randint(50, 550)
alien = canvas.create_oval(alien_x, 50, alien_x + 20, 70, fill="red")

# Bullet setup
bullets = []

# Movement functions
def move_left(event):
    canvas.move(player, -20, 0)

def move_right(event):
    canvas.move(player, 20, 0)

def shoot(event):
    player_coords = canvas.coords(player)
    bullet = canvas.create_rectangle(player_coords[0] + 5, 520, player_coords[0] + 15, 530, fill="yellow")
    bullets.append(bullet)
    move_bullets()

def move_bullets():
    global bullets
    for bullet in bullets[:]:
        canvas.move(bullet, 0, -10)
        bullet_coords = canvas.coords(bullet)
        alien_coords = canvas.coords(alien)
        
        if bullet_coords and alien_coords:
            if (alien_coords[0] < bullet_coords[0] < alien_coords[2] and
                alien_coords[1] < bullet_coords[1] < alien_coords[3]):
                canvas.delete(alien)
                canvas.delete(bullet)
                bullets.remove(bullet)
                reset_alien()
                return
        
        if bullet_coords[1] <= 0:
            canvas.delete(bullet)
            bullets.remove(bullet)
    
    if bullets:
        root.after(50, move_bullets)

def reset_alien():
    global alien
    alien_x = random.randint(50, 550)
    alien = canvas.create_oval(alien_x, 50, alien_x + 20, 70, fill="red")

# Keyboard bindings
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", shoot)

# Run the game loop
root.mainloop()