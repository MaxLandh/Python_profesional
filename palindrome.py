
def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string ==  string[::-1]

def run():
    word = 1000
    print(is_palindrome(word))


if __name__ == "__main__":
    run()