import pygame
from pygame.locals import *
from colors import Color
from botao import Botao
from jogo import Jogo

pygame.init()

color = Color()
button = Botao()

# VARIÁVEIS DE VALOR CONSTANTE

LARGURA = 800
ALTURA = 600

# DEFINIR PADRÃO DE TEXTOS NA TELA
def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

# FUNÇÃO PARA IMPRIMIR AS REGRAS DO JOGO DE DAMAS
def regras():
	sair = False

	while not sair:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				quit()
			if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
				sair = True

		display.fill(color.preto)

		fonte = pygame.font.SysFont('comicsansms', 20)

		info1 = fonte.render('O jogo de damas eh praticado em um tabuleiro de 64 casas.', False, (color.azul))
		info2 = fonte.render('O objetivo do jogo eh capturar todas as pecas do oponente.', False, (color.verde_escuro))
		info3 = fonte.render('A peca anda soh para frente, uma casa de cada vez, na diagonal.', False, (color.verde_escuro))
		info4 = fonte.render('Quando a peca atinge a oitava linha do tabuleiro ela vira dama.', False, (color.verde_escuro))
		info5 = fonte.render('A dama eh uma peca de movimentos mais amplos. Ela anda para frente e para tras,', False, (color.azul))
		info6 = fonte.render('quantas casas quiser, nao podendo saltar sobre uma peca da mesma cor. ', False, (color.azul))
		info7 = fonte.render('A captura e obrigatoria, ou seja, nao existe sopro.', False, (color.verde_escuro))
		info8 = fonte.render('Duas ou mais pecas juntas, na mesma diagonal, nao podem ser capturadas.', False, (color.verde_escuro))
		info9 = fonte.render('A peca e a dama podem capturar tanto para frente como para tras.', False, (color.azul))
		info10 = fonte.render('O movimento de captura pode ser encadeado sem que o jogador passe a vez.', False, (color.azul))
		
		game1 = fonte.render('Durante o jogo, ao clicar em uma peca, sera exibido em verde os movimentos', False, (color.vermelho))
		game2 = fonte.render('possiveis da mesma. Se nada acontecer ao clicar em uma peca, significa que', False, (color.vermelho))
		game3 = fonte.render('ela nao tem movimentos possiveis ou o turno pertence ao outro jogador.', False, (color.vermelho))

		voltar = fonte.render('Pressione qualquer tecla para voltar ao menu.', False, color.verde_claro)

		display.blit(info1, (5, 65))
		display.blit(info2, (5, 95))
		display.blit(info3, (5, 115))
		display.blit(info4, (5, 145))
		display.blit(info5, (5, 165))
		display.blit(info6, (5, 195))
		display.blit(info7, (5, 215))
		display.blit(info8, (5, 245))
		display.blit(info9, (5, 265))
		display.blit(info10, (5, 295))
		
		display.blit(game1, (5, 315))
		display.blit(game2, (5, 335))
		display.blit(game3, (5, 360))
		display.blit(voltar, (25, 550))

		pygame.display.update()
		clock.tick(60)

# FUNÇÃO PARA IMPRIMIR OS CRÉDITOS
def creditos():
	sair = False
	while not sair:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()
			if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
				sair = True

		display.fill(color.preto)
		fonte = pygame.font.SysFont('comicsansms', 20)
		surface_texto, rect_texto = text_objects("Programador: Lucas de Medeiros", fonte, color.branco)
		rect_texto.center = ((LARGURA / 2), ALTURA / 3)
		display.blit(surface_texto, rect_texto)

		surface_texto, rect_texto = text_objects("Disciplina: Programacao 1 / Laboratorio de Programacao 1", fonte, color.branco)
		rect_texto.center = ((LARGURA / 2), ALTURA / 2.7)
		display.blit(surface_texto, rect_texto)

		surface_texto, rect_texto = text_objects("Versao Python: 2.7.x", fonte, color.vermelho_claro)
		rect_texto.center = ((LARGURA / 2), ALTURA / 1.5)
		display.blit(surface_texto, rect_texto)

		surface_texto, rect_texto = text_objects("Versao Pygame: 1.9.1", fonte, color.vermelho_claro)
		rect_texto.center = ((LARGURA / 2), ALTURA / 1.3)
		display.blit(surface_texto, rect_texto)

		voltar = fonte.render('Pressione qualquer tecla para voltar ao menu.', False, color.verde_escuro)
		display.blit(voltar, (25, 550))

		pygame.display.update()
		clock.tick(15)

# FUNÇÃO PARA IMPRIMIR A TELA DO VENCEDOR
def tela_vencedor(vencedor):
	sair = False

	while not sair:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				quit()
			if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
				sair = True

		display.fill(color.preto)

		fonte = pygame.font.SysFont('comicsansms', 50)

		surface_texto, rect_texto = None, None

		if vencedor == "empate":
			surface_texto, rect_texto = text_objects("EMPATE!", fonte, color.branco)
		elif vencedor == "x":
			surface_texto, rect_texto = text_objects("VITORIA DO  VERMELHO", fonte, color.vermelho)
		elif vencedor == "o":
			surface_texto, rect_texto = text_objects("VITORIA DO BRANCO", fonte, color.branco)

		rect_texto.center = ((LARGURA / 2), ALTURA / 3)
		display.blit(surface_texto, rect_texto)

		fonte = pygame.font.Font(None, 30)
		voltar = fonte.render('Pressione qualquer tecla para voltar ao menu.', False, color.verde_claro)

		display.blit(voltar, (25, 550))

		pygame.display.update()
		clock.tick(60)

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

		display.fill(color.cinza)
		fonte = pygame.font.SysFont('comicsansms', 50)
		surface_texto, rect_texto = text_objects("Jogo de Damas", fonte, color.branco)
		rect_texto.center = ((LARGURA / 2), ALTURA / 3)
		display.blit(surface_texto, rect_texto)

		button.cria_botao("INICIAR",(LARGURA - 760, ALTURA / 2, 120, 40), color.verde_claro, color.verde_escuro, color.branco, display,loop_jogo)
		button.cria_botao("MANUAL",(LARGURA - 560, ALTURA / 2, 120, 40), color.branco, color.cinza, color.preto, display,regras)
		button.cria_botao("CREDITOS",(LARGURA - 360, ALTURA / 2, 120, 40), color.branco, color.cinza, color.preto, display,creditos)
		button.cria_botao("SAIR",(LARGURA - 160, ALTURA / 2, 120, 40), color.vermelho_claro, color.vermelho, color.branco, display,sair)

		pygame.display.update()
		clock.tick(15)

# SAIR DO JOGO
def sair():
	pygame.quit()
	quit()

# LOOP DA TELA DO JOGO DE DAMAS
def loop_jogo():
	sair = False

	game = Jogo()

	while not sair:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				quit()
			if evento.type == pygame.MOUSEBUTTONDOWN:
				game.avalia_clique(pygame.mouse.get_pos())

		display.fill(color.preto)
		game.desenha()

		vencedor = game.verifica_vencedor()

		if vencedor is not None:
			sair = True
			tela_vencedor(vencedor)

		pygame.display.update()
		clock.tick(60)

menu_jogo()
pygame.quit()
quit()