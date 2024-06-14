class Bank:

  def init(self):
    self.score = 0

  def open_score(self):
    self.score = 0

  def close_score(self):
    if self.score != 0:
      print("Внимание! Счет уже закрыт.")
    else:
      self.score = 0

  def replenish(self, summ):
    if summ < 0:
      raise ValueError("Сумма пополнения не может быть отрицательной.")
    if self.score == 0:
      print("Внимание! Счет закрыт. Пополнение невозможно.")
    else:
      self.score += summ

  def take_off(self, summ):
    if summ < 0:
      raise ValueError("Сумма снятия не может быть отрицательной.")
    if self.score == 0:
      print("Внимание! Счет закрыт. Снятие невозможно.")
    elif summ > self.score:
      print("Внимание! Недостаточно средств на счете.")
    else:
      self.score -= summ