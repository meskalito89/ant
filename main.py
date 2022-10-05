from field import Field
from ant import Ant
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import argparse
import pdb
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script create animation of Langton's ant")
    parser.add_argument('width', type=int, help='width of field')
    parser.add_argument('height', type=int, help='heigh of field')
    parser.add_argument('n_of_frames', type=int, help='count of frame in gif file')
    parser.add_argument('output_file', type=str, default='animation.gif', help='output_file.gif')
    parser.add_argument('-f', type=int, help='fps for gif file')
    args = parser.parse_args()

    size = (args.width, args.height)

    field = Field(size)

    fig = plt.figure()
    subplot = fig.add_subplot()
    

    def a(i):
        # pdb.set_trace()
        next_field = field.get_next_frame()
        image = plt.imshow(next_field, vmin=0., vmax=1.)
        return image.set_array(next_field)
        

    anim = FuncAnimation(fig, a, frames=args.n_of_frames)
    anim.save(args.output_file, fps=5)

