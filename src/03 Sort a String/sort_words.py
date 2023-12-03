'''Sort words alphabetically

Output:
Before sort: banana ORANGE apple Green
After sort: apple banana Green ORANGE
Before sort: Order this sentence using SORTED function
After sort: function Order sentence SORTED this using'''

def sort_words(text):
    '''Sort a string'''
    print(f"Before sort: {text}")
    # Create a list of words
    words_list = text.split(" ")
    # Treat all the list items as if they were lowercase
    # without actually changing the values in the list.
    sorted_list = sorted(words_list, key=str.lower)
    # Create a string from the array of words
    sorted_text = ' '.join(sorted_list)
    print(f"After sort: {sorted_text}")


if __name__ == '__main__':
    text_samples = ["banana ORANGE apple Green",
                    "Order this sentence using SORTED function"]

    for text_sample in (text_samples):
        sort_words(text_sample)
