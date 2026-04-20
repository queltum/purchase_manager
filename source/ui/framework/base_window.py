import tkinter as tk

from abc import ABC, abstractmethod

class BaseWindow(ABC):
	TITLE = "Window"
	ICON = "ui/icons/BaseWindow.ico"

	def __init__(self, master):
		self.master = master
		self.window = tk.Toplevel(master)
		self.window.withdraw()

		self.configure_window()
		self.create_widgets()
		self.layout_widgets()

	def show(self) -> None:
		self.on_show()
		self.window.deiconify()
		self.window.lift()
		self.window.focus_set()

	def hide(self) -> None:
		self.on_hide()
		self.window.withdraw()
		self.master.lift()
		self.master.focus_set()

	def configure_window(self):
		self.on_configure()
		self.window.title(self.TITLE)
		self.window.iconbitmap(self.ICON)

	def on_show(self) -> None:
		pass

	def on_hide(self) -> None:
		pass

	def on_configure(self) -> None:
		pass

	@abstractmethod
	def create_widgets(self) -> None:
		pass

	@abstractmethod
	def layout_widgets(self) -> None:
		pass