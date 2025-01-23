def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(file_contents)}  words found in the document\n")
    my_dict = count_char(file_contents)

    del my_dict[' ']
    del my_dict['.']
    del my_dict['#']
    sorted_items = sorted(my_dict.items(), key = lambda item: item[1], reverse=True)

    for tuple in sorted_items:
        print(f"The '{tuple[0]}' character was found {tuple[1]} times")


def count_words(val):
    return len(val.split())

def count_char(val):
    final = {}
    for letter in val:
        char = letter.lower()
        if char in final:
            final[char] += 1
        else:
            final[char] = 1
    return final

def sort_on(dict):
    return dict["num"]


main()