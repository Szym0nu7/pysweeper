#Imports
import pygame
import random 
import bomb

MINE_IMG = pygame.image.load('assets/image-1.png')

# Define a function to check if the mouse is over a box
def is_mouse_over_box(mouse_pos, box_x, box_y, box_size):
    return box_x <= mouse_pos[0] <= box_x + box_size and \
           box_y <= mouse_pos[1] <= box_y + box_size
           
# Check if the mouse is over any of the boxes
def writeBoxes(boxes):
# Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    for i in range(len(boxes)):
        j = 0
        for box in boxes[i]:
            box_rect = pygame.Rect(box[0], box[1], box[2], box[3])
            if is_mouse_over_box(mouse_pos, box[0], box[1], box[2]):
                boxes[i][j] = (box[0], box[1], box[2], box[3], (0,255,0)) #green
            else:
                boxes[i][j] = (box[0], box[1], box[2], box[3], (255,255,255)) #white
            j = j+1
            
def generateBombs(boxes,SURFACE):
    BOMBAMOUNT = 1
    # for i in range(BOMBAMOUNT):
    #     cell =  boxes[random.randint(0,len(boxes))][random.randint(0,len(boxes[0]))]
    #     mine = bomb.Bomb(cell[cell[0], cell[1], cell[2], cell[3], MINE_IMG, SURFACE])
    #     mine.drawBombs()
    #     print("ey")
    #     return mine
        