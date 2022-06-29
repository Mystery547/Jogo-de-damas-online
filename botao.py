import pygame

class Botao():
  def __ini__(self):
    pass



# FUNÇÃO PARA CRIAR UM BOTÃO
def cria_botao(msg, sqr, cor1, cor2, cor_texto, acao=None):
	mouse = pygame.mouse.get_pos()
	clique = pygame.mouse.get_pressed()

	if sqr[0] + sqr[2] > mouse[0] > sqr[0] and sqr[1] + sqr[3] > mouse[1] > sqr[1]:
		pygame.draw.rect(display, cor2, sqr)
		if clique[0] == 1 and acao != None:
			acao()
	else:
		pygame.draw.rect(display, cor1, sqr)

	fontePequena = pygame.font.SysFont('comicsansms', 20)
	surface_texto, rect_texto = text_objects(msg, fontePequena, cor_texto)
	rect_texto.center = (sqr[0] + 60, sqr[1] + 20)
	display.blit(surface_texto, rect_texto)