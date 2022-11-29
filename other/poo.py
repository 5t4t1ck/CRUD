class Airplane:
    def __init__(self, passengers, seats, pilots=[]):
        self.passengers = passengers
        self.seats = seats
        self.__pilots = pilots

    def takeoff(self):
        pass

airpplane = Airplane(passengers=20, seats=30, pilots=["Tom","Billy"])
airpplane.passengers=31
airpplane.takeoff()