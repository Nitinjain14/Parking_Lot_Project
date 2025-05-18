#extract the values from the text file and the action to be done
class Command:
    def __init__(self, action, reg_no=None, color=None, slot_no=None, capacity=None):
        self.action = action
        self.reg_no = reg_no
        self.color = color
        self.slot_no = slot_no
        self.capacity = capacity

    @classmethod
    def from_string(cls, command_str):
        parts = command_str.split()
        action = parts[0]
        if action == "create_parking_lot":
            return cls(action=action, capacity=int(parts[1]))
        elif action == "park":
            return cls(action=action, reg_no=parts[1], color=parts[2])
        elif action == "leave":
            return cls(action=action, slot_no=int(parts[1]))
        elif action in {"slot_numbers_for_cars_with_colour", "registration_numbers_for_cars_with_colour"}:
            return cls(action=action, color=parts[1])
        elif action == "slot_number_for_registration_number":
            return cls(action=action, reg_no=parts[1])
        return cls(action=action)
