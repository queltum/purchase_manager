import tkinter as tk

from ui.framework import BaseWindow

class StatsView(BaseWindow):
	TITLE =  "Stats"
	ICON = "ui/icons/StatsView.ico"

	def __init__(self, master, get_data):
		super().__init__(master)
		self.get_data = get_data
		self.total_items = tk.StringVar()
		self.total_amount = tk.StringVar()
		self.average_amount = tk.StringVar()
		self.bought_amount = tk.StringVar()
		self.planned_amount = tk.StringVar()

	def on_configure(self) -> None:
		self.window.resizable(False, False)

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
		self.total_items_lbl.grid(
			row=0,
			column=0,
		)
