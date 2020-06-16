"""Autor: Arkadiusz Łęga, email: horemheb@vp.pl
    
    Aplikacja licząca dane potrzebne do obliczenia
    diagramu Voronoi dla centrów reprezentowanych przez punkty.

    W części main trzeba podać punkty które są ujęte w zadaniu,
    oraz podać dla których par punktów mają być obliczone symetralne.
"""

# Długość długiego separatora oddzielającego różne części liczenia.
LONG_SEPARATOR = 80
# Długość krótkiego separatora oddzielającego różne części liczenia.
SHORT_SEPARATOR = 40


class Punkt:
    def __init__(self, name, coordinate_x, coordinate_y):
        self.__name = name
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y

    @property
    def name(self):
        return self.__name

    @property
    def coordinate_x(self):
        return self.__coordinate_x

    @property
    def coordinate_y(self):
        return self.__coordinate_y

    def __str__(self):
        return f'Punkt {self.__name}: x={self.__coordinate_x}, y={self.__coordinate_y}'


class Symetralna:
    """y = ax + b """

    def __init__(self, name, a, b):
        self.__name = name
        self.__a = a
        self.__b = b

    @property
    def name(self):
        return self.__name

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def __str__(self):
        return f'Symetralna {self.name}:\ty={round(self.a,2)}x+{round(self.b,2)}\n\t\t{round(self.a,2)*(-1)}x+y+{round(self.b,2)*(-1)}=0'

    def short(self):
        return f'Symetralna {self.name}:\t{round(self.a,2)*(-1)}x+y+{round(self.b,2)*(-1)}=0'


def det(a11, a12, a21, a22):
    # a11 a12
    # a21 a22
    return a11*a22-a12*a21


def licz_symetralna(point_1, point_2):
    print(f'Obliczam symetralną dla punktów: {point_1}, {point_2}')
    print(LONG_SEPARATOR*"=")
    print(f'{point_1.coordinate_y}=a*{point_1.coordinate_x}+b')
    print(f'{point_2.coordinate_y}=a*{point_2.coordinate_x}+b')
    print(SHORT_SEPARATOR*"-")

    riverse_y = point_1.coordinate_y * (-1)
    riverse_x = point_1.coordinate_x * (-1)
    if point_1.coordinate_x*(-1) < 0:
        print(f'{point_1.coordinate_y*(-1)}=-a*({point_1.coordinate_x*(-1)})-b')
    else:
        print(f'{point_1.coordinate_y*(-1)}=-a*{point_1.coordinate_x*(-1)}-b')
    print(f'{point_2.coordinate_y}=a*{point_2.coordinate_x}+b')
    print(SHORT_SEPARATOR*"-")

    y = riverse_y + point_2.coordinate_y
    x = riverse_x + point_2.coordinate_x

    print(f'{y}=a*{x}')

    a = x*y
    print(f'a={a}')
    print(SHORT_SEPARATOR*"-")
    print(f'{point_1.coordinate_y}={a}*{point_1.coordinate_x}+b')
    if point_1.coordinate_y < 0:
        print(f'b=-({a}*{point_1.coordinate_x}){point_1.coordinate_y}')
    else:
        print(f'b=-({a}*{point_1.coordinate_x})+{point_1.coordinate_y}')

    b = point_1.coordinate_y + ((a * point_1.coordinate_x) * (-1))
    print(f'b={b}')
    print(SHORT_SEPARATOR*"=")

    print(f'a={a}, b={b}')
    print(SHORT_SEPARATOR*"*")

    print(
        f'Obliczma środek pomiędzy punktem {point_1.name} a {point_2.name}')
    print(
        f'S=(({point_1.coordinate_x}+{point_2.coordinate_x})/2;({point_1.coordinate_y}+{point_2.coordinate_y})/2)')
    s = Punkt(name="S", coordinate_x=(point_1.coordinate_x+point_2.coordinate_x)/2,
              coordinate_y=(point_1.coordinate_y+point_2.coordinate_y)/2)
    print(f'{s}')
    print(SHORT_SEPARATOR*"-")

    reverse_a = x/y*(-1)
    print(f'Odwrócony i przeciwny a={round(reverse_a,2)}')
    print(f'{s.coordinate_y}={round(reverse_a,2)}*{s.coordinate_x}+b')
    print(
        f'b=({round(reverse_a,2)}*{round(s.coordinate_x,2)})*(-1)+{round(s.coordinate_y,2)}')
    symetralna_b = reverse_a*s.coordinate_x*(-1) + s.coordinate_y
    print(f'b={round(symetralna_b,2)}')
    print(SHORT_SEPARATOR*"=")
    new_sym = Symetralna(
        name=f'{point_1.name}{point_2.name}', a=reverse_a, b=symetralna_b)
    print(f'{new_sym}')
    print(LONG_SEPARATOR*"_")
    return new_sym


