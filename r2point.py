from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    def is_top(p1):
        return p1.y >= 0

    def find_x_point(p1, p2):
        return R2Point(p1.x-((p1.x - p2.x)*p1.y/(p1.y-p2.y)), 0)

    def top_area_of_triangle(a, b, c):
        e = [R2Point.is_top(a), R2Point.is_top(b), R2Point.is_top(c)]
        area = 0
        if sum(e) == 0:
            area = 0
        elif sum(e) == 3:
            area = R2Point.area(a, b, c)
        elif sum(e) == 1:
            if R2Point.is_top(b):
                a, b = b, a
            if R2Point.is_top(c):
                a, c = c, a
            area = R2Point.area(a, R2Point.find_x_point(a, b),
                                R2Point.find_x_point(a, c))
        else:
            if not R2Point.is_top(b):
                a, b = b, a
            if not R2Point.is_top(c):
                a, c = c, a
            area = R2Point.area(b, c, R2Point.find_x_point(c, a)) +
            + R2Point.area(b, R2Point.find_x_point(a, c),
                           R2Point.find_x_point(a, b))
        return abs(area)


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))
