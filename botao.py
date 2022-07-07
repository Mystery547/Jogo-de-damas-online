import pygame

# DEFINIR PADRÃO DE TEXTOS NA TELA
def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

class Botao():
  def __init__(self):
    pass

  def cria_botao(self, msg, sqr, cor1, cor2, cor_texto, display,acao=None):
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