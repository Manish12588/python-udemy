# match case was introduce after 3.10 pyton version

seat_type = input("Enter the seat type (sleeper/AC/General/Luxury)").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No AC, beds available")
    case "ac":
        print("Air Conditioner ")
    case "general":
        print("Cheapest opetion - no reservation required")
    case "luxury":
        print("Luxury - premium seat with meal")
    case _:
        print("Invalid seat type")
