# import packaged modules
import io
import pycurl
from getpass import getpass
from termcolor import colored

# import custom modules
from modules.initialize_controller import initialize_controller
from modules.print_status import print_status

def query(proxy, proxy_port, url):
    output = io.BytesIO()  # create an instance of bytesio

    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.PROXY, proxy)
    query.setopt(pycurl.PROXYPORT, proxy_port)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
    query.setopt(pycurl.WRITEFUNCTION, output.write)

    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as e:
        print(colored(str(e), "red", attrs=["bold"]))
        return None  # return none or the error
    finally:
        query.close()  # ensure the curl object is closed

try:
    # initialize the tor controller
    passwd = getpass(colored("Password:", "yellow", attrs=["bold"]))
    controller = initialize_controller(9051, passwd)

    print_status(controller) # print current tor daemon status
    url = input(colored("\nURL: ", "yellow", attrs=["bold"]))
    print(f"\n{colored("Result:", "yellow", attrs=["bold"])}\n{query("localhost", 9050, url)}")

except Exception as e:
    print(colored(str(e), "red", attrs=["bold"]))