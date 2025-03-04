from stem.control import Controller

def initialize_controller(control_port, passwd):
    controller = Controller.from_port(port=control_port)
    controller.authenticate(password=passwd)
    return controller