import numpy as np


class Ant:
    """ant"""
    def __init__(self, position: np.array, direction: np.array = np.array([1,0])) -> None:
        self._position = position
        self._direction = direction

    def get_position(self):
        """retrun current position of ant"""
        return self._position

    def step(self, cell_under: bool):
        "create one step"
        self.change_direction(cell_under)
        self._position += self._direction

    def change_direction(self, cell_under_ant: bool) -> None:
        "change directory of movement by cell under ant"
        left = np.array([[0, -1], [1, 0]])
        right = np.array([[0, 1], [-1, 0]])
        direction = self._direction
        if cell_under_ant:
            self._direction = np.dot(direction, right)
        else:
            self._direction = np.dot(direction, left)
