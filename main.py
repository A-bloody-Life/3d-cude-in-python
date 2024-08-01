# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: <encoding name> -*-
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


class Cube:
    def __init__(self, origin=(0, 0, 0), size=1):
        self.origin = np.array(origin)
        self.size = size
        self.vertices = self._calculate_vertices()

    def _calculate_vertices(self):
        """Вычисляет вершины куба на основе его размера и положения."""
        o = self.origin
        s = self.size
        return np.array([[o[0], o[1], o[2]],
                         [o[0] + s, o[1], o[2]],
                         [o[0] + s, o[1] + s, o[2]],
                         [o[0], o[1] + s, o[2]],
                         [o[0], o[1], o[2] + s],
                         [o[0] + s, o[1], o[2] + s],
                         [o[0] + s, o[1] + s, o[2] + s],
                         [o[0], o[1] + s, o[2] + s]])

    def draw(self):
        """Отображает куб в 3D пространстве."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Определяем грани куба
        faces = [
            [self.vertices[0], self.vertices[1], self.vertices[2], self.vertices[3]],  # нижняя грань
            [self.vertices[4], self.vertices[5], self.vertices[6], self.vertices[7]],  # верхняя грань
            [self.vertices[0], self.vertices[1], self.vertices[5], self.vertices[4]],  # передняя грань
            [self.vertices[2], self.vertices[3], self.vertices[7], self.vertices[6]],  # задняя грань
            [self.vertices[1], self.vertices[2], self.vertices[6], self.vertices[5]],  # правая грань
            [self.vertices[0], self.vertices[3], self.vertices[7], self.vertices[4]],  # левая грань
        ]

        # Рисуем грани
        ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        # Устанавливаем пределы осей
        ax.set_xlim([self.origin[0], self.origin[0] + self.size])
        ax.set_ylim([self.origin[1], self.origin[1] + self.size])
        ax.set_zlim([self.origin[2], self.origin[2] + self.size])

        plt.show()

# Пример использования
cube = Cube(origin=(0, 0, 0), size=1)
cube.draw()
