from schemas import Vector, Matriz
from typing import List
from copy import deepcopy
import numpy as np


def gram_schmidt(
    vectors: List[Vector], ortonormalize: List[Vector] | None = None
) -> List[Vector]:
    if ortonormalize is None:
        ortonormalize = []
    elif len(vectors) == 0:
        ortonormalize = list(map(lambda i: round(i, 4), ortonormalize))
        return ortonormalize

    v = vectors[0]
    del vectors[0]
    if v.is_vector_zero():
        return gram_schmidt(vectors, ortonormalize)
    if len(ortonormalize) == 0:
        v = v.normalize()
        ortonormalize.append(v)

        return gram_schmidt(vectors, ortonormalize)

    u = deepcopy(v)
    for w in ortonormalize:
        u = u - (w * (v * w))

    if u.is_vector_zero():
        return gram_schmidt(vectors, ortonormalize)

    u: Vector = u.normalize()

    ortonormalize.append(u)
    return gram_schmidt(vectors, ortonormalize)


def inverse(M: Matriz) -> Matriz:
    tmp = []
    for i in M._rows:
        tmp.append(i._values)
    A = np.array(tmp)
    tmp = []
    A = np.linalg.inv(A)
    for i in A:
        tmp.append(Vector(i))
    return Matriz(tmp)
