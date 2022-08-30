
import sys
from beadfinder import BeadFinder
from picture import Picture
import glob


def main():
    # get inputs
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    # the distance that each blob goes from one frame to another one should be less than delta
    delta = float(sys.argv[3])
    # put inputs in A and A is a list
    A = glob.glob(sys.argv[4])
    frame = Picture(A[0])

    # instantiate the beadfinder object
    bf = BeadFinder(frame, tau)
    prev_beads = bf.getBeads(min_pixels)

    # read each frame from commandline and compare with the previous frame
    for i in range(1, len(A)):
        curr_frame = Picture(A[i])
        bf = BeadFinder(curr_frame, tau)
        curr_beads = bf.getBeads(min_pixels)
        for curr_bead in curr_beads:
            min_distance = float('inf')
            for prev_bead in prev_beads:
                d = curr_bead.distanceTo(prev_bead)
                if d <= delta and d < min_distance:
                    min_distance = d
            if min_distance != float('inf'):
                print('%0.4f' % min_distance)
        if i < (len(A) - 1):
            print()

        prev_beads = curr_beads


if __name__ == '__main__':
    main()






