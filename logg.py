class Fore:
    BLACK = '\x1b[30m'
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'
    BLUE = '\x1b[34m'
    MAGENTA = '\x1b[35m'
    CYAN = '\x1b[36m'
    WHITE = '\x1b[37m'
    RESET = '\x1b[39m'

    LIGHTBLACK = '\x1b[90m'
    LIGHTRED = '\x1b[91m'
    LIGHTGREEN = '\x1b[92m'
    LIGHTYELLOW = '\x1b[93m'
    LIGHTBLUE = '\x1b[94m'
    LIGHTMAGENTA = '\x1b[95m'
    LIGHTCYAN = '\x1b[96m'
    LIGHTWHITE = '\x1b[97m'


class Back:
    BLACK = '\x1b[40m'
    RED = '\x1b[41m'
    GREEN = '\x1b[42m'
    YELLOW = '\x1b[43m'
    BLUE = '\x1b[44m'
    MAGENTA = '\x1b[45m'
    CYAN = '\x1b[46m'
    WHITE = '\x1b[47m'
    RESET = '\x1b[49m'

    LIGHTBLACK = '\x1b[100m'
    LIGHTRED = '\x1b[101m'
    LIGHTGREEN = '\x1b[102m'
    LIGHTYELLOW = '\x1b[103m'
    LIGHTBLUE = '\x1b[104m'
    LIGHTMAGENTA = '\x1b[105m'
    LIGHTCYAN = '\x1b[106m'
    LIGHTWHITE = '\x1b[107m'

class Log:
    def Info(message: str, end: str = '\n'):
        print(f'[{Fore.GREEN}Info{Fore.RESET}] {message}', flush=True, end=end)

    def Warning(message: str, end: str = '\n'):
        print(f'[{Fore.YELLOW}Warning{Fore.RESET}] {message}', flush=True, end=end)

    def Error(message: str, end: str = '\n'):
        print(f'[{Fore.RED}Error{Fore.RESET}] {message}', flush=True, end=end)