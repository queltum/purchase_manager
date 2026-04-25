from core.models import Item

class Items(dict):
	def __init__(self):
		super().__init__()
		self._id_cnt = -1

	def _get_next_item_id(self) -> str:
		self._id_cnt += 1
		return f"item_{self._id_cnt}"

	def include(self, item: Item) -> str:
		item_id = self._get_next_item_id()
		self[item_id] = item
		return item_id

	def set_status(self, item_id, status) -> None:
		self[item_id].status = status

	def replace(self, item: Item, item_id) -> None:
		self[item_id] = item

	def remove(self, item_id) -> None:
		del self[item_id]

	@property
	def profile(self) -> dict:
		return {
			item_id: item.profile
			for item_id, item in self.items()
		}

	@property
	def snapshot(self) -> dict:
		return {
			"id_cnt": self._id_cnt,
			"items": self
		}

	@snapshot.setter
	def snapshot(self, snapshot) -> None:
		self._id_cnt = snapshot["id_cnt"]
		self.clear()
		self.update({
			item_id: Item(*item)
			for item_id, item in snapshot["items"].items()
		})
