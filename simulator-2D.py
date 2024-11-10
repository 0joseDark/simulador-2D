import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulador 2D de Cubos")

# Configurações do cenário
cor_fundo = (30, 30, 30)
velocidade_cenario = 5
offset_x, offset_y = 0, 0  # Posição inicial do cenário

# Lista para armazenar os cubos
cubos = []

# Configurações dos cubos
tamanho_cubo = 30
cor_cubo = (200, 100, 50)
cubo_selecionado = None

# Função para desenhar cubos
def desenhar_cubos():
    for cubo in cubos:
        pygame.draw.rect(tela, cor_cubo, (cubo[0] + offset_x, cubo[1] + offset_y, tamanho_cubo, tamanho_cubo))

# Loop principal do jogo
rodando = True
while rodando:
    tela.fill(cor_fundo)

    # Captura eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Criação de um novo cubo com o clique do botão direito
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo para mover/selecionar
                x, y = evento.pos
                for cubo in cubos:
                    # Verifica se o clique foi em um cubo existente
                    if cubo[0] + offset_x <= x <= cubo[0] + offset_x + tamanho_cubo and cubo[1] + offset_y <= y <= cubo[1] + offset_y + tamanho_cubo:
                        cubo_selecionado = cubo
                        break
            elif evento.button == 3:  # Botão direito para criar um cubo
                x, y = evento.pos
                novo_cubo = (x - offset_x, y - offset_y)
                cubos.append(novo_cubo)

        # Liberação do botão do rato para soltar o cubo
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                cubo_selecionado = None

        # Apaga um cubo com o clique do botão do meio
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 2:
            x, y = evento.pos
            for cubo in cubos:
                if cubo[0] + offset_x <= x <= cubo[0] + offset_x + tamanho_cubo and cubo[1] + offset_y <= y <= cubo[1] + offset_y + tamanho_cubo:
                    cubos.remove(cubo)
                    break

    # Movendo o cubo selecionado com o rato
    if cubo_selecionado:
        x, y = pygame.mouse.get_pos()
        cubo_selecionado = (x - offset_x - tamanho_cubo // 2, y - offset_y - tamanho_cubo // 2)
        cubos[cubos.index(cubo_selecionado)] = cubo_selecionado

    # Movimento do cenário com as teclas de setas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        offset_x += velocidade_cenario
    if teclas[pygame.K_RIGHT]:
        offset_x -= velocidade_cenario
    if teclas[pygame.K_UP]:
        offset_y += velocidade_cenario
    if teclas[pygame.K_DOWN]:
        offset_y -= velocidade_cenario

    # Desenha os cubos na tela
    desenhar_cubos()
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()
