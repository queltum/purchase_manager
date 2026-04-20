from core.models import Stats
from ui.views.view_data import StatsData
from core.mappers import BaseMapper

class StatsMapper(BaseMapper):
	@staticmethod
	def to_view(model: Stats) -> StatsData:
		return StatsData(
			str(model.total_items),
			str(model.total_amount),
			str(model.average_amount),
			str(model.bought_amount),
			str(model.planned_amount)
		)

	@staticmethod
	def to_model(view: StatsData) -> Stats:
		return Stats(
			float(view.total_items),
			float(view.total_amount),
			float(view.average_amount),
			float(view.bought_amount),
			float(view.planned_amount)
		)