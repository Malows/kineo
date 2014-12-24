form sympy import *
""" Abstraccion de movimiento cinematico en cualquier eje, X, Y o Z """
class Movimiento_cinematico:
    def __init__(self):
        self._pos_ini = None
        self._pos_fin = None
        self._vel_ini = None
        self._vel_fin = None
        self._acel = None
        self._tiempo = None

        self.ecuacion_posicion = expr()
        self.ecuacion_velocidad = expr()

    @def tiempo():
        doc = "The tiempo property."
        def fget(self):
            if self._tiempo is not None:
                return self._tiempo
            elif:

            else:

        def fset(self, value):
            if value >= 0:
                self._tiempo = value
            else:
                raise ValueError("El tiempo no puede ser una variable negativa")
        def fdel(self):
            del self._tiempo
        return locals()
    tiempo = property(**tiempo())

    @def