import tkinter as tk
from tkinter import simpledialog, messagebox


def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result


# Initialize the Tkinter root (main window)
root = tk.Tk()
root.withdraw()  # Hide the main window since we only need popups

# Get user input via popup dialogs
message = simpledialog.askstring("Input", "Enter the message:")
shift_value = simpledialog.askinteger("Input", "Enter the shift value:")
mode = simpledialog.askstring("Input", "Choose mode (encrypt/decrypt):").lower()

# Validate mode input
if mode not in ('encrypt', 'decrypt'):
    messagebox.showerror("Error", "Invalid mode! Please enter 'encrypt' or 'decrypt'.")
else:
    # Encrypt or Decrypt based on user choice
    output = caesar_cipher(message, shift_value, mode)

    # Display the result in a popup
    messagebox.showinfo("Result", f"The result is: {output}")

# Close the Tkinter root window
root.destroy()
