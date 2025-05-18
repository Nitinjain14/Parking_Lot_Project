from Parking_Lot_project.services.parking_service import ParkingLot

def handle_command(file_path):
    with open(file_path, "r") as file:
        data = file.read().replace("\n", " ")  # replace newline with space for split function
    data_ls = data.split(" ")
    ParkingLot_capacity = ParkingLot(int(data_ls[1]))
    print(f"Created a parking lot with {ParkingLot_capacity.capacity} slots")

    # main loop
    print(data_ls)
    j = 0
    i = 2
    while i < len(data_ls):
        if data_ls[i] == "park":
            slot = ParkingLot_capacity.park_vehicle(j, data_ls[i + 1], data_ls[i + 2])
            if slot == -1:
                print("Sorry, parking lot is full")
            else:
                print(f"Allocated Slot number: {slot}")
            i += 3
            j += 1

        elif data_ls[i] == "leave":
            slot = ParkingLot_capacity.remove_vehicle(int(data_ls[i + 1]))
            print(f"Slot number {slot} is free")
            i += 2

        elif data_ls[i] == "status":
            vehicles_status = ParkingLot_capacity.status_all_vehicle()
            if not vehicles_status:
                print("Parking lot is empty")
            else:
                print("Slot No.\tReg No\t\t\tColor")
                for v in range(len(vehicles_status)):
                    print(vehicles_status[v][0], "\t\t", vehicles_status[v][1], "\t\t", vehicles_status[v][2])
            i += 1

        elif data_ls[i] == "slot_numbers_for_cars_with_colour":
            slot_clr = ParkingLot_capacity.slot_of_coloured_vehicle(data_ls[i + 1])
            if not slot_clr:
                print("Not found")
            else:
                for c in range(len(slot_clr)):
                    print(slot_clr[c], end=" ")
                print()
            i += 2

        elif data_ls[i] == "slot_number_for_registration_number":
            slot_reg = ParkingLot_capacity.slot_of_regno_vehicle(data_ls[i + 1])
            print(slot_reg)
            i += 2

        elif data_ls[i] == "registration_numbers_for_cars_with_colour":
            cars_name = ParkingLot_capacity.regno_of_colored_vehicle(data_ls[i + 1])
            if not cars_name:
                print("Not found")
            else:
                for c in range(len(cars_name)):
                    print(cars_name[c], end=" ")
                print()
            i += 2