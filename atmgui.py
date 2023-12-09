import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def simple_dialog(title, prompt):
    return simpledialog.askfloat(title, prompt, parent=root)

class ATM:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000  # Initial balance for demonstration
        self.transaction_history = []

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            messagebox.showinfo("Success", f"Withdrawal of ${amount} successful!")
            return True
        else:
            messagebox.showerror("Error", "Invalid withdrawal amount")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            messagebox.showinfo("Success", f"Deposit of ${amount} successful!")
            return True
        else:
            messagebox.showerror("Error", "Invalid deposit amount")
            return False

    def transfer(self, to_user_id, amount):
        # Simplified transfer logic, for demonstration purposes
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Transfer to {to_user_id}: ${amount}")
            messagebox.showinfo("Success", f"Transfer of ${amount} to {to_user_id} successful!")
            return True
        else:
            messagebox.showerror("Error", "Invalid transfer amount")
            return False

    def get_transaction_history(self):
        return "\n".join(self.transaction_history)

class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")

        self.atm = None

        # Configure root window
        root.geometry("400x300")
        root.configure(bg="#2E4053")  # Background color

        # Create and place components using grid
        self.label_user_id = tk.Label(root, text="User ID:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2E4053")
        self.entry_user_id = tk.Entry(root, font=("Helvetica", 12))

        self.label_pin = tk.Label(root, text="PIN:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2E4053")
        self.entry_pin = tk.Entry(root, show="*", font=("Helvetica", 12))

        self.button_login = tk.Button(root, text="Login", command=self.login, font=("Helvetica", 12), bg="#16A085", fg="#ECF0F1")
        self.button_quit = tk.Button(root, text="Quit", command=self.quit, font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1")

        self.label_balance = tk.Label(root, text="Balance: $0", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#2E4053")

        self.button_withdraw = tk.Button(root, text="Withdraw", command=self.withdraw, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.button_deposit = tk.Button(root, text="Deposit", command=self.deposit, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.button_transfer = tk.Button(root, text="Transfer", command=self.transfer, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.button_history = tk.Button(root, text="Transaction History", command=self.show_history, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.button_sign_out = tk.Button(root, text="Sign Out", command=self.sign_out, font=("Helvetica", 12), bg="#E67E22", fg="#ECF0F1")

        self.label_user_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_user_id.grid(row=0, column=1, padx=10, pady=10)
        self.label_pin.grid(row=1, column=0, padx=10, pady=10)
        self.entry_pin.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_quit.grid(row=2, column=1, columnspan=2, pady=10)

    def login(self):
        user_id = self.entry_user_id.get()
        pin = self.entry_pin.get()

        # Example user ID and pin for demonstration
        if user_id == "123" and pin == "1234":
            self.atm = ATM(user_id, pin)
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid user ID or PIN")

    def show_main_menu(self):
        # Update GUI for main menu
        self.label_user_id.grid_forget()
        self.entry_user_id.grid_forget()
        self.label_pin.grid_forget()
        self.entry_pin.grid_forget()
        self.button_login.grid_forget()
        self.button_quit.grid_forget()

        self.label_balance.grid(row=0, column=0, columnspan=2, pady=10)
        self.update_balance_label()

        self.button_withdraw.grid(row=1, column=0, padx=10, pady=10)
        self.button_deposit.grid(row=1, column=1, padx=10, pady=10)
        self.button_transfer.grid(row=2, column=0, padx=10, pady=10)
        self.button_history.grid(row=2, column=1, padx=10, pady=10)
        self.button_sign_out.grid(row=3, column=0, columnspan=2, pady=10)

    def update_balance_label(self):
        balance_text = f"Balance: ${self.atm.balance}"
        self.label_balance.config(text=balance_text)

    def withdraw(self):
        amount = simple_dialog("Withdraw", "Enter withdrawal amount:")
        if amount is not None:
            if self.atm.withdraw(amount):
                self.update_balance_label()

    def deposit(self):
        amount = simple_dialog("Deposit", "Enter deposit amount:")
        if amount is not None:
            if self.atm.deposit(amount):
                self.update_balance_label()

    def transfer(self):
        to_user_id = simple_dialog("Transfer", "Enter recipient's User ID:")
        amount = simple_dialog("Transfer", "Enter transfer amount:")
        if to_user_id is not None and amount is not None:
            if self.atm.transfer(to_user_id, amount):
                self.update_balance_label()

    def show_history(self):
        history_text = self.atm.get_transaction_history()
        messagebox.showinfo("Transaction History", history_text)

    def sign_out(self):
        # Reset GUI to the login screen
        self.label_balance.grid_forget()
        self.button_withdraw.grid_forget()
        self.button_deposit.grid_forget()
        self.button_transfer.grid_forget()
        self.button_history.grid_forget()
        self.button_sign_out.grid_forget()

        self.label_user_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_user_id.grid(row=0, column=1, padx=10, pady=10)
        self.label_pin.grid(row=1, column=0, padx=10, pady=10)
        self.entry_pin.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_quit.grid(row=2, column=1, columnspan=2, pady=10)

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    atm_gui = ATMGUI(root)
    root.mainloop()
