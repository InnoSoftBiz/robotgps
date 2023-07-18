import simplekml

def Line_kml(waypoint):
    Gwaypoint = []
    for x, y in waypoint:
        path = y, x
        Gwaypoint.append(path)

    kml = simplekml.Kml()
    ls = kml.newlinestring(name = 'Line path Robot')
    ls.coords = Gwaypoint
    ls.exetrude = 1
    ls.altitudemode = simplekml.AltitudeMode.relativetoground
    ls.style.linestyle.width = 5
    ls.style.linestyle.color = simplekml.Color.yellow
    kml.save("LineString Robot.kml")