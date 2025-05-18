from Parking_Lot_project.models.vehicles import Vehicle

# creating space in parking lot
class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.vehicles = [None] * capacity

    # function to park a vehicle
    def park_vehicle(self, j, regno, color):
        slot = j
        if slot >= self.capacity:
            for k in range(self.capacity):
                if self.vehicles[k] is None:
                    slot = k
                    break
                elif k == self.capacity - 1:
                    return -1
        self.vehicles[slot] = Vehicle(regno, color)
        return slot + 1

    # function to remove a vehicle
    def remove_vehicle(self, slot):
        self.vehicles[slot - 1] = None
        return slot

    #function to get status of all vehicle
    def status_all_vehicle(self):
        vehicles_status = []
        for i in range(self.capacity):
            if self.vehicles[i] is not None:
                vehicles_status.append([i + 1, self.vehicles[i].get_regno(), self.vehicles[i].get_color()])
        return vehicles_status

    # function to get slot of a vehicle according to colour
    def slot_of_coloured_vehicle(self, color):
        slot_clr = []
        for i in range(self.capacity):
            if self.vehicles[i] is not None and self.vehicles[i].get_color() == color:
                slot_clr.append(i + 1)
        return slot_clr

    # function to get slot of a vehicle according to regno
    def slot_of_regno_vehicle(self, regno):
        for i in range(self.capacity):
            if self.vehicles[i] is not None and self.vehicles[i].get_regno() == regno:
                return i + 1
        else:
            return "Not found"

    # function to get regno of a vehicle according to colour
    def regno_of_colored_vehicle(self, color):
        cars_name = []
        for i in range(self.capacity):
            if self.vehicles[i] is not None and self.vehicles[i].get_color() == color:
                cars_name.append(self.vehicles[i].get_regno())
        return cars_name
