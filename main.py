import gpxpy
from geopy.distance import geodesic
import math

# Change input.gpx to your file name
gpx_file = open('./input.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

# Arbitrary length list
waypoints = [0] * 10000

distance = 0

for track in gpx.tracks:
    for segment in track.segments:
        for i in range(1, len(segment.points)): 
            point1 = segment.points[i-1]
            point2 = segment.points[i]
            distance += geodesic((point1.latitude, point1.longitude), (point2.latitude, point2.longitude)).meters 
            if waypoints[math.floor(distance/1000)] == 0:
                newWP = gpxpy.gpx.GPXWaypoint(point2.latitude, point2.longitude)
                newWP.name = "KM " + str(math.floor(distance/1000))
                gpx.waypoints.append(newWP)
                waypoints[math.floor(distance/1000)] = 1

# [Optional] Change output.gpx to whatever you want the output file to be called
with open('./output.gpx', 'w') as output_file:
    output_file.write(gpx.to_xml())
