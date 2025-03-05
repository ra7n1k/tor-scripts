# About
The goal of this project is to provide common and usable tor-daemon management scripts for everyone.
You can use the scripts under the MIT License.
Most of the scripts in this project use Python 3 and Stem library (Cross Platform).

*Inspired by the Stem Docs project*

# Features

## Main

### Request a New Circuit
File: `new_circuit.py`

This is for requesting a new Tor circuit. You can use this by providing the Tor control password.
`control_port` variable is to set Tor control port. It is set to `9051` by default.

### HTTP Request
File: `query.py`

This is for sending a HTTP request (alternatives to `curl` and `wget`). This supports Onion Services. You can use this by providing the Tor control password and the target URL.

## Modules

### Initialize the Tor Controller
File: `modules/initialize_controller.py`

This is for initializing Tor controller. You can use this module by providing the control port and the Tor control password.

### Print the Tor Status
File: `modules/print_status.py`

This is for printing the current status of the Tor process and circuit.