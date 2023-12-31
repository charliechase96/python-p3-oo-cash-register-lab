#!/usr/bin/env python3

class CashRegister():

  def __init__(self, cash_register_with_discount=False, discount=None):
    if discount is None:
      if cash_register_with_discount:
        self.discount = 20
      else:
        self.discount = 0
    else:
      self.discount = discount

    self.total = 0.00
    self.items = []
    self.transactions = []
  
  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    self.items.extend([title] * quantity)

    self.title = title

    self.transactions.append((title, price, quantity))
  
  def void_last_transaction(self):
    if self.transactions:
      last_transaction = self.transactions.pop(-1)

      title, price, quantity = last_transaction

      self.total -= price * quantity

      for _ in range(quantity):
        self.items.remove(title)
      

  def apply_discount(self, cash_register_with_discount=True):
    if cash_register_with_discount:
      if self.discount > 0:
        discounted_total = self.total * (1 - (self.discount / 100.0))
        self.total = discounted_total
        print(f"After the discount, the total comes to ${int(discounted_total)}.")
      else:
        print(f"There is no discount to apply.")