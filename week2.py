from logo import logoo
import math
print(logoo)

points = [(3,4), (1,2), (2,4), (1,5), (1,-1)]
distances = []
def euclideanDistance(point1,point2):
    x1 , y1 = point1
    x2, y2 = point2
    return math.sqrt((x2- x1) **2 + (y2 - y1) ** 2)

for i in range(len(points)):
    for j in range (i+1, len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)

min_distance = min(distances)
print(f"Points in 2D space : {points}")
print(f"Distances between points in 2D space: {distances}")
print(f"minimum value is : {min_distance}")
