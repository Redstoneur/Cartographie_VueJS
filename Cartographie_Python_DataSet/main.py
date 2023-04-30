import csv
import json

LinkFolderCSV = "./CSV/"
CSVfileName = input("Enter the name of the file: ")
if CSVfileName == "":
    CSVfileName = "dataset.csv"
elif CSVfileName.find(".csv") == -1:
    CSVfileName = CSVfileName + ".csv"

try:
    with open(LinkFolderCSV + CSVfileName, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")
    exit()



features = []

with open(LinkFolderCSV + CSVfileName, newline="") as csvfile:
  reader = csv.DictReader(csvfile, delimiter=";")
  for row in reader:
    feature = {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [float(row["longitude"].replace(",", ".")), float(row["latitude"].replace(",", "."))]
      },
      "properties": {
        "node": row["node"],
        "indicateur_1": row["indicateur_1"],
        "indicateur_2": row["indicateur_2"],
        "indicateur_3": row["indicateur_3"]
      }
    }
    features.append(feature)

geojson = {
  "type": "FeatureCollection",
  "features": features
}


LinkFolderGeoJSON = "./GeoJSON/"
GeoJSONfileName = CSVfileName.replace(".csv", ".geojson")
with open(LinkFolderGeoJSON + GeoJSONfileName, "w") as f:
  f.write(json.dumps(geojson))

print("File created: " + GeoJSONfileName)


