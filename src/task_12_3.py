# Создать класс Point, описывающий точку(атрибуты x, y). Создать класс Figure  .  Создать три дочерних класса Circle
# (атрибуты: координаты центра(тип Point), длина радиуса; методы: нахождение периметра и площади окружности),
# Triangle (атрибуты: три точки, методы:нахождение площади и периметра), Square (атрибуты: две точки,
# методы: нахождение площади и периметра). При потребности создавать все необходимые
# методы не описанные в задании


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Figure:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def cut(self):
        cut = ((self.x2 - self.x1) ** 2 + ((self.y2 - self.y1) ** 2)) ** 0.5
        return cut


class Circle(Figure):



    def radius(self):
        radius = ((self.x2 - self.x1) ** 2 + ((self.y2 - self.y1) ** 2)) ** 0.5
        return radius

    def cir_duga(self):
        cir_duga = cir.radius() * 2 * 3.14159265
        return cir_duga

    def area (self):
        area = cir.radius() ** 2 * 3.14159265
        return area


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x2, y2)
        self.x3 = x3
        self.y3 = y3

    def side_a_b(self):
        side_a_b = ((self.x2 - self.x1) ** 2 + ((self.y2 - self.y1) ** 2)) ** 0.5
        return side_a_b

    def side_b_c(self):
        side_b_c = ((self.x3 - self.x2) ** 2 + ((self.y3 - self.y2) ** 2)) ** 0.5
        return side_b_c

    def side_a_c(self):
        side_a_c = ((self.x3 - self.x1) ** 2 + ((self.y3 - self.y1) ** 2)) ** 0.5
        return side_a_c

    def sum_sides(self):
        sum_sides = tri.side_a_b() + tri.side_a_c() + tri.side_b_c()
        return sum_sides

    def tile_p(self):
        tile_p = tri.sum_sides() / 2
        return tile_p

    def area_tri(self):
        s = (tri.tile_p() * (tri.tile_p() - tri.side_a_b()) * (tri.tile_p() - tri.side_b_c()) * (tri.tile_p()
                                                                                                 - tri.side_a_c())) ** 0.5
        return s


class Square(Figure):

    def diag(self):
        super().cut()
        diag = squ.cu()
        return diag

    def area(self):
        area = squ.diag() * squ.diag() / 2
        return area


def main():
    fig = Figure(0, 0, 1, 1)
    cir = Circle(0, 0, 4, 4)
    tri = Triangle(0, 0, 0, 2, 2, 0)
    squ = Square(0, 0, 9, 9)

    # print(f'Point A (x={fig.x1},y={fig.y1})')
    # print(f'Point B (x={fig.x2},y={fig.y2})')
    # print(f'Distance from Point A to Point B equals {fig.cut()}')

    print(f'Point A (x={cir.x1},y={cir.y1})')
    print(f'Point B (x={cir.x2},y={cir.y2})')
    print(f'Radius from point A to point B equals {cir.cut()}')
    duga = cir.radius() * 2 * 3.1415926
    print(duga)

    print(f'Circumference with center coordinates ({cir.x1}, {cir.y1}) and '
          f'radius {cir.radius()} equals {duga}')
    print(f'Area of a circle with radius {cir.radius()} equals {cir.area()}')

    #
    # print(f'Point A (x={tri.x1},y={tri.y1})')
    # print(f'Point B (x={tri.x2},y={tri.y2})')
    # print(f'Point C (x={tri.x3},y={tri.y3})')
    # print(f'Side A - B = {tri.side_a_b()}')
    # print(f'Side B - C = {tri.side_b_c()}')
    # print(f'Side A - C = {tri.side_a_c()}')
    # print(f'Perimeter a triangle with sides {tri.side_a_b()}, '
    #       f'{tri.side_b_c()} and {tri.side_a_c()}  equals {tri.sum_sides()}')
    # print(f'Area a triangle with sides {tri.side_a_b()}, '
    #       f'{tri.side_b_c()} and {tri.side_a_c()}  equals {tri.area_triangle()}')

    # print(f'Point A (x={squ.x1},y={squ.y1})')
    # print(f'Point B (x={squ.x2},y={squ.y2})')
    # print(f'Diagonal a Square equals {squ.diag()}')
    # print(f'Area a Square with Diagonal {squ.diag()} equals {squ.area()}')

if __name__ == '__main__':
    main()