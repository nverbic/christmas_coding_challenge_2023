''' Identify a palindrome '''

def reverse_using_slice(text):
    '''Reverse a string using slice operator'''
    return text [::-1]

def is_palindrome(text):
    '''Check if the text argument is a polindrome.'''
    # Remove any white spaces and uppercases
    original_text = "".join(text.split()).casefold()
    # Reverse the text
    reversed_text = reverse_using_slice(original_text)

    print(f"Inputed text without whitespaces: {original_text}")
    print(f"Reversed text: {reversed_text}")

    # Ignore uppercase letters when comparing
    if original_text == reversed_text:
        return True

    return False


if __name__ == '__main__':
    input_text = input("Please enter a string to check if it is a palindrome: \n")
    result = is_palindrome(input_text)
    if result:
        print("Yes, the string is a palindrome.")
    else:
        print("No, the string is not a palindrome. ")
