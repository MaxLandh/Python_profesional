from subprocess import REALTIME_PRIORITY_CLASS


def make_repeat_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    
    return repeater

def run():
    repeat_5 = make_repeat_of(5)
    print(repeat_5("Hola"))

if __name__ == "__main__":
    run()