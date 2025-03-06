from termcolor import colored

def print_error(e):
    print(colored(str(e), "red", attrs=["bold"]))