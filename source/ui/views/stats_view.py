import tkinter as tk

from ui.framework import BaseWindow

class StatsView(BaseWindow):
	TITLE =  "Stats"
	ICON = "ui/icons/StatsView.ico"

	def __init__(self, master, get_data):
		self.get_data = get_data
		self.total_items = tk.StringVar()
		self.total_amount = tk.StringVar()
		self.average_amount = tk.StringVar()
		self.bought_amount = tk.StringVar()
		self.planned_amount = tk.StringVar()
		super().__init__(master)

	def update(self) -> None:
		stats = self.get_data()
		self.total_items.set(stats.total_items)
		self.total_amount.set(stats.total_amount)
		self.average_amount.set(stats.average_amount)
		self.bought_amount.set(stats.bought_amount)
		self.planned_amount.set(stats.planned_amount)

	def on_show(self) -> None:
		self.update()

	def on_configure(self) -> None:
		self.window.geometry("200x120")
		self.window.resizable(False, False)
		self.window.protocol(
			"WM_DELETE_WINDOW", self.hide
		)

	def create_widgets(self) -> None:
		self.total_items_lbl = tk.Label(
			self.window, 
			textvariable=self.total_items
		)
		self.total_amount_lbl = tk.Label(
			self.window, 
			textvariable=self.total_amount
		)
		self.average_amount_lbl = tk.Label(
			self.window, 
			textvariable=self.average_amount
		)
		self.bought_amount_lbl = tk.Label(
			self.window, 
			textvariable=self.bought_amount
		)
		self.planned_amount_lbl = tk.Label(
			self.window, 
			textvariable=self.planned_amount
		)

	def layout_widgets(self) -> None:
		self.total_items_lbl.pack()
		self.total_amount_lbl.pack()
		self.average_amount_lbl.pack()
		self.bought_amount_lbl.pack()
		self.planned_amount_lbl.pack()
