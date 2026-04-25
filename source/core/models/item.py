import config

class ItemSlot:
	def __init__(self, index):
		self.index = index

	def __get__(self, instance, owner):
		if instance is None:
			return self
		return instance[self.index]
	
	def __set__(self, instance, value):
		instance[self.index] = value

class Item(list):
	NAME = 0 
	CATEGORY = 1
	QUANTITY = 2
	UNIT_PRICE = 3
	PLANNED_DATE = 4
	STATUS = 5

	name = ItemSlot(NAME)
	category = ItemSlot(CATEGORY)
	quantity = ItemSlot(QUANTITY)
	unit_price = ItemSlot(UNIT_PRICE)
	planned_date = ItemSlot(PLANNED_DATE)
	status = ItemSlot(STATUS)

	def __init__(
		self, 
		name,
		category,
		quantity,
		unit_price,
		planned_date,
		status
	):
		super().__init__([
			name,
			category,
			quantity,
			unit_price,
			planned_date,
			status
		])

	def is_bought(self) -> bool:
		return self.status == config.BOUGHT

	@property
	def total_price(self) -> float:
		return self.quantity * self.unit_price

	@property
	def profile(self) -> tuple:
		return (
			self.name,
			self.category,
			self.quantity,
			self.unit_price,
			self.total_price,
			self.planned_date,
			self.status
		)
