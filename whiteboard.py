# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False


# check original word against the reversed string

# return a true if same 
# return a false if not same

def solution (word):
    word = word.lower()

    if word == word[::-1]:
        return True 
    else:
        return False