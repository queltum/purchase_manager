import json

class Provider:
	@staticmethod
	def import_list(path) -> dict:
		with open(path, "r", encoding="utf-8") as f:
			return json.load(f)

	@staticmethod
	def export_list(path, data) -> None:
		with open(path, "w", encoding="utf-8") as f:
			json.dump(data, f, ensure_ascii=False, indent=4)
