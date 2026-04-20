from abc import abstractmethod
from ui.framework.base_window import BaseWindow

class BaseForm(BaseWindow):
	TITLE = "Form"
	ICON = "ui/icons/BaseForm.ico"

	def __init__(self, master, on_submit):
		super().__init__(master)
		self.on_submit = on_submit

	def submit(self) -> None:
		self.on_submit(self.collect())

	def on_show(self) -> None:
		self.reset()

	def on_configure(self) -> None:
		self.window.resizable(False, False)
		self.window.protocol(
			"WM_DELETE_WINDOW", self.hide
		)

	@abstractmethod
	def collect(self) -> None:
		pass

	@abstractmethod
	def reset(self) -> None:
		pass

	@abstractmethod
	def create_widgets(self) -> None:
		pass

	@abstractmethod
	def layout_widgets(self) -> None:
		pass