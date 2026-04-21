import tkinter as tk
from tkinter import messagebox

class Menubar(tk.Menu):
	def __init__(self, master, orchestrator):
		super().__init__(master, tearoff=0)
		self.orchestrator = orchestrator
		self.file_menu = tk.Menu(self, tearoff=0)
		self.edit_menu = tk.Menu(self, tearoff=0)
		self.view_menu = tk.Menu(self, tearoff=0)
		self.help_menu = tk.Menu(self, tearoff=0)

		self.file_menu.add_command(
			label="Open",
			command=orchestrator.load_data
		)

		self.file_menu.add_command(
			label="Save as",
			command=orchestrator.save_data
		)

		self.file_menu.add_command(
			label="Exit", 
			command=master.destroy
		)

		self.edit_menu.add_command(
			label="Add product", 
			command=orchestrator.show_add_form
		)
		self.edit_menu.add_command(
			label="Edit product",
			command=orchestrator.show_edit_form
		)
		self.edit_menu.add_command(
			label="Mark as bought",
			command=orchestrator.mark_as_bought
		)
		self.edit_menu.add_command(
			label="Mark as planned",
			command=orchestrator.mark_as_planned
		)
		self.edit_menu.add_command(
			label="Remove product", 
			command=orchestrator.remove_item
		)

		self.view_menu.add_command(
			label="Filter",
			command=orchestrator.show_filter_form
		)
		self.view_menu.add_command(
			label="Stats",
			command=orchestrator.show_stats_window
		)

		self.help_menu.add_command(
			label="About",
			command=lambda: messagebox.showinfo(
				"About", 
				"Purchase manager"
			)
		)

		self.add_cascade(label="File", menu=self.file_menu)
		self.add_cascade(label="Edit", menu=self.edit_menu)
		self.add_cascade(label="View", menu=self.view_menu)
		self.add_cascade(label="Help", menu=self.help_menu)
		self.master.config(menu=self)