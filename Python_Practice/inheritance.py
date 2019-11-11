class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connection = True

    def __str__(self):
        return f"Device {self.name} {self.connected_by}"

    def disconnect(self):
        self.connection = False
        print("Disconnected")

#device = Device("printer", "usb")
#print(device)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connection:
            print("your not connected")
        print(f"printing {pages} pages")
        self.remaining_pages -= pages #remaining_pages = remaining_pages - pages

printer = Printer("printer", "usb", 1000)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(20)
