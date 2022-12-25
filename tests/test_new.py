from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Segment
from convex import Polygon


# Тесты для треугольника
class TestR2Point1:

    # Проверка подсчета площади когда точки 2 точки лежат на оси Ox
    def test_top_area_of_triangle_1(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(0.0, 1.0)
        assert R2Point.top_area_of_triangle(a, b, c) == 0.5


class TestR2Point2:

    # Проверка подсчета площади когда одна точка ниже оси Ox
    def test_top_area_of_triangle_2(self):
        a, b, c = R2Point(-2.0, 0.0), R2Point(0.0, 1.0), R2Point(0.0, -1.0)
        assert R2Point.top_area_of_triangle(a, b, c) == 1.0


class TestR2Point3:

    # Проверка подсчета площади когда все точки ниже оси Ox
    def test_top_area_of_triangle_3(self):
        a, b, c = R2Point(-2.0, -1.0), R2Point(-1.0, -5.0), R2Point(-7.0, -9.0)
        assert R2Point.top_area_of_triangle(a, b, c) == 0.0


class TestR2Point4:

    # Проверка подсчета площади когда две точки ниже оси Ox
    def test_top_area_of_triangle_4(self):
        a, b, c = R2Point(-2.0, -1.0), R2Point(2.0, -1.0), R2Point(0.0, 1.0)
        assert R2Point.top_area_of_triangle(a, b, c) == 1.0


class TestR2Point5:

    # Проверка подсчета площади когда все точки выше оси Ox
    def test_top_area_of_triangle_4(self):
        a, b, c = R2Point(1.0, 1.0), R2Point(-1.0, 1.0), R2Point(1.0, 3.0)
        assert R2Point.top_area_of_triangle(a, b, c) == 2.0


# Тесты для четырехугольника
class TestPolygon1:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Добавим точку, получим квадрат в первой четверти
    def test_area_top(self):
        assert self.f.add(R2Point(1.0, 1.0)).area_top() == approx(1)


class TestPolygon2:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(R2Point(
                0.0, 0.0), R2Point(
                -1.0, 0.0), R2Point(
                0.0, -1.0))

    # Добавим точку, получим квадрат к третьей четверти
    def test_area_top_1(self):
        assert self.f.add(R2Point(-1.0, -1.0)).area_top() == approx(0)


class TestPolygon3:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(R2Point(
            1.0, 1.0), R2Point(
            -1.0, -1.0), R2Point(
            1.0, -1.0))

    # Добавим точку, получим квадрат
    def test_area_top_1(self):
        assert self.f.add(R2Point(-1.0, 1.0)).area_top() == approx(2)
