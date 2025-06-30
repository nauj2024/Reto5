from ejercicio1.Shape1.shapes import Point, Rectangle, Square, Triangle, Isosceles, Equilateral, Scalene, TriRectangle

# puntos
p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(2, 3.464) 
p4 = Point(4, 3)
p5 = Point(0, 3)

# rectangulo
rect = Rectangle(p1, 4, 3)
print("Rectángulo:")
print("  Área:", rect.compute_area())
print("  Ángulos:", rect.compute_inner_angles())
print()

# cuadrado
square = Square(p1, 4)
print("Cuadrado:")
print("  Área:", square.compute_area())
print("  Ángulos:", square.compute_inner_angles())
print()

# triangulo
tri = Triangle(p1, p2, p4)
print("Triángulo:")
print("  Área:", tri.compute_area())
print("  Ángulos:", tri.compute_inner_angles())
print()

# triangulo equilatero
eq = Equilateral(p1, p2, p3)
print("Triángulo Equilátero:")
print("  Área:", eq.compute_area())
print("  Ángulos:", eq.get_angles())
print()

# triangulo isoseles
iso = Isosceles(p1, p5, Point(2, 3))
print("Triángulo Isósceles:")
print("  Área:", iso.compute_area())
print("  Ángulos:", iso.compute_inner_angles())
print()

# triangulo escaleno
sca = Scalene(p1, Point(1, 4), Point(5, 2))
print("Triángulo Escaleno:")
print("  Área:", sca.compute_area())
print("  Ángulos:", sca.compute_inner_angles())
print()

# triangulo rectangulo
tri90 = TriRectangle(p1, p2, p5)
print("Triángulo Rectángulo:")
print("  Área:", tri90.compute_area())
print("  Ángulos:", tri90.get_angles())
print()

