from core.models import Item
from core.mappers import BaseMapper
from ui.views.view_data import ItemData

class ItemMapper(BaseMapper):
	@staticmethod
	def to_model(
		data: ItemData
	) -> Item:
		return Item(
			data.name,
			data.category,
			data.quantity,
			data.unit_price,
			data.status,
			data.date
		)

	@staticmethod
	def to_view(
		item: Item
	) -> ItemData:
		return ItemData(
			name=item.name,
			category=item.category,
			quantity=item.quantity,
			unit_price=item.unit_price,
			status=item.status,
			date=item.date
		)