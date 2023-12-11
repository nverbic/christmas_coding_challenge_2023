''' Count the number of words in the file

Output:
Total number of words used in the text: 976836

The TOP 20 words:
the : 30257
and : 28413
i : 23070
to : 20997
of : 18824
a : 16163
you : 14570
my : 13179
in : 12333
that : 12063
is : 9858
not : 9066
with : 8531
me : 8262
for : 8244
it : 8212
his : 7583
be : 7384
this : 7165
he : 7100'''


from collections import Counter
import re

def count_word(file_path):
    ''' Count the number of words in a text file '''
    with open(file_path, encoding='utf-8') as fp:
        data = fp.read()
        # Words contain letters, numbers, apostrophes and hyphens
        # String is converted to lowercase
        words = re.findall(r"([A-Z0-9'-]+)", data.lower(), re.IGNORECASE)
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
