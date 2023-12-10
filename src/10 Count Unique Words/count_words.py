''' Count the number of words in the file

Output:
Total number of words used in the text: 961948

The TOP 20 words:
the : 25536
I : 20681
and : 19852
to : 17016
of : 16830
a : 13701
my : 11421
in : 10759
you : 9585
is : 8334
that : 8155
And : 7858
not : 7410
with : 7388
his : 6852
be : 6398
your : 6394
for : 6009
have : 5588
it : 5252'''


from collections import Counter

def count_word(file_path):
    ''' Count the number of words in a text file '''
    with open(file_path, encoding='utf-8') as fp:
        data = fp.read()
        words = data.split()
        print(f"Total number of words used in the text: {len(words)}")

        # Count the number of times a specific word occurs
        count = Counter(words)

    # Print the 20 most used words from the text
    print("\nThe TOP 20 words:")
    for key, value in count.most_common(20):
        print(f"{key} : {value}")


if __name__ == '__main__':
    file_path = "src/10 Count Unique Words/shakespeare.txt"
    count_word(file_path)
