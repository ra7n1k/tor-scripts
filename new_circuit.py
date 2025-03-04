# import packaged modules
from getpass import getpass
from stem import Signal
from termcolor import colored

# import custom modules
from modules.initialize_controller import initialize_controller
from modules.print_status import print_status

try:
    # initialize the tor controller
    passwd = getpass(colored("Password:", "yellow", attrs=["bold"]))
    controller = initialize_controller(9051, passwd)

    print_status(controller) # print current tor daemon status
    # request a new circuit
    controller.signal(Signal.NEWNYM)
    print(colored("\nA new circuit was requested.", "green", attrs=["bold"]))
    print_status(controller) # print current tor daemon status

except Exception as e:
    print(colored(str(e), "red", attrs=["bold"]))