import sys
import aioconsole

def erase_input_line():
    # Move the cursor to the beginning of the line
    sys.stdout.write('\r')
    # Overwrite the line with empty spaces
    sys.stdout.write(' ' * len(input("hello")))
    # Move the cursor back to the beginning of the line
    sys.stdout.write('\r')
    sys.stdout.flush()

# Usage example
aioconsole.ainput("Enter your message: ")
erase_input_line()
