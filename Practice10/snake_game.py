import pygame, random

pygame.init() 

W, H = 600, 600
screen = pygame.display.set_mode((W, H))  
clock = pygame.time.Clock()  

snake = [(300,300)]   # initial snake position 
dx, dy = 20, 0        # movement direction

# initial food 
food = (random.randint(0,29)*20, random.randint(0,29)*20)

score = 0  
level = 1   
speed = 10  

font = pygame.font.Font(None, 36)     
big_font = pygame.font.Font(None, 72) 

def new_food():
    # generate new food that is not inside the snake body
    while True:
        f = (random.randint(0,29)*20, random.randint(0,29)*20)
        if f not in snake:
            return f

def draw_grid():
    # draw grid lines for better movement visibility
    for x in range(0, W, 20):
        pygame.draw.line(screen, (40,40,40), (x,0), (x,H))
    for y in range(0, H, 20):
        pygame.draw.line(screen, (40,40,40), (0,y), (W,y))

running = True
game_over = False  

while running:
    screen.fill((15,15,15))  # background color
    draw_grid()              # draw grid

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # exit game

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -20
            if event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 20
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -20, 0
            if event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 20, 0

    if not game_over:
        # new head position
        head = (snake[0][0] + dx, snake[0][1] + dy)

        # wall collision check
        if head[0] < 0 or head[0] >= W or head[1] < 0 or head[1] >= H:
            game_over = True

        # self collision check
        if head in snake:
            game_over = True

        snake.insert(0, head)  # add new head

        # check if food is eaten
        if head == food:
            score += 1
            food = new_food()

            # increase level every 3 points
            if score % 3 == 0:
                level += 1
                speed += 2  # increase game speed
        else:
            snake.pop()  # remove tail

    # draw snake
    for i, s in enumerate(snake):
        if i == 0:
            # snake head
            pygame.draw.rect(screen, (0,255,150), (*s,20,20))
        else:
            pygame.draw.rect(screen, (0,200,0), (*s,20,20))

    # draw food (circle)
    pygame.draw.circle(screen, (255,50,50), (food[0]+10, food[1]+10), 10)

   
    text = font.render(f"Score: {score}   Level: {level}", True, (200,200,200))
    screen.blit(text, (10,10))

    
    if game_over:
        over = big_font.render("GAME OVER", True, (255,50,50))
        screen.blit(over, (120,250))

    pygame.display.flip()  
    clock.tick(speed)     

pygame.quit()  