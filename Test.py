import read_kml as rkml
import line

kml = rkml.KML("TestFollow.kml")
all_path = kml.unzip()
print(all_path)
line.Line_kml(all_path)