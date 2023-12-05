class PalindromeChecker:
    def __init__(self, text:str):
        self.text = text

    def sanitize_text(self):
        """
        Remove spaces and convert to lowercase for case-insensitive comparison.
        """
        return ''.join(char.lower() for char in self.text if char.isalnum())

    def is_palindrome(self):
        """
        Check if the text is a palindrome.
        """
        sanitized_text = self.sanitize_text()
        reversed_text = sanitized_text[::-1]
        return sanitized_text == reversed_text

if __name__ == "__main__":
    
    test_cases = ["radar", "A man, a plan, a canal, Panama!", "Hello, World!"]

    for test in test_cases:
        print(f"Is {test} a palindrome? - {PalindromeChecker(test).is_palindrome()}")

# slightly similar approach to yours