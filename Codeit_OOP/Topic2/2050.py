# 2038.py에서 EAFP 스타일로 Paint 클래스 변경
from math import sqrt, pi
from abc import ABC, abstractmethod


class Shape(ABC):
    """도형 클래스"""

    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스를 그림판에 추가한다"""
        self.shapes.append(shape)

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        total_area = 0

        for shape in self.shapes:
            try:
                total_area += shape.area()
            except (AttributeError, TypeError):
                print("그림판에 area 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}(이)가 있습니다.".format(shape))

        return total_area

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        total_perimeter = 0

        for shape in self.shapes:
            try:
                total_perimeter += shape.perimeter()
            except (AttributeError, TypeError):
                print("그림판에 perimeter 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}(이)가 있습니다.".format(shape))

        return total_perimeter


class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.width

    def perimeter(self):
        """직사각형의 둘레의 길이를 리턴한다"""
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레의 길이를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class RightTriangle(Shape):
    """직각삼각형 클래스"""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """직각삼각형 인스턴스의 넓이를 구한다"""
        return self.base * self.height / 2

    def perimeter(self):
        """직각삼각형 인스턴스의 둘레의 길이를 구한다"""
        return sqrt(self.base**2 + self.height**2) + self.base + self.height


class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레의 길이를 리턴한다"""
        return 3 * self.side


class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


# Shape 클래스를 상속받는 클래스의 인스턴스들
right_triangle = RightTriangle(3, 4)
equilateral_triangle = EquilateralTriangle(3)
circle = Circle(4)
rectangle = Rectangle(3, 4)

# Shape 클래스를 상속받지 않고 area, perimeter 메소드도 없는 클래스의 인스턴스
cylinder = Cylinder(4, 3)

# 그림판 인스턴스 생성
paint_program = Paint()

# 그림판에 인스턴스들 추가
paint_program.add_shape(cylinder)
paint_program.add_shape(right_triangle)
paint_program.add_shape(equilateral_triangle)
paint_program.add_shape(circle)
paint_program.add_shape(rectangle)

# 그림판에 추가된 인스턴스들의 총 넓이합과 둘레합 계산
print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

# 그림판의 도형들의 정보 출력
print(paint_program)