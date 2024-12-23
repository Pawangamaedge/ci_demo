from src.maths_operations import Algebra, Geometry
import pytest

class Testing_algebra:
     def test_algebra_square(self):
          assert Algebra.square(20) == 400
          assert Algebra.square(10) == 100
          assert Algebra.square(9) == 81
          assert Algebra.square(7) == 49

     def test_algebra_cube(self):
          assert Algebra.cube(2) == 8
          assert Algebra.cube(4) == 64
     
     def test_algebra_add(self):
          assert Algebra.add(2,3) == 5
          assert Algebra.add(5,10) == 15

class Testing_geometry:
     def test_is_triangle(self):
          assert Geometry.is_triangle(120, 40, 20) == True
          assert Geometry.is_triangle(45, 67, 99) == False

     def test_is_quadrilateral(self):
          assert Geometry.is_quadrilateral(350, 5, 5, 0) == True
          assert Geometry.is_quadrilateral(11, 22, 33, 44) == False

