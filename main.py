#Imports
import pygame
import random
import writeGrid

# Set the box properties
box_size = 36
num_boxes_x = 20
num_boxes_y = 20
boxes = []

# Set the screen size
screen_width = box_size*num_boxes_x + num_boxes_x
screen_height = box_size*num_boxes_y + num_boxes_y
screen = pygame.display.set_mode((screen_width, screen_height))



for i in range(num_boxes_y):
    boxes.append([])
    for j in range(num_boxes_x):
        box_x = i+i* box_size #(i *1.1)+i *1.1  * box_size
        box_y = j+j* box_size#(j *1.1)+j *1.1  * box_size 
        box_color = (0,0,0)
        boxes[i].append((box_x, box_y, box_size, box_size, box_color))

mine = writeGrid.generateBombs(boxes,screen)

# Set up the game loop
running = True
FPS = 60
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    writeGrid.writeBoxes(boxes)
    
    
    
    # Draw the boxes
    screen.fill((240, 240, 240)) # White background
    for i in range(len(boxes)):
        for box in boxes[i]:
            pygame.draw.rect(screen, box[4], (box[0], box[1], box[2], box[3]))
          
    
    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()