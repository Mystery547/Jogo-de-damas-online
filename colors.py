class Color():
  __PRETO = (0, 0, 0)
  __BRANCO = (255, 255, 255)
  __CINZA = (100, 100, 100)
  __VERMELHO = (120, 0, 0)
  __VERDE_ESCURO = (0, 120, 0)
  __VERDE_CLARO = (0, 255, 0)
  __VERMELHO_CLARO = (255, 0, 0)
  __AZUL = (0, 0, 255)
  __COR_FUNDO = (54, 54, 54)
  __COR_TABULEIRO = (0, 31, 0)

  def __init__(self) -> None:
    self.__preto = self.__class__.__PRETO
    self.__branco = self.__class__.__BRANCO
    self.__cinza = self.__class__.__CINZA
    self.__vermelho = self.__class__.__VERMELHO
    self.__verde_escuro = self.__class__.__VERDE_ESCURO
    self.__verde_claro = self.__class__.__VERDE_CLARO
    self.__vermelho_claro = self.__class__.__VERMELHO_CLARO
    self.__azul = self.__class__.__AZUL
    self.__cor_fundo = self.__class__.__COR_FUNDO
    self.__cor_tabuleiro = self.__class__.__COR_TABULEIRO
  
  @property
  def preto(self):
    return self.__preto
  
  @property
  def branco(self):
    return self.__branco
  
  @property
  def cinza(self):
    return self.__cinza
  
  @property
  def vermelho(self):
    return self.__vermelho

  @property
  def verde_escuro(self):
    return self.__verde_escuro
  
  @property
  def verde_claro(self):
    return self.__verde_claro
  
  @property
  def vermelho_claro(self):
    return self.__vermelho_claro
  
  @property
  def azul(self):
    return self.__azul
  
  @property
  def cor_fundo(self):
    return self.__cor_fundo
  
  @property
  def cor_tabuleiro(self):
    return self.__cor_tabuleiro
  