from Parking_Lot_project.models import vehicles
from Parking_Lot_project.models.vehicles import Vehicle

# creating space in parking lot
class ParkingLot:
    def __init__(self, capacity):
        self._capacity = capacity
        self._slots = [None] * capacity

    # function to get capacity
    @property
    def capacity(self):
        return self._capacity

    # function to park a vehicle
    def park_vehicle(self, regno, color):
        for i in range(self.capacity):
            if self._slots[i] is None:
                self._slots[i] = Vehicle(regno, color)
                return i + 1
        return -1

    # function to remove a vehicle
    def remove_vehicle(self, slot):
        if 0<slot<=self.capacity and self._slots[slot-1]:
            self._slots[slot-1] = None
            return slot
        return -1

    #function to get status of all vehicles
    def status_all_vehicle(self):
        print("Slot No.\tReg No\t\tColor")
        for i,vehicle in enumerate(self._slots):
            if vehicle:
                print(i,"\t\t",vehicle.regno,"\t\t",vehicle.color)

    # function to get slot of a vehicle according to colour
    def slot_of_coloured_vehicle(self, color):
        return [i+1 for i, v in enumerate(self._slots) if v and v.color == color]

    # function to get slot of a vehicle according to regno
    def slot_of_regno_vehicle(self, regno):
        for i, v in enumerate(self._slots):
            if v and v.regno == regno:
                return i + 1
        return -1

    # function to get regno of a vehicle according to colour
    def regno_of_colored_vehicle(self, color):
        return [v.regno for v in self._slots if v and v.color == color]
