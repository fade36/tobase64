def read_from_file(path):
    with open(path, "rb") as file:
        return list(file.read())
