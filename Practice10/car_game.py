import pygame, random

pygame.init()

W, H = 400, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = pygame.Rect(180, 500, 40, 60)
enemy = pygame.Rect(180, 0, 40, 60)

coins = []
coin_count = 0

font = pygame.font.Font(None, 36)

speed = 5
running = True
game_over = False   # жаңа айнымалы

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5

        # 🔒 экраннан шықпау
        if player.x < 0:
            player.x = 0
        if player.x > W - player.width:
            player.x = W - player.width

        # движение врага
        enemy.y += speed
        if enemy.y > H:
            enemy.y = 0
            enemy.x = random.randint(0, W - 40)

        # 💥 соғылу тексеру
        if player.colliderect(enemy):
            game_over = True

        # создаём монеты
        if random.randint(1, 100) == 1:
            coins.append(pygame.Rect(random.randint(0, W-20), 0, 20, 20))

        # движение монет
        for coin in coins[:]:
            coin.y += 5
            if player.colliderect(coin):
                coins.remove(coin)
                coin_count += 1
            elif coin.y > H:
                coins.remove(coin)

    # рисуем
    pygame.draw.rect(screen, (0,255,0), player)
    pygame.draw.rect(screen, (255,0,0), enemy)

    for coin in coins:
        pygame.draw.circle(screen, (255,215,0), coin.center, 10)

    text = font.render(f"Coins: {coin_count}", True, (255,255,255))
    screen.blit(text, (250, 10))

    # 🟥 Game Over шығару
    if game_over:
        over_text = font.render("GAME OVER", True, (255,0,0))
        screen.blit(over_text, (120, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()