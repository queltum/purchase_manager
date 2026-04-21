from core.models import Stats
from ui.views.view_data import StatsData
from core.mappers import BaseMapper

class StatsMapper(BaseMapper):
	@staticmethod
	def to_view(model: Stats) -> StatsData:
		return StatsData(
			f"Total items: {model.total_items}",
			f"Total amount: {model.total_amount}",
			f"Average amount: {model.average_amount}",
			f"Bought amount: {model.bought_amount}",
			f"Planned amount: {model.planned_amount}"
		)

	# todo
	@staticmethod
	def to_model(data: StatsData) -> None:
		pass