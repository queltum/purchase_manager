import ui
import core

import tkinter as tk

def main() -> None:
	root = tk.Tk()

	root.title("Purchase manager")
	root.iconbitmap("ui/icons/pm_logo.ico")
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)

	items = core.Items()
	items_view = ui.ItemsView(root)

	stats = core.Stats(items)

	orchestrator = core.Orchestrator(
		root,
		items,
		stats,
		items_view,
		None
	)
	menubar = ui.Menubar(root, orchestrator)
	root.mainloop()

if __name__ == "__main__":
	main()