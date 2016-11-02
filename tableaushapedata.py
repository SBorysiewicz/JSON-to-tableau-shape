# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import csv
import json
 
class TableauShapeFromJSON(object):
    
    def json_to_csv(self, jsonFile, csvFile):
    
        # with open("drainagediv.json") as file:
        with open(jsonFile) as file:
            data = json.load(file)

        # f = csv.writer(open("drainagediv.csv", "wb+"))
        f = csv.writer(open(csvFile, "wb+"))

        # Write CSV Header, If you dont need that, remove this line
        f.writerow(["DivNumber", "Division", "polygonId", "lineId", "pointId", "Longitude", "Latitude"])

        polygonId = 0
        lineId = 0

        for x in data["features"]:

            divNum = x["properties"]["DivNumber"]
            divName = x["properties"]["Division"]
            geometry = x["geometry"]["coordinates"]
            pointId = 0

            for polygons in geometry:
                for lines in polygons:
                    for point in lines:
                        f.writerow([divNum, divName, polygonId, lineId, pointId, point[0], point[1]])
                        pointId += 1
                    lineId += 1
                polygonId += 1
