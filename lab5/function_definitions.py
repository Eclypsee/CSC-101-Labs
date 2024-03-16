"""function_definitions.py

Write your function definitions in this file.

Write unit tests for your functions in 'function_tests.py'.

You may, but are not required, to write 'print' tests under the main guard.
"""
from point import Point

# Write your function definitions here
def first_element(l:list[list[float]])->list[float]:
    """first element of a nested list->list"""
    return [l[x][0] for x in range(len(l)) if len(l[x])>0]

def x_coordinates(l:list[Point])->list[Point]:
    """list of points-->list of x coords of points"""
    return [p.x for p in l if len(l)>0]

def are_in_positive_quadrant(l:list[Point])->list:
    """takes a list of points, return points in quadrant 1"""
    return [poi for poi in l if poi.x>0 and poi.y>0]

def distance(a:Point, b:Point)->float:
    """gets euclidean distance between 2 point objects"""
    return float(((a.x-b.x)**2+(a.y-b.y)**2)**.5)

def manhattan_distance(a:Point, b:Point)->float:
    """gets manhattan distance between 2 point objects"""
    return float(abs(a.x-b.x)+abs(a.y-b.y))

def origin_distances(a:Point, b:Point)->float:
    """takes 2 points, return a list of 2 distances from each point to origin"""
    return [float((a.x**2+a.y**2)**0.5), float((b.x**2+b.y**2)**0.5)]
if __name__ == '__main__':
    print(first_element([[1.2, 3.4, 5.6], [], [7.8, 9.0], [11.12], [], [13.14, 15.16]]))
    print(x_coordinates([]))
    print(are_in_positive_quadrant([Point(3,4), Point(-4,3)]))
    print(distance(Point(0, 0), Point(3, 4)))
    print(manhattan_distance(Point(3, 5), Point(4, 6)))
    print(origin_distances(Point(3, 4), Point(4, 6)))