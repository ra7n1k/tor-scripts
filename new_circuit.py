import getpass
from stem import Signal
from stem import CircStatus
from stem.control import Controller
from termcolor import colored

def initialize_controller(control_port, passwd):
    controller = Controller.from_port(port=control_port)
    controller.authenticate(password=passwd)
    return controller

controller = initialize_controller(9051, getpass.getpass(colored("Password:", "yellow", attrs=["bold"])))

def print_status():
    print(colored("\nTor version: ", "yellow", attrs=["bold"]) + colored(controller.get_info("version"), "cyan"))
    print(colored("\nProcess/PID: ", "yellow", attrs=["bold"]) + colored(controller.get_info("process/pid"), "cyan"))
    
    for circ in sorted(controller.get_circuits()):
        if circ.status != CircStatus.BUILT:
            continue

        print(colored("\nCircuit %s (%s)" % (circ.id, circ.purpose), "yellow", attrs=["bold"]))

        for i, entry in enumerate(circ.path):
            div = "+" if (i == len(circ.path) - 1) else "|"
            fingerprint, nickname = entry

            desc = controller.get_network_status(fingerprint, None)
            address = desc.address if desc else "unknown"

            print(colored(" %s- %s (%s, %s)" % (div, fingerprint, nickname, address), "cyan"))

try:
    print_status()
    controller.signal(Signal.NEWNYM)
    print(colored("\nNew circuit was requested.", "green", attrs=["bold"]))
    print_status()

except Exception as e:
    print(colored(str(e), "red", attrs=["bold"]))