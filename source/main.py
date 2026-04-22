import ui
import core

from core.models import Item

import tkinter as tk

def main() -> None:
	root = tk.Tk()

	root.title("Purchase manager")
	root.iconbitmap("ui/icons/pm_logo.ico")
	root.rowconfigure(0, weight=1)
	root.columnconfigure(0, weight=1)

	orchestrator = core.Orchestrator(
		root
	)
	menubar = ui.Menubar(root, orchestrator)
	root.mainloop()

if __name__ == "__main__":
	main()