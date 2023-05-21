import os

text = "Hello"
terminal_width = os.get_terminal_size().columns
print(f"{text:>{terminal_width}}")

text = "Hello"
width = 10
print("{:<10}".format(text))