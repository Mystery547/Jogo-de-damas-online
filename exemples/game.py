class Game:
  def __init__(self, id) -> None:
    self.p1Went = False
    self.p2Went = False
    self.ready = False
    self.id = id
    self.moves = [None, None]
    self.wins = [0, 0]
    self.ties = 0
  
  def getPlayerMove(self, p):
    """
    :param p: 0 or 1
    :return: Move
    """
    return self.moves[p]

  def player(self, player, move):
    pass
