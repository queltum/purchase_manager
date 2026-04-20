import config
import tkinter as tk

from tkinter import ttk
from ui.framework import BaseForm
from ui.views.view_data import ItemData

class AddForm(BaseForm):
	TITLE = config.ADD_FORM_TITLE
	ICON = "ui/icons/AddForm.ico"

	def __init__(self, master, on_submit):
		super().__init__(master, on_submit)

	def reset(self) -> None:
		self.name_ent.delete(0, tk.END)
		self.category_cbx.set("")
		self.quantity_ent.delete(0, tk.END)
		self.unit_price_ent.delete(0, tk.END)

	def collect(self) -> ItemData:
		return ItemData(
			name=self.name_ent.get(),
			category=self.category_cbx.get(),
			quantity=self.quantity_ent.get(),
			unit_price=self.unit_price_ent.get()
		)

	def create_widgets(self) -> None:
		self.name_lbl = tk.Label(
			self.window, 
			text=config.ITEM_NAME_TITLE
		)
		self.category_lbl = tk.Label(
			self.window, 
			text=config.ITEM_CATEGORY_TITLE
		)
		self.quantity_lbl = tk.Label(
			self.window, 
			text=config.ITEM_QUANTITY_TITLE
		)
		self.unit_price_lbl = tk.Label(
			self.window, 
			text=config.ITEM_UNIT_PRICE_TITLE
		)

		self.name_ent = tk.Entry(self.window)
		self.quantity_ent = tk.Entry(self.window)
		self.unit_price_ent = tk.Entry(self.window)
		self.category_cbx = ttk.Combobox(
			self.window, values=config.CATEGORIES
		)
		self.submit_btn = tk.Button(
			self.window,
			text="Submit",
			command=self.submit
		)

	def layout_widgets(self) -> None:
		self.name_lbl.grid(
			row=0, column=0, sticky="ew"
		)
		self.category_lbl.grid(
			row=1, column=0, sticky="ew"
		)
		self.quantity_lbl.grid(
			row=2, column=0, sticky="ew"
		)
		self.unit_price_lbl.grid(
			row=3, column=0, sticky="ew"
		)

		self.name_ent.grid(
			row=0, 
			column=1, 
			sticky="ew",
			padx=4,
			pady=4
		)
		self.category_cbx.grid(
			row=1,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.quantity_ent.grid(
			row=2,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.unit_price_ent.grid(
			row=3,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.submit_btn.grid(
			row=4,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)

