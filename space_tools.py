import math

spaceport_lats = {
    'PSCA': 57,
    'SLC-46': 29,
    'Camden': 33,
    'Vandenberg': 31,
    'SaxaVord': 68
}

def inc_from_az(lat,azimuth):
    rlat = math.radians(lat)
    razimuth = math.radians(azimuth)

    inc = round(math.degrees(
        math.acos(
            math.cos(rlat)*math.sin(razimuth)
            )
        ),1)

    return(inc)

def az_from_inc(lat,inclination):
    rlat = math.radians(lat)
    rinc = math.radians(inclination)

    try:
        az = round(math.degrees(
                math.asin(
                    math.cos(rinc)/math.cos(rlat)
                )
            ),1)
        return(az)
    except ValueError:
        return(None)

spaceport = ""
while spaceport not in spaceport_lats:
    for key in spaceport_lats:
        print(key)

    spaceport = input("Type the name of a spaceport from the list to launch from: ")

    if spaceport == "quit":
        break
    try:
        lat = spaceport_lats[spaceport]
        print(f"The latitude of {spaceport} is {lat} degrees")
    except KeyError:
        print(f"{spaceport} is not a spaceport")


# azimuth = float(input("What azimuth are you flying? "))
# dinc = inc_from_az(lat, azimuth)
# print(f"At latitude {lat}, an azimuth of {azimuth}, results in the inclination of: {dinc}")
#
inclination = float(input("What inclination are you trying to hit? "))
daz = az_from_inc(lat, inclination)
print(f"At latitude {lat} ({spaceport}), to achieve an inclination of {inclination}, the azimuth required is: {daz}")



# for azimuth in range(360):
#     dinc = inc_from_az(lat, azimuth)
#     print(f"At latitude {lat}, an azimuth of {azimuth}, results in the inclination of: {dinc}")
#
# for inclination in range(360):
#     daz = az_from_inc(lat, inclination)
#     print(f"At latitude {lat}, to achieve an inclination of {inclination}, the azimuth required is: {daz}")
