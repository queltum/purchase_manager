import config
from tkinter import ttk

class NoSelectionError(Exception):
	pass

class ItemsView(ttk.Treeview):
	def __init__(self, master):
		super().__init__(
			master,
			columns=config.COLUMNS,
			show="headings",
			selectmode="browse"
		)

		self.scrollbar = ttk.Scrollbar(
			master,
			orient="vertical",
			command=self.yview
		)

		for column, width, anchor in zip(
			config.COLUMNS,
			config.WIDTHS, 
			config.ANCHORS
		):
			self.heading(column, text=column)
			self.column(column, width=width, anchor=anchor)
		self.configure(yscrollcommand=self.scrollbar.set)
		self.tag_configure("bought", background="lightgreen")
		self.tag_configure("planned", background="lightyellow")

		self.grid(
			row=0,
			column=0,
			sticky="nsew"
		)
		self.scrollbar.grid(
			row=0,
			column=1,
			sticky="ns"
		)

	def include(self, values, item_id) -> None:
		self.insert(
			"", 
			"end",
			iid=item_id,
			values=values,
			tags=(values[-1],)
		)

	def remove(self, item_id) -> None:
		self.delete(item_id)

	def replace(self, values, item_id) -> None:
		self.item(item_id, values=values, tag=(values[-1],))

	def hide(self, item_id) -> None:
		self.detach(item_id)

	def show(self, item_id) -> None:
		self.reattach(item_id, "", "end")

	def get_selection(self) -> str:
		selected = self.selection()

		if not selected:
			raise NoSelectionError("No item selected")
		return selected[0]

	def apply_tags(self) -> None:
		for item_id in self.get_children():
			self.item(
				item_id,
				tags=(self.item(
					item_id
				)["values"][-1],)
			)

	def drop(self) -> None:
		for item_id in self.get_children():
			self.delete(item_id)

	def import_items(self, items) -> None:
		for item_id in items:
			self.include(items[item_id], item_id)