import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ant import Ant

class Field:
    def __init__(self, size: tuple) -> None:
        x, y = size[0]//2, size[1]//2
        self.ant = Ant([x, y])
        self.field = np.zeros(size, dtype='bool')

    def setfield(self, field: np.array) -> None:
        self.field = np.array

    def step(self) -> None:
        try:
            x, y = self.ant.get_position()
            self.field[x, y] = ~self.field[x, y]
            self.ant.step(self.field[x, y])
        except IndexError:
            pass

    def plot(self) -> None:
        plt.imshow(self.field)
        plt.show()

    def get_next_frame(self, *args, **kwargs) -> np.array:
        self.step()
        return self.field
