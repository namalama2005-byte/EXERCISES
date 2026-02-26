def longest(strings: list):
    longest_str = strings[0]


    for current_string in strings:
        if len(current_string) > len(longest_str):
            longest_str = current_string

    return longest_str


if __name__== "__main__":
    strings = ['hi', 'hiya', 'hello', 'howdyboody', 'hi there']
    print(longest(strings))