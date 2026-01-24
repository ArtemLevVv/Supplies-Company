import modules, pygame, game

game.screen.fill((100, 255, 0))

modules.init_data()
game.init_data()

plyer = game.Player()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            print(x, y)
        if keys[pygame.K_ESCAPE]:
            run = False
        plyer.movement(keys= keys)
    game.screen.fill((100, 255, 0))
    plyer.blit_sprite(game.screen)
    game.draw_world(['0', '01', '10', '11'], game.screen)
    pygame.display.update()
pygame.quit()