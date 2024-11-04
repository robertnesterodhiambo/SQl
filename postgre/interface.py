import tkinter as tk
from tkinter import messagebox, Text
from whatif import generate_modified_sql, get_qep_cost
from preprocessing import load_database, fetch_qep

class QueryOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Query Optimizer What-If Analysis")

        # SQL Query Entry Panel
        tk.Label(root, text="SQL Query:").pack()
        self.query_text = Text(root, height=4, width=50)
        self.query_text.pack()

        # Buttons
        tk.Button(root, text="Fetch QEP", command=self.display_qep).pack()
        tk.Button(root, text="Run What-If Analysis", command=self.run_what_if_analysis).pack()

        # Panels for QEP and AQP display
        self.qep_display = Text(root, height=15, width=50)
        tk.Label(root, text="QEP Display:").pack()
        self.qep_display.pack()

        self.aqp_display = Text(root, height=15, width=50)
        tk.Label(root, text="AQP Display:").pack()
        self.aqp_display.pack()

    def display_qep(self):
        sql_query = self.query_text.get("1.0", tk.END).strip()
        if not sql_query:
            messagebox.showwarning("Input Error", "Please enter an SQL query.")
            return
        try:
            qep = fetch_qep(sql_query)
            self.qep_display.delete("1.0", tk.END)
            self.qep_display.insert(tk.END, qep)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch QEP: {str(e)}")

    def run_what_if_analysis(self):
        sql_query = self.query_text.get("1.0", tk.END).strip()
        if not sql_query:
            messagebox.showwarning("Input Error", "Please enter an SQL query.")
            return
        try:
            modified_sql, aqp = generate_modified_sql(sql_query)
            self.aqp_display.delete("1.0", tk.END)
            self.aqp_display.insert(tk.END, aqp)
            cost_diff = get_qep_cost(sql_query) - get_qep_cost(modified_sql)
            messagebox.showinfo("Cost Analysis", f"Cost difference: {cost_diff}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run what-if analysis: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QueryOptimizerApp(root)
    root.mainloop()
