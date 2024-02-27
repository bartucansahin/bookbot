def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
            print(file_contents)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except UnicodeDecodeError:
        print("File is not encoded in a way that Python can read.")
    
    

main()


