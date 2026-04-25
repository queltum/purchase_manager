import config
import tkinter as tk

from tkinter import ttk
from ui.framework import BaseForm
from ui.views.view_data import ItemData

class FilterForm(BaseForm):
	TITLE = config.FILTER_FORM_TITLE
	ICON = "ui/icons/FilterForm.ico"

	def __init__(self, master, on_submit, on_discard):
		self.on_discard = on_discard
		super().__init__(master, on_submit)

	def collect(self) -> ItemData:
		return ItemData(
			category=self.category_cbx.get(),
			status=self.status_cbx.get(),
			planned_date=self.planned_date_ent.get()
		)

	def on_hide(self) -> None:
		self.on_discard()

	def reset(self) -> None:
		self.category_cbx.set("")
		self.status_cbx.set("")
		self.planned_date_ent.delete(0, tk.END)

	def create_widgets(self) -> None:
		self.category_lbl = tk.Label(
			self.window, 
			text=config.ITEM_CATEGORY_TITLE
		)
		self.status_lbl = tk.Label(
			self.window,
			text=config.ITEM_STATUS_TITLE
		)
		self.planned_date_lbl = tk.Label(
			self.window,
			text=config.ITEM_DATE_TITLE
		)

		self.category_cbx = ttk.Combobox(
			self.window, values=config.CATEGORIES
		)
		self.status_cbx = ttk.Combobox(
			self.window, values=config.STATUSES
		)
		self.planned_date_ent = tk.Entry(self.window)

		self.discard_btn = tk.Button(
			self.window,
			text="Discard",
			command=self.on_discard
		)

		self.submit_btn = tk.Button(
			self.window,
			text="Apply",
			command=self.submit
		)

	def layout_widgets(self) -> None:
		self.category_lbl.grid(
			row=0,
			column=0,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.status_lbl.grid(
			row=1,
			column=0,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.planned_date_lbl.grid(
			row=2,
			column=0,
			sticky="ew",
			padx=4,
			pady=4
		)

		self.category_cbx.grid(
			row=0,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.status_cbx.grid(
			row=1,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.planned_date_ent.grid(
			row=2,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.discard_btn.grid(
			row=3,
			column=0,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.submit_btn.grid(
			row=3,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)