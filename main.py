import pygame
from pygame.locals import *
from colors import Color

pygame.init()

color = Color()

# VARIÁVEIS DE VALOR CONSTANTE

LARGURA = 800
ALTURA = 600

# INICIANDO PROGRAMAÇÃO DO DISPLAY

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo de Damas')
pygame.font.init()
clock = pygame.time.Clock()

# TELA DO MENU
def menu_jogo():
	while True:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()

		display.fill(color.preto)
		fonte = pygame.font.SysFont('comicsansms', 50)
		surface_texto, rect_texto = text_objects("Jogo de Damas", fonte, color.branco)
		rect_texto.center = ((LARGURA / 2), ALTURA / 3)
		display.blit(surface_texto, rect_texto)

		cria_botao("INICIAR",(LARGURA - 760, ALTURA / 2, 120, 40), color.verde_claro, color.verde_escuro, color.branco, loop_jogo)
		cria_botao("MANUAL",(LARGURA - 560, ALTURA / 2, 120, 40), color.branco, color.cinza, color.preto, regras)
		cria_botao("CREDITOS",(LARGURA - 360, ALTURA / 2, 120, 40), color.branco, color.cinza, color.preto, creditos)
		cria_botao("SAIR",(LARGURA - 160, ALTURA / 2, 120, 40), color.verde_claro, color.vermelho, color.branco, sair)

		pygame.display.update()
		clock.tick(15)

# SAIR DO JOGO
def sair():
	pygame.quit()
	quit()

# FUNÇÕES AUXILIARES NO LOOP DO JOGO
def coluna_clicada(pos):
	x = pos[0]
	for i in range(1, 8):
		if x < i * ALTURA / 8:
			return i - 1
	return 7

def linha_clicada(pos):
	y = pos[1]
	for i in range(1, 8):
		if y < i * ALTURA / 8:
			return i - 1
	return 7

# LOOP DA TELA DO JOGO DE DAMAS
def loop_jogo():
	sair = False

	jogo = Jogo()

	while not sair:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				quit()
			if evento.type == pygame.MOUSEBUTTONDOWN:
				jogo.avalia_clique(pygame.mouse.get_pos())

		display.fill(color.preto)
		jogo.desenha()

		vencedor = jogo.verifica_vencedor()

		if vencedor is not None:
			sair = True
			tela_vencedor(vencedor)

		pygame.display.update()
		clock.tick(60)

menu_jogo()
pygame.quit()
quit()