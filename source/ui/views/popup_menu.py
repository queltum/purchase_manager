import tkinter as tk

class PopupMenu:
	def __init__(self, master, controller):
		self.master = master
		self.controller = controller
		self.nosel_popup = tk.Menu(master, tearoff=0)
		self.sel_popup = tk.Menu(master, tearoff=0)

		self.nosel_popup.add_command(
			label="Add product", 
			command=controller.display_add
		)
		self.nosel_popup.add_command(
			label="Filter", 
			command=controller.display_filter
		)
		# nosel_popup.add_command(
		# 	label="Report", 
		# 	command=
		# )

		self.sel_popup.add_command(
			label="Edit product", 
			command=controller.display_edit
		)
		self.sel_popup.add_command(
			label="Mark as bought", 
			command=controller.mark_as_bought_by_sel
		)
		self.sel_popup.add_command(
			label="Mark as planned",
			command=controller.mark_as_planned_by_sel
		)
		self.sel_popup.add_command(
			label="Remove product", 
			command=controller.remove_product_by_sel
		)

		self.master.bind("<Button-3>", self._on_display)

	def _on_display(self, event) -> None:
		if self.controller.is_selected():
			popup = self.sel_popup
		else:
			popup = self.nosel_popup
		popup.tk_popup(event.x_root, event.y_root)
