# one mile is = 1609.344 meters

def convert_velocity(v):
    miles = 1609.344
    kmh = v*(miles/1000)
    ms = kmh/3.6
    return ms, kmh

ms, kmh = convert_velocity(10)
print(ms, kmh)
