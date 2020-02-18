temp_change = 0.04

def calculate(temp_change):
    sea_ice = 1000000
    new_sea_ice = sea_ice * (1-temp_change)
    print("new sea ice area is {}".format(new_sea_ice))
    sea_level_change = (new_sea_ice - sea_ice) / sea_ice * 100 * 20
    print("sea level change is {}".format(sea_level_change))

calculate(temp_change)