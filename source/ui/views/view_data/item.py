from typing import Optional

class ItemData:
	def __init__(
		self,
		*,
		name: Optional[str]=None,
		category: Optional[str]=None,
		quantity: Optional[int]=None,
		unit_price: Optional[str]=None,
		planned_date: Optional[str]=None,
		status: Optional[str]=None,
	):
		self.name = name
		self.category = category
		self.quantity = quantity
		self.unit_price = unit_price
		self.planned_date = planned_date
		self.status = status