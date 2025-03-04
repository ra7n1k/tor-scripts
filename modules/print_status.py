from termcolor import colored
from stem import CircStatus

def print_status(controller):
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
