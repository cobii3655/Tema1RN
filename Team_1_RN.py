import pathlib
import math

def load_system(path: pathlib.Path) -> tuple[list[list[float]], list[float]]:

  A, B = [], []
  for i in path.read_text().strip().splitlines():
    if not i:
      continue
    st, dr = i.split("=")
    B.append(float(dr))

    save = []
    terms = (st.replace(" ", "").replace("-", "+-").strip("+").split("+"))

    for t in terms:
      val = t.split("*")[0]
      save.append(float(val))

    A.append(save)

  return A, B

A, B = load_system(pathlib.Path("system.txt"))
print(f"{A=} {B=}")

def determinant(matrix: list[list[float]]) -> float:
    x1 = 1
    x2 = 1
    A = matrix
    x1 = (A[0][0]*A[1][1]*A[2][2]+A[1][0]*A[2][1]*A[0][2]+A[0][1]*A[1][2]*A[2][0])
    x2 = (A[0][2]*A[1][1]*A[2][0]+A[0][0]*A[1][2]*A[2][1]+A[0][1]*A[1][0]*A[2][2])

    return x1-x2

print(f"{determinant(A)=}")


def trace(matrix: list[list[float]]) -> float:
    A = matrix
    Trace = A[0][0]+A[1][1]+A[2][2]

    return Trace

print(f"{trace(A)=}")

def norm(vector: list[float]) -> float:
  B = vector
  norma = math.sqrt(B[0] * B[0] + B[1] * B[1] + B[2] * B[2])
  return norma

print(f"{norm(B)=}")

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    A = matrix
    c1 = [A[0][0], A[1][0], A[2][0]]
    c2 = [A[0][1], A[1][1], A[2][1]]
    c3 = [A[0][2], A[1][2], A[2][2]]

    return [c1,c2,c3]

print(f"{transpose(A)=}")


def multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    A = matrix
    B = vector

    rez1 = A[0][0]*B[0]
    rez2 = A[0][1]*B[1]
    rez3 = A[0][2]*B[2]

    return [rez1,rez2,rez3]

print(f"{multiply(A, B)=}")

def solve_cramer(matrix: list[list[float]], vector: list[float]) -> list[float]:

    x = 0
    A = matrix
    B = vector

    c1 = [A[0][0], A[1][0], A[2][0]]
    c2 = [A[0][1], A[1][1], A[2][1]]
    c3 = [A[0][2], A[1][2], A[2][2]]

    Ax = [[B[0], c2[0], c3[0]], [B[1], c2[1], c3[1]], [B[2], c2[2], c3[2]]]
    Ay = [[c1[0], B[0], c3[0]], [c1[1], B[1], c3[1]], [c1[2], B[2], c3[2]]]
    Az = [[c1[0], c2[0], B[0]], [c1[1], c2[1], B[1]], [c1[2], c2[2], B[2]]]


    detA = determinant(A)
    detAx = determinant(Ax)
    detAy = determinant(Ay)
    detAz = determinant(Az)

    x = detAx/detA
    y = detAy/detA
    z = detAz/detA


    return [x,y,z]

print(f"{solve_cramer(A, B)=}")


def minor(matrix: list[list[float]], i: int, j: int) -> list[list[float]]:
  sub = []
  for r in range(3):
    if r != i:
      temp = []
      for c in range(3):
        if c != j:
          temp.append(matrix[r][c])
      sub.append(temp)
  return sub

def cofactor(matrix: list[list[float]]) -> list[list[float]]:
  cof = []
  for i in range(3):
    temp = []
    for j in range(3):
      m = minor(matrix, i, j)
      det_m = m[0][0] * m[1][1] - m[0][1] * m[1][0]
      val = ((-1) ** (i + j)) * det_m
      temp.append(val)
    cof.append(temp)

  return cof

def adjoint(matrix: list[list[float]]) -> list[list[float]]:
  A = matrix
  c = cofactor(A)
  adj = [[c[0][0], c[1][0], c[2][0]], [c[0][1], c[1][1], c[2][1]],[c[0][2], c[1][2], c[2][2]]]

  return adj

def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
  A = matrix
  B = vector
  detA = determinant(A)
  adjA = adjoint(A)

  invA = [[adjA[r][c] / detA for c in range(3)] for r in range(3)]

  x = invA[0][0] * B[0] + invA[0][1] * B[1] + invA[0][2] * B[2]
  y = invA[1][0] * B[0] + invA[1][1] * B[1] + invA[1][2] * B[2]
  z = invA[2][0] * B[0] + invA[2][1] * B[1] + invA[2][2] * B[2]

  return [x, y, z]

print(f"{solve(A, B)=}")