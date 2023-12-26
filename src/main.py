import numpy as np

from algorithm import gram_schmidt, inverse
from schemas import Vector, Matriz


M = Matriz(
    [
        Vector([1, 1, 1]),
        Vector([1, 2, 1]),
        Vector([0, 2, 1]),
    ]
)

vectors = gram_schmidt(M.transpose()._rows)
QT = Matriz(vectors)

v = Vector([4, 5, 3])

R = QT @ M
IR = inverse(R)
Q = QT.transpose()

print((IR @ QT) @ v)
