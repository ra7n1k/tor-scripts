# import packaged modules
import io
import pycurl
from getpass import getpass
from termcolor import colored
from urllib.parse import urlparse
import os

# import custom modules
from modules.initialize_controller import initialize_controller
from modules.print_status import print_status
from modules.print_error import print_error

def query(proxy, proxy_port, url, save_as_a_file):
    output = io.BytesIO()  # create an instance of bytesio

    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.PROXY, proxy)
    query.setopt(pycurl.PROXYPORT, proxy_port)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)

    if save_as_a_file:
            
        file = os.path.basename(urlparse(url).path)

        if not file:
            file = "output"

        with open(file, "wb") as f:
            def write_callback(data):
                f.write(data)
                return len(data)
            
            query.setopt(pycurl.WRITEFUNCTION, write_callback)

            try:
                query.perform()

            except pycurl.error as e:
                print_error(e)
                
            finally:
                query.close()  # ensure the curl object is closed
    else:
        query.setopt(pycurl.WRITEFUNCTION, output.write)

        try:
            query.perform()
            return output.getvalue()

        except pycurl.error as e:
            print_error(e)
            return None
            
        finally:
            query.close()  # ensure the curl object is closed

try:
    # initialize the tor controller
    passwd = getpass(colored("Password:", "yellow", attrs=["bold"]))
    controller = initialize_controller(9051, passwd)

    print_status(controller) # print current tor daemon status
    url = input(colored("\nURL: ", "yellow", attrs=["bold"]))

    if (input(colored("\nDo you want to save the result as a file? (y/n)\n", "yellow", attrs=["bold"])).lower() == "y"):
        result = query("localhost", 9050, url, True)
        print(f"\n{colored("The result has been saved as a file.", "yellow", attrs=["bold"])}")
    else:
        result = query("localhost", 9050, url, False)
        print(f"\n{colored("Result:", "yellow", attrs=["bold"])}\n{result}")

except Exception as e:
    print_error(e)