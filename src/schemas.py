from typing import List


class Vector:
    def __init__(self, values: list) -> None:
        self._components: int = len(values)
        assert len(values) == self._components
        self._values = values

    def __getitem__(self, component: int) -> int:
        return self._values[component]

    def __setitem__(self, component: int, value: int):
        assert type(value) == int
        self._values[component] = value

    def __add__(self, u):
        assert isinstance(u, Vector)
        assert self._components == u._components
        resultado = [a + b for a, b in zip(self._values, u.values)]
        return Vector(resultado)

    def __sub__(self, u):
        assert isinstance(u, Vector)
        assert self._components == u._components
        resultado = [a - b for a, b in zip(self._values, u.values)]
        return Vector(resultado)

    def __mul__(self, u):
        if isinstance(u, int) or isinstance(u, float):
            resultado = [a * u for a in self._values]
            return Vector(resultado)

        assert isinstance(u, Vector)
        assert self._components == u._components
        resultado = sum([a * b for a, b in zip(self._values, u.values)])
        return resultado

    def __len__(self):
        return self._components

    def __str__(self) -> str:
        return f"Vector({self._values})"

    def __repr__(self) -> str:
        return f"Vector({self._values})"

    def __abs__(self):
        norma2 = self * self
        return norma2 ** (1 / 2)

    def __round__(self, v):
        resultado = [round(a, v) for a in self._values]
        return Vector(resultado)

    def normalize(self):
        return self * (1 / abs(self))

    def is_vector_zero(self):
        v = round(self, 2)
        return all(list(map(lambda i: i == 0, v._values)))

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values: list):
        assert len(values) == self._components
        self._values = values


class Matriz:
    def __init__(self, rows: List[Vector]) -> None:
        assert all(list(map(lambda i: len(i) == len(rows[0]), rows)))

        self._rows = rows
        self.shape = (len(rows), rows[0]._components)

    def transpose(self):
        tmp = []
        for i in range(self.shape[1]):
            v = self[:, i]
            tmp.append(v)
        return Matriz(tmp)

    def __getitem__(self, pos):
        assert len(pos) == 2
        row, col = pos

        if not isinstance(row, int) and not isinstance(col, int):
            mrow = self._rows[row]
            tmp = []
            for k, i in enumerate(mrow):
                tmp.append(Vector(i[col]))
            return Matriz(tmp)
        elif not isinstance(row, int):
            mrow = self._rows[row]
            tmp = []
            for k, i in enumerate(mrow):
                tmp.append(i[col])

            return Vector(tmp)

        elif not isinstance(col, int):
            mrow = self._rows[row]
            return Vector(mrow[col])

        mrow = self._rows[row]
        value = mrow[col]
        return value

    def __str__(self) -> str:
        s = "Matriz(\n"
        for i in self._rows:
            s += str(i._values) + "\n"
        s += ")"

        return s

    def __matmul__(self, u):
        if isinstance(u, Vector):
            b = Matriz([u])
            b = b.transpose()

            return self @ b
        ut = u.transpose()
        new_rows = []
        for row in self._rows:
            tmp = []
            for col in ut._rows:
                tmp.append(col * row)
            new_rows.append(Vector(tmp))
        return Matriz(new_rows)

    def __round__(self, d=1):
        tmp = []
        for row in self._rows:
            tmp.append(round(row, d))
        return Matriz(Vector(tmp))
