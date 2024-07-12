def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write('%s\n' % item)
        print(f"Деректер {filename} файлына жазылды.")
    except (FileNotFoundError, PermissionError, IOError):
        print("Қате орын алды. Файлды жазу мүмкін емес.")

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        print(f"Деректер {filename} файлының ішінде оқылды.")
        return [line.strip() for line in data]
    except (FileNotFoundError, PermissionError, IOError):
        print("Қате орын алды. Файлды оқу мүмкін емес.")
        return []
