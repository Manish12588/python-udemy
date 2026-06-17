device_status = "Active"
temprature = 38

if device_status == "Active":
    if temprature > 35:
        print(f"High temprature alert!")
    else:
        print(f"Temprature is normal")
else:
    print(f"Device is offline")
