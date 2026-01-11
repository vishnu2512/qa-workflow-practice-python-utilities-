def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as error:
        return f"Unexpected error: {error}"

if __name__ == "__main__":
    content = read_file("sample.txt")
    print(content)
