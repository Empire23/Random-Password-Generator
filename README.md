# Random Password Generator

A versatile Python-based password generator that supports both command-line interface (CLI) and graphical user interface (GUI) modes. Generate secure, customizable passwords with options for length, character types, complexity enforcement, and more.

## Features

- **Customizable Password Length**: Set password length from 4 to 32 characters.
- **Character Type Selection**: Include or exclude letters (a-z, A-Z), numbers (0-9), and symbols (!@#$%^&* etc.).
- **Complexity Enforcement**: Ensure passwords contain at least one of each selected character type.
- **Exclude Specific Characters**: Remove unwanted characters from the generated password.
- **Password Strength Calculation**: Automatically assesses and displays password strength (Weak, Medium, Strong).
- **Clipboard Integration**: Easily copy generated passwords to the clipboard (GUI mode).
- **Dual Interface**: Use via command-line for scripting or GUI for interactive use.
- **Error Handling**: Validates inputs and provides helpful error messages.

## Requirements

- Python 3.6 or higher
- `tkinter` (usually included with Python installations)
- `pyperclip` library for clipboard functionality

## Installation


1. Install the required dependency:
   ```bash
   pip install pyperclip
   ```

## Usage

### GUI Mode

Run the application with the GUI:
```bash
python password_generator.py --gui
```

The GUI allows you to:
- Adjust password length using the slider
- Select character types (letters, numbers, symbols)
- Enable complexity enforcement
- Specify characters to exclude
- Generate and view passwords
- Check password strength
- Copy passwords to clipboard

### CLI Mode

Generate passwords from the command line:
```bash
python password_generator.py [options]
```

#### Options

- `-l, --length LENGTH`: Password length (default: 12, range: 4-32)
- `-let, --letters`: Include letters (default: True)
- `--no-letters`: Exclude letters
- `-num, --numbers`: Include numbers (default: True)
- `--no-numbers`: Exclude numbers
- `-sym, --symbols`: Include symbols (default: True)
- `--no-symbols`: Exclude symbols
- `-c, --enforce-complexity`: Enforce complexity (at least one of each selected type)
- `-e, --exclude CHARACTERS`: Characters to exclude from the password

#### Examples

Generate a default 12-character password:
```bash
python password_generator.py
```

Generate a 16-character password with all character types:
```bash
python password_generator.py --length 16
```

Generate a password excluding vowels and numbers:
```bash
python password_generator.py --exclude "aeiouAEIOU0123456789"
```

Generate a strong password with enforced complexity:
```bash
python password_generator.py --length 20 --enforce-complexity
```

## How It Works

The password generator uses Python's `random` module to select characters from a customizable charset. The charset is built based on your selections and exclusions. For complexity enforcement, the generator attempts to create a password that includes at least one character from each selected type.

Password strength is calculated based on:
- Length (8+ characters for basic, 12+ for better)
- Presence of lowercase letters
- Presence of uppercase letters
- Presence of digits
- Presence of symbols

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# Random-Password-Generator
