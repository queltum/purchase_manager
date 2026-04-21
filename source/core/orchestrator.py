from ui.views.forms import *
from tkinter import messagebox, filedialog
from ui.views import ItemsView, StatsView
from core.models import Items, Stats
from core.mappers import ItemMapper, StatsMapper
from core.provider import Provider

class Orchestrator:
	def __init__(
		self, 
		master
	):
		self.items = Items()
		self.stats = Stats(self.items)
		self.items_view = ItemsView(master)
		self.stats_view = StatsView(master, self.get_stats_data)

		self.add_form = AddForm(master, self.add_item)
		self.edit_form = EditForm(
			master, self.edit_item, self.get_item_data
		)
		self.filter_form = FilterForm(
			master, self.apply_filter, self.discard_filter
		)

	def show_add_form(self) -> None:
		self.add_form.show()

	def show_edit_form(self) -> None:
		self.edit_form.show()

	def show_filter_form(self) -> None:
		self.filter_form.show()

	def show_stats_window(self) -> None:
		self.stats.update()
		self.stats_view.show()

	def get_item_data(self):
		return ItemMapper.to_view(
			self.items[
				self.items_view.get_selection()
			]
		)

	def get_stats_data(self):
		return StatsMapper.to_view(
			self.stats
		)

	def add_item(self, data) -> None:
		item = ItemMapper.to_model(data)
		self.items_view.include(
			item.profile,
			self.items.include(item)
		)
		self.add_form.hide()
		self.stats.update()
		self.stats_view.update()

	def edit_item(self, data) -> None:
		item = ItemMapper.to_model(data)
		item_id = self.items_view.get_selection()
		self.items_view.replace(item.profile, item_id)
		self.items.replace(item, item_id)
		self.edit_form.hide()
		self.stats.update()
		self.stats_view.update()

	def apply_filter(self, data) -> None:
		self.discard_filter()

		for pid in self.items:
			item = self.items[pid]

			if (
				(data.category and item.category != data.category) or
				(data.status and item.status != data.status) or
				(data.date and item.date != data.date)
			):
				self.items_view.hide(pid)

	def discard_filter(self) -> None:
		for pid in self.items:
			self.items_view.show(pid)

	def remove_item(self) -> None:
		selected = self.items_view.get_selection()

		if messagebox.askyesno(
			"Confirmation", 
			"Do you really want to remove it?"
		):
			self.items.remove(selected)
			self.items_view.remove(selected)
			self.stats.update()
			self.stats_view.update()

	def mark_as_bought(self) -> None:
		item_id = self.items_view.get_selection()
		self.items[item_id].status = "bought"
		self.items_view.set_status(item_id, "bought")
		self.stats.update()
		self.stats_view.update()

	def mark_as_planned(self) -> None:
		item_id = self.items_view.get_selection()
		self.items[item_id].status = "planned"
		self.items_view.set_status(item_id, "planned")
		self.stats.update()
		self.stats_view.update()

	def load_data(self) -> None:
		path = filedialog.askopenfilename(
			title="Choose a file",
			filetypes=[
				("JSON files", "*.json"), 
				("All files", ".")
			]
		)

		if path:
			self.items_view.drop()
			self.items.snapshot = Provider.import_list(path)
			self.items_view.import_items(self.items.profile)
			self.items_view.apply_tags()

	def save_data(self) -> None:
		path = filedialog.asksaveasfilename(
			title="Save a file",
			defaultextension=".json",
			filetypes=[("JSON files", "*.json")]
		)

		if path:
			Provider.export_list(path, self.items.snapshot)