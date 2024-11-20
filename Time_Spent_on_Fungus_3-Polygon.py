# Import Shapely Package and pandas:
from shapely.geometry import Point, Polygon
import pandas as pd
import csv

# Import trajectory files:
df = pd.read_csv(r"C:\Users\smkca\Downloads\Scent_Trajectories.csv")

# Upload your polygon coordinates into the coordinate variable below:

WinnerCords = [1312.9, 317.1], [1356.6, 322.8], [1390.0, 329.3], [1415.2, 336.7], [1410.3, 364.3], [1403.0, 394.4], [
    1392.4, 430.2], [1359.1, 417.2], [1334.7, 396.0], [1321.7, 372.4], [1311.9, 346.4]
WinnerPoly = Polygon(WinnerCords)
LoserCords = [1312.9, 317.1], [1356.6, 322.8], [1390.0, 329.3], [1415.2, 336.7], [1410.3, 364.3], [1403.0, 394.4], [
    1392.4, 430.2], [1359.1, 417.2], [1334.7, 396.0], [1321.7, 372.4], [1311.9, 346.4]
LoserPoly = Polygon(LoserCords)
ControlCords = [1312.9, 317.1], [1356.6, 322.8], [1390.0, 329.3], [1415.2, 336.7], [1410.3, 364.3], [1403.0, 394.4], [
    1392.4, 430.2], [1359.1, 417.2], [1334.7, 396.0], [1321.7, 372.4], [1311.9, 346.4]
ControlPoly = Polygon(ControlCords)

# Apply the Shapely function Within with the PANDAS function Apply:

df['Within_WinnerPoly'] = df.apply(lambda row: Point(row['x'], row['y']).within(WinnerPoly), axis=1)
print(df['Within_WinnerPoly'])

df['Within_LoserPoly'] = df.apply(lambda row: Point(row['x'], row['y']).within(LoserPoly), axis=1)
print(df['Within_LoserPoly'])

df['Within_ControlPoly'] = df.apply(lambda row: Point(row['x'], row['y']).within(ControlPoly), axis=1)
print(df['Within_ControlPoly'])

# Count the number of True and False Statements:
counts = df['Within_WinnerPoly'].value_counts()
print(counts)

counts2 = df['Within_LoserPoly'].value_counts()
print(counts2)

counts3 = df['Within_ControlPoly'].value_counts()
print(counts3)

# Convert frames to seconds using estimated frames per second (1 frame per sec)
BeetleTimeMinutes1 = counts / 60
print(BeetleTimeMinutes1)

BeetleTimeMinutes2 = counts / 60
print(BeetleTimeMinutes2)

BeetleTimeMinutes3 = counts / 60
print(BeetleTimeMinutes3)

RowTitles = ("Winner Filter", "Loser Filter", "Control Filter")

# Create CSV files of the output, one with a simple time in minutes,
with open('TimeSpentonFilterPaper', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time spent OFF area (Min)', 'Time spent ON area (min)'])
    writer.writerow(BeetleTimeMinutes1)
    writer.writerow(BeetleTimeMinutes2)
    writer.writerow(BeetleTimeMinutes3)
df.to_csv('BeetleTimeinPolygon.csv', index=False)
