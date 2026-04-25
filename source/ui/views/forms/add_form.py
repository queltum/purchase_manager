import config
import tkinter as tk

from tkinter import ttk
from datetime import datetime
from ui.framework import BaseForm
from ui.views.view_data import ItemData

class AddForm(BaseForm):
	TITLE = config.ADD_FORM_TITLE
	ICON = "ui/icons/AddForm.ico"

	def __init__(self, master, on_submit):
		self.status_var = tk.StringVar(value=config.PLANNED)
		self.quantity_var =  tk.IntVar(value=1)
		super().__init__(master, on_submit)

	def reset(self) -> None:
		self.name_ent.delete(0, tk.END)
		self.category_cbx.set("")
		self.quantity_sbx.delete(0, tk.END)
		self.unit_price_ent.delete(0, tk.END)
		self.planned_date_ent.delete(0, tk.END)
		self.planned_date_ent.insert(
			0, 
			datetime.now().strftime("%d/%m/%y")
		)
		self.status_planned_rbt.select()

	def collect(self) -> ItemData:
		return ItemData(
			name=self.name_ent.get(),
			category=self.category_cbx.get(),
			quantity=self.quantity_var.get(),
			unit_price=self.unit_price_ent.get(),
			planned_date=self.planned_date_ent.get(),
			status=self.status_var.get()
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
		self.planned_date_lbl = tk.Label(
			self.window,
			text=config.ITEM_PLANNED_DATE_TITLE
		)

		self.name_ent = tk.Entry(self.window)
		self.category_cbx = ttk.Combobox(
			self.window, values=config.CATEGORIES
		)
		self.quantity_sbx = tk.Spinbox(
			self.window,
			from_=1,
			to=1024,
			increment=1,
			textvariable=self.quantity_var
		)
		self.unit_price_ent = tk.Entry(self.window)
		self.planned_date_ent = tk.Entry(self.window)
		self.status_planned_rbt = tk.Radiobutton(
			self.window,
			text="Planned",
			variable=self.status_var,
			value=config.PLANNED,
			state="active"
		)
		self.status_bought_rbt = tk.Radiobutton(
			self.window,
			text="Bought",
			variable=self.status_var,
			value=config.BOUGHT
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
		self.planned_date_lbl.grid(
			row=4, column=0, sticky="ew"
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
		self.quantity_sbx.grid(
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
		self.planned_date_ent.grid(
			row=4,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.status_planned_rbt.grid(
			row=5,
			column=0,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.status_bought_rbt.grid(
			row=5,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
		self.submit_btn.grid(
			row=6,
			column=1,
			sticky="ew",
			padx=4,
			pady=4
		)
