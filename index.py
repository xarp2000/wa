import pygame, random

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

azul = (122, 122, 255)
vermelho = (255, 100, 0)

executando = True

tiros = []
velocidade_tiro = 5

jogador_altura = 30
jogador_largura = 30
jogador_x = 400
jogador_y = 480
jogador_cor = (166, 214, 76)
velocidade_jogador = 0.5

#enemy
enemy_altura = 30
enemy_largura = 30
enemy_cor = (178, 48, 52)
velocidade_enemy = 3
enemies = []
contador_geração_enemy = 0
quantidade_enemy = 5

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x = jogador_x - velocidade_jogador
    
    if teclas[pygame.K_RIGHT] and jogador_x < largura:
        jogador_x = jogador_x + velocidade_jogador
    
    if teclas[pygame.K_SPACE]:
        tiros.append([jogador_x + jogador_largura // 2 - 2, jogador_y])

    novo_inimigo_x = random.randint(0, largura - enemy_largura)
    novo_inimigo_y = random.randint(-50, -10)
    enemies.append([novo_inimigo_x, novo_inimigo_y])

    print(enemies)
    
    for tiro in tiros[:]:
        tiro[1] = tiro[1] - 5
        if tiro[1] < 0:
            tiros.remove(tiro)
        
    for enemy in enemies:
        pygame.draw.rect(tela, enemy_cor, (enemy[0], enemy[1], enemy_altura, enemy_largura))

    for enemy in enemies[:]:
        enemy[1] = enemy[1] + velocidade_enemy
        if enemy[1] > altura:
            enemies.remove(enemy)

    tela.fill(azul)
    pygame.draw.rect(tela, jogador_cor, (jogador_x, jogador_y, jogador_largura, jogador_altura))

    #desenho de tiro na tela
    for tiro in tiros:
        pygame.draw.rect(tela, vermelho, (tiro[0], tiro[1], 4, 10))
    pygame.display.flip()
pygame.quit()