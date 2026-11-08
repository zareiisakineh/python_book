# file: ex_11_01_read_text_file_start.py

def print_file(filename: str) -> None:
    """Print the contents of a text file with line numbers.
    Prints a helpful message if the file does not exist.
    """
    
    # TODO Part 1: open with "with open(filename, encoding='utf-8') as f:"
    # loop over lines with "for i, line in enumerate(f, 1):"
    # strip trailing newline: line.rstrip()
    # print: "  1: line text"
    #with open(filename, encoding="utf-8") as f:
    #    for i, line in enumerate(f, 1):
    #        print(f"{i}: {line.rstrip()}")

    
    # TODO Part 2: wrap in try-except FileNotFoundError
    # print: "Error: 'filename' not found."
    #try:
    #    with open(filename, encoding="utf-8") as f:
    #            for i, line in enumerate(f, 1):
    #                print(f"{i}: {line.rstrip()}")            
    #except FileNotFoundError:
    #    print(f"Error: '{filename}' finnes ikke")
        

    # TODO Part 3: restructure using try-except-else
    # put the file reading in the else block
    try:
        f = open(filename, encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    else:
        with f:
            for i, line in enumerate(f, 1):
                print(f"{i}: {line.rstrip()}")


if __name__ == "__main__":
    print_file("sample.txt")
    print()
    print_file("missing.txt")
