# Import a library of functions called 'pygame'
import pygame
import random
# Initialize the game engine
pygame.init()
black = [ 0, 0, 0]
#Colors used in this game
white = [255,255,255]
green=[0,255,0]
#set the music
music=pygame.mixer.Sound("song.wav")
#music.play()
#Specify the comments display on the screen after the game 
basicfont=pygame.font.Font('freesansbold.ttf',32)
gameover=basicfont.render("GAME OVER",1,green)
gameoverrect=gameover.get_rect()
#Display the result on the screen
scoreboard=pygame.font.Font(None,32)
# Set the height and width of the screen
screen = pygame.display.set_mode([600, 500])
pygame.display.set_caption("Point collection")
#coordinates
x_coord=0
y_coord=250
clock = pygame.time.Clock()
#create lists
atkr=[]
point=[] 
atkb=[]
# Loop 10 times and add a images in a random x,y position
for i in range(10):
    x=random.randrange(200,600)
    y=random.randrange(0,500)
    atkr.append([x,y])
for i in range(5):
    x=random.randrange(0,600)
    y=random.randrange(0,500)
    point.append([x,y])
for i in range(10):
    x=random.randrange(0,600)
    y=random.randrange(0,500)
    atkb.append([x,y])
#Loop until the user clicks the close button.
done=False
move_x=0
move_y=0
score=0
while done==False:
    music.play()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # Ketboard used to control the player in left,right,top and bottom
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x=-3             
            if event.key == pygame.K_RIGHT:
                move_x= 3
            if event.key==pygame.K_UP:
                move_y=-3
	    if event.key==pygame.K_DOWN:	
		move_y=3				
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                move_x=0
	    if event.key==pygame.K_RIGHT:
                move_x=0
            if event.key==pygame.K_UP:
                move_y=0
            if event.key==pygame.K_DOWN:
		move_y=0                               
#Move the object according to the speed vector.
    x_coord=x_coord+move_x
    y_coord=y_coord+move_y
    screen.fill(black)
# Create player 
    player=pygame.image.load("man.jpg").convert()
    screen.blit(player,[x_coord,y_coord])
    rect1=pygame.Rect(x_coord,y_coord,25,35)
    player.set_colorkey(black)
# Process each atkr in the list
    for i in range(len(atkr)):
        atkr_img=pygame.image.load("im.gif").convert()
        screen.blit(atkr_img,atkr[i])
        # Move the atkr left three pixel
        atkr[i][0]-=3
        if rect1.collidepoint(atkr[i][0],atkr[i][1]):
	    score=score-1
            y=random.randrange(0,500)
            atkr[i][1]=y
            x=random.randrange(590,600)
            atkr[i][0]=x      
        # If the atkr has moved off the left of the screen
        if atkr[i][0] <0:
            # Reset it just right of the screen
            y=random.randrange(0,500)
            atkr[i][1]=y
            x=random.randrange(590,600)
            atkr[i][0]=x           
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Process each point list elements
    for i in range(len(point)):
        point_img=pygame.image.load("b2-17.png").convert()
        screen.blit(point_img,point[i])
        # Move the point image down three pixel
        point[i][1]+=3
      	if rect1.collidepoint(point[i][0],point[i][1]):
            score=score+1
            y=random.randrange(-500,-10)
            point[i][1]=y
            x=random.randrange(0,600)
            point[i][0]=x
        # If the image has moved off the bottom of the screen
        if point[i][1] > 500:
            # Reset it just above the top
            y=random.randrange(-500,-10)
            point[i][1]=y
            # Give it a new x position
            x=random.randrange(0,600)
            point[i][0]=x
    for i in range(len(atkb)):
        atkb_img=pygame.image.load("alien.png").convert()
        screen.blit(atkb_img,atkb[i])
        atkb_img.set_colorkey(white)
        # Move the image top three pixel
        atkb[i][1]-=3        
        if rect1.collidepoint(atkb[i][0],atkb[i][1]):
            score=score-1
            y=random.randrange(490,500)
            atkb[i][1]=y
            x=random.randrange(0,600)
            atkb[i][0]=x
        # If the imaged has moved off the top of the screen
        if atkb[i][1] <0:
            # Reset it to the new position
            y=random.randrange(490,500)
            atkb[i][1]=y
            x=random.randrange(0,600)
            atkb[i][0]=x
    screen.blit(scoreboard.render("score"+str(score),4,white),[40,40])
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    
    clock.tick(20)
    if score<-2:
        screen.blit(gameover,gameoverrect)
        pygame.display.flip()
        done=True   
pygame.quit ()
