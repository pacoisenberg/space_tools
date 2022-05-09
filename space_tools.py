import math

spaceport_lats = {
    'PSCA': 57.4304338,
    'SLC46': 28.4581376,
    'Camden': 30.9366602,
    'SLC8': 34.5763024,
    'SaxaVord': 60.8190531
}

def inc_from_az(lat,azimuth):
    rlat = math.radians(lat)
    razimuth = math.radians(azimuth)

    inc = round(math.degrees(
        math.acos(
            math.cos(rlat)*math.sin(razimuth)
            )
        ),2)

    return(inc)

def az_from_inc(lat,inclination):
    rlat = math.radians(lat)
    rinc = math.radians(inclination)

    try:
        az = round(math.degrees(
                math.asin(
                    math.cos(rinc)/math.cos(rlat)
                )
            ),2)
        return(az)
    except ValueError:
        return(None)

def inc_or_az():
    calc_choice = ""
    while calc_choice not in ['a','i']:
        calc_choice = input("Do you want to calculate (a)zimuth or (i)nclination?" )
        calc_choice = calc_choice[0]
    return (calc_choice)

def lat_user_choice(spaceport_dictionary):

    spaceport = ""
    while spaceport not in spaceport_lats:
        for key in spaceport_lats:
            print(key)

        spaceport = input("Type the name of a spaceport from the list or enter a latitude to launch from: ").upper()

        if spaceport == "QUIT":
            break
        try:
            lat = spaceport_lats[spaceport]
            print(f"The latitude of {spaceport} is {lat} degrees")
        except KeyError:
            try:
                lat = float(spaceport)
                if 0 <= lat <= 90:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"{spaceport} is not a valid entry")

    return(spaceport, lat)

spaceport, lat = lat_user_choice(spaceport_lats)
type_of_calc = inc_or_az()

if type_of_calc == "a":
    inclination = float(input("What inclination are you trying to hit? "))
    daz = az_from_inc(lat, inclination)
    print(f"At latitude {lat} ({spaceport}), to achieve an inclination of {inclination}, the azimuth required is: {daz}")

elif type_of_calc == "i":
    azimuth = float(input("What azimuth are you flying? "))
    dinc = inc_from_az(lat, azimuth)
    print(f"At latitude {lat} ({spaceport}), an azimuth of {azimuth}, results in the inclination of: {dinc}")
