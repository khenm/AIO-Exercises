# modify  your file path
file_path = r'D:\AIO\Exercise--git\AIO-Exercises\Week-2\P1_data.txt'


def count_chars_from_file(file_path: str) -> dict:
    """Count the number of characters in a string,

    Args:
        file_path (str): a paragraph of words to be split
    """
    # initialize the dictionary
    words_dict: dict = {}

    # read file
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        for word in words:
            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += 1
    print(words_dict)


def main():
    count_chars_from_file(file_path=file_path)


if __name__ == "__main__":
    main()
