#Import Shapely Package and pandas:
from shapely.geometry import Point, Polygon
import pandas as pd
import csv

# Import trajectory files:
df = pd.read_csv(r"C:\Users\smkca\Downloads\Scent_Trajectories.csv")

# Upload your polygon coordinates into the coordinate variable below:

coords1 = [1312.9, 317.1], [1356.6, 322.8], [1390.0, 329.3], [1415.2,336.7], [1410.3, 364.3], [1403.0, 394.4], [1392.4, 430.2], [1359.1, 417.2], [1334.7, 396.0], [1321.7, 372.4], [1311.9, 346.4]
poly1 = Polygon(coords1)
coords2 = [1312.9, 317.1], [1356.6, 322.8], [1390.0, 329.3], [1415.2,336.7], [1410.3, 364.3], [1403.0, 394.4], [1392.4, 430.2], [1359.1, 417.2], [1334.7, 396.0], [1321.7, 372.4], [1311.9, 346.4]
poly2 = Polygon(coords2)
coords3 = [1312.9, 317.1], [1356.6, 322.8], [1390.0, 329.3], [1415.2,336.7], [1410.3, 364.3], [1403.0, 394.4], [1392.4, 430.2], [1359.1, 417.2], [1334.7, 396.0], [1321.7, 372.4], [1311.9, 346.4]
poly3 = Polygon(coords3)

#Apply the Shapely function Within with the PANDAS function Apply:

df['within_polygon1'] = df.apply(lambda row: Point(row['x'], row['y']).within(poly1), axis=1)
print(df['within_polygon1'])

df['within_polygon2'] = df.apply(lambda row: Point(row['x'], row['y']).within(poly2), axis=1)
print(df['within_polygon2'])

df['within_polygon3'] = df.apply(lambda row: Point(row['x'], row['y']).within(poly3), axis=1)
print(df['within_polygon3'])

#Count the number of True and False Statements:
counts = df['within_polygon1'].value_counts()
print(counts)

counts2 = df['within_polygon2'].value_counts()
print(counts2)

counts3 = df['within_polygon3'].value_counts()
print(counts3)

#Convert frames to seconds using estimated frames per second (1 frame per sec)
BeetleTimeMinutes1 = counts / 60
print(BeetleTimeMinutes1)

BeetleTimeMinutes2 = counts / 60
print(BeetleTimeMinutes2)

BeetleTimeMinutes3 = counts / 60
print(BeetleTimeMinutes3)

#Create CSV files of the output, one with a simple time in minutes,
with open('TimeSpentonFilterPaper', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time spent OFF area (Min)', 'Time spent ON area (min)'])
    writer.writerow(BeetleTimeMinutes1)
    writer.writerow(BeetleTimeMinutes2)
    writer.writerow(BeetleTimeMinutes3)
df.to_csv('BeetleTimeinPolygon.csv', index=False)