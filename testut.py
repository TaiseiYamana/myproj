import unittest
import calc

import numpy as np

a = np.array([1,2,4])
b = np.array([5,4,6])


def CROSS(A,B):
    C = np.array([0,0,0])
    C[0] = A[1]*B[2]-B[1]*A[2]
    C[1] = -1*(A[0]*B[2]-B[0]*A[2])
    C[2] = A[0]*B[1]-B[0]*A[1]
    return C
class TestCalc(unittest.TestCase):
  def test_cross(self):
      self.assertEqual(np.cross(a, b)[0],CROSS(a,b)[0])
      self.assertEqual(np.cross(a, b)[0],CROSS(a,b)[1])
      self.assertEqual(np.cross(a, b)[2],CROSS(a,b)[2])
