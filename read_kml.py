from pykml import parser

class KML:

    def __init__(self, file):
        self.file = file

    def kml_to_csv(self):
        with open(self.file, 'rb') as file:
            for line in file:
                print(line)
            # root = parser.parse(file).getroot()
            # placemarks = root.Document.Placemark
            # for placemark in placemarks:
            #     coordinates = placemark.Point.coordinates.text.strip().split(',')
            #     longitude, latitude = [float(coord.strip()) for coord in coordinates[:2]]
            #     pack_waypoint = [latitude, longitude]
            #
            #     yield pack_waypoint

    def unzip(self):
        waypoint = []
        for i in self.kml_to_csv():
            waypoint.append(i)

        return waypoint