from machine import Pin

class MultPin():
    _pins = []
    
    def __init__(self, *args, **kwargs):
        self._pins = list(args)
        
    def value(self, state):
        for val in self._pins:
            val.value(state)
            
    def add_pin(self, pin):
        self._pins.append(pin)
        
    def add_pins(self, *pins):
        self._pins += list(pins)
    
    def remove_pin(self, pin):
        self._pins.remove(pin)
        