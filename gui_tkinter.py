import tkinter as tk
from tkinter import messagebox
import rig_manager as rm

class RigManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rig Manager GUI")
        self.geometry("400x300")

        # Working directory input label and field
        tk.Label(self, text="Rig Directory Path:").pack(pady=5)
        self.dir_entry = tk.Entry(self, width=50)
        self.dir_entry.pack(pady=5)

        # N cores input label and field
        tk.Label(self, text="Number of Cores:").pack(pady=5)
        self.ncores_entry = tk.Entry(self, width=20)
        self.ncores_entry.pack(pady=5)

        # Output display area
        self.output_text = tk.Text(self, height=8, width=50)
        self.output_text.pack(pady=5)

        # Buttons for commands
        tk.Button(self, text="Launch Rig", command=self.launch_rig).pack(side=tk.LEFT, padx=5, pady=10)
        tk.Button(self, text="Set Number of Cores", command=self.set_cores).pack(side=tk.LEFT, padx=5, pady=10)
        tk.Button(self, text="View Stats", command=self.view_stats).pack(side=tk.LEFT, padx=5, pady=10)
        tk.Button(self, text="Stop Rig", command=self.stop_rig).pack(side=tk.LEFT, padx=5, pady=10)

        # Initialize RigManager with empty working dir first
        self.manager = None

    def launch_rig(self):
        path = self.dir_entry.get()
        try:
            self.manager = rm.RigManager(working_dir=path)
            self.manager.launch()
            self.print_output("Rig launched successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def set_cores(self):
        if not self.manager:
            messagebox.showwarning("Warning", "Launch the rig first.")
            return
        try:
            n = int(self.ncores_entry.get())
            self.manager.set_ncores(n=n)
            self.print_output(f"Number of cores set to {n}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for number of cores.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_stats(self):
        if not self.manager:
            messagebox.showwarning("Warning", "Launch the rig first.")
            return
        try:
            stats = self.manager.get_stats()
            self.print_output(stats)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def stop_rig(self):
        if not self.manager:
            messagebox.showwarning("Warning", "Launch the rig first.")
            return
        try:
            self.manager.stop()
            self.print_output("Rig stopped successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def print_output(self, msg):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, str(msg))


if __name__ == "__main__":
    app = RigManagerGUI()
    app.mainloop()
