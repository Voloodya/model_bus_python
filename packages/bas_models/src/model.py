from packages.bas_models.src.bus import Bus


class Model:
    def __init__(self, buses: [Bus]):
        self.buses = buses

    def run(self, flights: int) -> [int]:
        raise NotImplementedError() #Метод переопределяется в конкретных моделях

    def reset_buses(self):
        for bus in self.buses:
            bus.reset()
