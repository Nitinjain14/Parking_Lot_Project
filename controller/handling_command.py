from Parking_Lot_project.services.parking_service import ParkingLot
from Parking_Lot_project.models.command import Command

def handle_command(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    parking_lot_val = None
    for line in lines:
        command = Command.from_string(line)

        if command.action == "create_parking_lot":
            parking_lot_val = ParkingLot(command.capacity)
            print(f"Created a parking lot with {parking_lot_val.capacity} slots")

        elif command.action == "park":
            slot = parking_lot_val.park_vehicle(command.reg_no, command.color)
            if slot == -1:
                print("Sorry, parking lot is full")
            else:
                print(f"Allocated Slot number: {slot}")

        elif command.action == "leave":
            slot = parking_lot_val.remove_vehicle(command.slot_no)
            if slot == -1:
                print("Vehicle not found")
            else:
                print(f"Slot number {slot} is free")

        elif command.action == "status":
            parking_lot_val.status_all_vehicle()

        elif command.action == "slot_numbers_for_cars_with_colour":
            slot = parking_lot_val.slot_of_coloured_vehicle(command.color)
            print(", ".join(map(str, slot)) if slot else "Not found")

        elif command.action == "slot_number_for_registration_number":
            slot = parking_lot_val.slot_of_regno_vehicle(command.reg_no)
            print(slot if slot != -1 else "Not found")

        elif command.action == "registration_numbers_for_cars_with_colour":
            reg_nos = parking_lot_val.regno_of_colored_vehicle(command.color)
            print(", ".join(reg_nos) if reg_nos else "Not found")
