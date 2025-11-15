import argparse
import random
import string
import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip  # For clipboard integration

def generate_password(length, use_letters, use_numbers, use_symbols, enforce_complexity=False, exclude_chars=""):
    """
    Generate a random password based on the specified criteria.

    :param length: Length of the password
    :param use_letters: Include letters (a-z, A-Z)
    :param use_numbers: Include numbers (0-9)
    :param use_symbols: Include symbols (!@#$%^&* etc.)
    :param enforce_complexity: Ensure at least one of each selected type
    :param exclude_chars: Characters to exclude from the charset
    :return: Generated password string
    """
    charset = ""
    if use_letters:
        charset += string.ascii_letters
    if use_numbers:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    # Remove excluded characters
    charset = ''.join(c for c in charset if c not in exclude_chars)

    if not charset:
        raise ValueError("At least one character type must be selected after exclusions.")

    password = ''.join(random.choices(charset, k=length))

    if enforce_complexity:
        # Ensure at least one of each selected type (considering exclusions)
        has_upper = use_letters and any(c.isupper() for c in password) and any(c.isupper() for c in charset if c.isupper())
        has_lower = use_letters and any(c.islower() for c in password) and any(c.islower() for c in charset if c.islower())
        has_digit = use_numbers and any(c.isdigit() for c in password) and any(c.isdigit() for c in charset if c.isdigit())
        has_symbol = use_symbols and any(c in string.punctuation for c in password) and any(c in string.punctuation for c in charset if c in string.punctuation)

        attempts = 0
        while attempts < 100 and not (has_upper or not use_letters) and not (has_lower or not use_letters) and not (has_digit or not use_numbers) and not (has_symbol or not use_symbols):
            password = ''.join(random.choices(charset, k=length))
            has_upper = use_letters and any(c.isupper() for c in password) and any(c.isupper() for c in charset if c.isupper())
            has_lower = use_letters and any(c.islower() for c in password) and any(c.islower() for c in charset if c.islower())
            has_digit = use_numbers and any(c.isdigit() for c in password) and any(c.isdigit() for c in charset if c.isdigit())
            has_symbol = use_symbols and any(c in string.punctuation for c in password) and any(c in string.punctuation for c in charset if c in string.punctuation)
            attempts += 1

    return password

def calculate_strength(password):
    """
    Calculate password strength based on length and character types.
    :param password: The password string
    :return: Strength level (Weak, Medium, Strong)
    """
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score < 3:
        return "Weak"
    elif score < 5:
        return "Medium"
    else:
        return "Strong"

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x400")

        # Length
        ttk.Label(root, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        self.length_slider = ttk.Scale(root, from_=4, to=32, orient="horizontal", variable=self.length_var)
        self.length_slider.pack()
        self.length_label = ttk.Label(root, text="12")
        self.length_label.pack()
        self.length_slider.config(command=self.update_length_label)

        # Character types
        ttk.Label(root, text="Include:").pack(pady=5)
        self.letters_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(root, text="Letters (a-z, A-Z)", variable=self.letters_var).pack()
        self.numbers_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(root, text="Numbers (0-9)", variable=self.numbers_var).pack()
        self.symbols_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(root, text="Symbols (!@#$%^&*)", variable=self.symbols_var).pack()

        # Enforce complexity
        self.complexity_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(root, text="Enforce Complexity (at least one of each selected type)", variable=self.complexity_var).pack(pady=5)

        # Exclude characters
        ttk.Label(root, text="Exclude Characters:").pack(pady=5)
        self.exclude_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.exclude_var, width=30).pack()

        # Generate button
        self.generate_btn = ttk.Button(root, text="Generate Password", command=self.generate)
        self.generate_btn.pack(pady=10)

        # Password display
        ttk.Label(root, text="Generated Password:").pack()
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(root, textvariable=self.password_var, state="readonly", width=30)
        self.password_entry.pack()

        # Strength
        self.strength_var = tk.StringVar(value="Strength: ")
        ttk.Label(root, textvariable=self.strength_var).pack(pady=5)

        # Copy button
        self.copy_btn = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_btn.pack(pady=10)

    def update_length_label(self, value):
        self.length_label.config(text=str(int(float(value))))

    def generate(self):
        try:
            length = self.length_var.get()
            use_letters = self.letters_var.get()
            use_numbers = self.numbers_var.get()
            use_symbols = self.symbols_var.get()
            enforce_complexity = self.complexity_var.get()
            exclude_chars = self.exclude_var.get()

            password = generate_password(length, use_letters, use_numbers, use_symbols, enforce_complexity, exclude_chars)
            self.password_var.set(password)
            strength = calculate_strength(password)
            self.strength_var.set(f"Strength: {strength}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Generate a password first.")

def main():
    # Check if GUI mode or CLI
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        root = tk.Tk()
        app = PasswordGeneratorGUI(root)
        root.mainloop()
    else:
        # CLI mode
        parser = argparse.ArgumentParser(description="Generate a random password.")
        parser.add_argument(
            "--length", "-l",
            type=int,
            default=12,
            help="Length of the password (default: 12)"
        )
        parser.add_argument(
            "--letters", "-let",
            action="store_true",
            default=True,
            help="Include letters (a-z, A-Z) (default: True)"
        )
        parser.add_argument(
            "--no-letters",
            action="store_false",
            dest="letters",
            help="Exclude letters"
        )
        parser.add_argument(
            "--numbers", "-num",
            action="store_true",
            default=True,
            help="Include numbers (0-9) (default: True)"
        )
        parser.add_argument(
            "--no-numbers",
            action="store_false",
            dest="numbers",
            help="Exclude numbers"
        )
        parser.add_argument(
            "--symbols", "-sym",
            action="store_true",
            default=True,
            help="Include symbols (!@#$%^&* etc.) (default: True)"
        )
        parser.add_argument(
            "--no-symbols",
            action="store_false",
            dest="symbols",
            help="Exclude symbols"
        )
        parser.add_argument(
            "--enforce-complexity", "-c",
            action="store_true",
            help="Enforce complexity (at least one of each selected type)"
        )
        parser.add_argument(
            "--exclude", "-e",
            type=str,
            default="",
            help="Characters to exclude from the password"
        )

        args = parser.parse_args()

        try:
            password = generate_password(args.length, args.letters, args.numbers, args.symbols, args.enforce_complexity, args.exclude)
            print(f"Generated password: {password}")
            strength = calculate_strength(password)
            print(f"Strength: {strength}")
        except ValueError as e:
            print(f"Error: {e}")
            return 1

        return 0

if __name__ == "__main__":
    exit(main())
