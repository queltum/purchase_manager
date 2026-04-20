from typing import Optional

class ItemData:
	def __init__(
		self,
		*,
		name: Optional[str]=None,
		category: Optional[str]=None,
		quantity: Optional[str]=None,
		unit_price: Optional[str]=None,
		status: Optional[str]="planned",
		date: Optional[str]=None
	):
		self.name = name
		self.category = category
		self.quantity = quantity
		self.unit_price = unit_price
		self.status = status
		self.date = date