def punkt_przeciecia(symetralna_1, symetralna_2):
    print(LONG_SEPARATOR*"=")
    print(f'Punkt przecięcia: {symetralna_1.name} {symetralna_2.name}')

    print(f'{symetralna_1.short()}\n{symetralna_2.short()}')
    sym_1_x = symetralna_1.a
    sym_1_y = 1
    sym_1_ = symetralna_1.b

    sym_2_x = symetralna_2.a
    sym_2_y = 1
    sym_2_ = symetralna_2.b

    w = det(sym_1_x, sym_1_y, sym_2_x, sym_2_y)
    print(f'W={round(w,2)}')

    wx = det(sym_1_, sym_1_y, sym_2_, sym_2_y)
    print(f'Wx={round(wx,2)}')

    wy = det(sym_1_x, sym_1_, sym_2_x, sym_2_)
    print(f'Wy={round(wy,2)}')

    x = wx/w*(-1)
    print(f'x={round(x,2)}')

    y = wy/w
    print(f'y={round(y,2)}')
    print(LONG_SEPARATOR*"_")


def main():
    print('\nSymetralne oraz punkty przecięcia symetralnych dla\nDiagramu Voronoi dla centrów reprezentowanych przez punkty.')
    print("Wprowadzone punkty:\n", end="")
    punkty = {'A': Punkt(name='A', coordinate_x=3, coordinate_y=-1),
              'B': Punkt(name='B', coordinate_x=2, coordinate_y=1),
              'C': Punkt(name='C', coordinate_x=5, coordinate_y=2),
              'D': Punkt(name='D', coordinate_x=6, coordinate_y=4)
              }
    print(*punkty.values(), sep=';\n', end=".\n")

    print("\nOBLICZAM SYMETRALNE")
    symetralne = {'AB': licz_symetralna(punkty.get('A'), punkty.get('B')),
                  'AC': licz_symetralna(punkty.get('A'), punkty.get('C')),
                  'BC': licz_symetralna(punkty.get('B'), punkty.get('C')),
                  'BD': licz_symetralna(punkty.get('B'), punkty.get('D')),
                  'CD': licz_symetralna(punkty.get('C'), punkty.get('D'))
                  }
    print("Obliczone symetralne dla punktów:\n", end="")
    print(*symetralne.values(), sep=';\n', end=".\n")
    print("KONIEC OBLICZANIA SYMETRALNYCH\n")

    print("OBLICZAM PUNKTY PRZECIĘCIA SYMETRALNYCH")
    punkt_przeciecia(symetralne.get('AB'), symetralne.get('AC'))
    punkt_przeciecia(symetralne.get('BC'), symetralne.get('AC'))
    punkt_przeciecia(symetralne.get('BC'), symetralne.get('CD'))
    punkt_przeciecia(symetralne.get('CD'), symetralne.get('AB'))
    print("KONIEC OBLICZANIA PUNKTÓW PRZECIĘCIA SYMETRALNYCH\n")


if __name__ == '__main__':
    main()
