class Stats:
	def __init__(self, items):
		self.items = items
		self.reset()

	def reset(self) -> None:
		self.total_items = 0
		self.total_amount = 0
		self.average_amount = 0
		self.bought_amount = 0
		self.planned_amount = 0

	def update(self) -> None:
		self.reset()

		for item in self.items.values():
			if item.is_bought():
				self.bought_amount += item.price
			else:
				self.planned_amount += item.price

		self.total_items = len(self.items)
		self.total_amount = self.planned_amount + self.bought_amount
		self.average_amount = (
			self.total_amount / self.total_items
			if self.total_items > 0
			else 0
		)
