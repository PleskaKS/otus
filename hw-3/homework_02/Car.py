import Vehicle


class Car(Vehicle.Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = None

    def set_engine(self, object):
        self.engine = object
