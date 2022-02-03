
"""File donde se demuestra la ventaja de usar variables estaticas
    En este ejemplo creamos un error en el programa ya que se esta pasando
    un entero a la función del palindromo

    En consola para realizar un testeo es como sigue:
    mypy palindrome.py --check-untyped-defs
"""

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string ==  string[::-1]

def run():
    # Local variable
    print(is_palindrome(word))


if __name__ == "__main__":
    #Global variable
    word = input("Escribe una palabra: ")
    run()