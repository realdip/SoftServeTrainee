
def file_parser(file_path, source_text, replace_text=None):
    if not isinstance(file_path, (str)):
        print("TypeError,", 'file path:', file_path)
        return None
    if not isinstance(source_text, (str)):
        print("TypeError,", 'source_text:', file_path)
        return None
    if not isinstance(replace_text, (str)) and replace_text:
        print("TypeError,", 'replace_text:', file_path)
        return None

    str_count = 0
    try:
        with open(file_path) as f:
            for line in f:
                str_count += line[:].count(source_text)
    except FileNotFoundError:
        print("FileNotFoundError,", 'file path:', file_path)
        return None

    if replace_text:
        with open(file_path) as f:
            text = f.read()
        with open(file_path, 'w') as f:
            f.write(text.replace(source_text, replace_text))
    return str_count


if __name__ == "__main__":
    f = 'file.txt'
    print((file_parser(f, 'entry')), 'Entries found')
    print((file_parser(f, 'entry', 'replace')), 'Entries was replaced')
    print((file_parser(f, 'entry')), 'Entries found')
