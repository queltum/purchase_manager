from datetime import datetime

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
	NAME, CATEGORY, QUANTITY, UNIT_PRICE, STATUS, DATE = range(6)

	name = ItemSlot(NAME)
	category = ItemSlot(CATEGORY)
	quantity = ItemSlot(QUANTITY)
	unit_price = ItemSlot(UNIT_PRICE)
	status = ItemSlot(STATUS)
	date = ItemSlot(DATE)

	def __init__(
		self, 
		name,
		category,
		quantity,
		unit_price,
		status="planned",
		date=""
	):
		super().__init__([
			name,
			category,
			quantity,
			unit_price,
			status,
			date
		])

	def is_bought(self) -> bool:
		return self.status == "bought"

	def set_status(self, status) -> None:
		if status == "bought":
			self.date = datetime.now().strftime("%d/%m/%Y")
		self.status = status

	@property
	def price(self) -> float:
		return str(
			float(self.quantity) * float(self.unit_price)
		)

	@property
	def profile(self) -> tuple:
		return (
			self.name, 
			self.quantity, 
			self.price, 
			self.status
		)
