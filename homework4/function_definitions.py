"""function_definitions.py

Write your function definitions in this file.

Write unit tests for your functions in 'function_tests.py'.

You may, but are not required, to write 'print' tests under the main guard.
"""
from price import Price
from geometry import Rectangle
from geometry import Point
from geometry import Circle
from book import Book
from employee import Employee

# Write your function definitions here
def vowel_count(k:str)->int:
    """counts vowels in a string"""
    vc = 0
    for c in k:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vc+=1
    return vc

def short_lists(l:list[list[int]])->list[list[int]]: # example input [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """returns a list of sublists with 2 elements"""
    return [x for x in l if len(x)==2]

def ascending_pairs(l:list[list[int]])->list[list[int]]:
    """returns a list of sublists with 2 elements sorted ascending order"""
    new = []
    for x in range(len(l)):
        if len(l[x])==2:
            new.append([min(l[x]), max(l[x])])
        else:
            new.append(l[x])
    return new
def add_prices(a:Price, b:Price)->Price:
    """adds 2 price objects and returns result object"""
    cents = (a.cents+b.cents)%100
    dollars = a.dollars+b.dollars+(a.cents+b.cents)//100
    return Price(dollars, cents)
def rectangle_perimeter(r:Rectangle)->float:
    """gets the perimeter of a rectangle object as a float"""
    tl = r.top_left
    br = r.bottom_right
    return abs(br.x-tl.x)*2+abs(tl.y-br.y)*2
def books_by_author(n:str, b:list)->list:
    """returns a list of book objects by author n"""
    return[x for x in b if x.author == n]
def circle_bound(r:Rectangle)->Circle:
    """takes a rectangle and returns a bounding circle object"""
    diameter  = abs(r.top_left.x-r.bottom_right.x) if abs(r.top_left.x-r.bottom_right.x) > abs(r.top_left.y-r.bottom_right.y) else abs(r.top_left.y-r.bottom_right.y)
    center = Point((r.top_left.x+r.bottom_right.x)/2, (r.top_left.y+r.bottom_right.y)/2)
    return Circle(center, diameter/2)
def below_pay_average(names:list[Employee])->list[str]:
    """returns a list of employees underpaid compared to average"""
    total = 0;
    for x in range(len(names)):
        total+=names[x].pay
    if len(names)>0:
        average = total/len(names)
    else:
        average = 0
    return [e.name for e in names if e.pay<average]

if __name__ == '__main__':
    print(vowel_count("adei ousu eqa .*&%$#isf"))
    print(short_lists([[1, 2], [4, 5, 6], [7, 8, 9]]))
    print(ascending_pairs([[1, 2], [12, 6, 11], [11, 9]]))
    print(add_prices(Price(3, 41), Price(9, 99)))
    print(rectangle_perimeter(Rectangle(Point(3.2, 4), Point(7,9))))
    print(books_by_author("a2", [Book("book1", "a1"), Book("book2", "a2"), Book("book3", "a2"), Book("book4", "a9"), Book("book11", "a1")]))
    print(circle_bound(Rectangle(Point(4, 12), Point(12, 8))))
    print(below_pay_average([Employee("john", 33.0), Employee("Joe", 11.0)]))