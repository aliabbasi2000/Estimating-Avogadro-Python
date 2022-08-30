
import sys
import luminance
import stdarray
import stdio
from blob import Blob
from picture import Picture


class BeadFinder:

    def __init__(self, picture, tau):

        self.img = picture
        self.tau = tau

        # list of blobs
        self.blobs = []

        # create visited array with the same shape of image
        visited = stdarray.create2D(self.img.width(), self.img.height(), False)

        # want to find blobs recursively
        for i in range(self.img.width()):
            for j in range(self.img.height()):
                pixel = self.img.get(i, j)
                if luminance.luminance(pixel) >= self.tau:
                    blob = Blob()
                    self.fsa(self.img, i, j, visited, blob)
                    if blob.mass() > 0:
                        self.blobs.append(blob)

    def fsa(self, img, i, j, visited, blob):
        '''
        first search algorithm to find connected parts
        '''

        if i < 0 or j < 0 or i >= img.width() or j >= img.height() or visited[i][j] == True or luminance.luminance(img.get(i, j)) < self.tau:
            return

        visited[i][j] = True

        # add (i,j) to this blob
        blob.add(i, j)

        # each pixel four neighbors
        row_nbr = [-1, 1, 0, 0]
        col_nbr = [0, 0, 1, -1]

        # recursively call for each neighbor
        for nbr in range(4):
            self.fsa(img, i + row_nbr[nbr], j + col_nbr[nbr], visited, blob)

    def getBeads(self, min_pixels):

        beads = []
        for i in self.blobs:
            if i.mass() >= min_pixels:
                beads.append(i)
        return beads


def main():
    
    min_pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    img = Picture(sys.argv[3])

    # create beadfinder object
    bf = BeadFinder(img, tau)
    beads = bf.getBeads(min_pixels)

    print('number of beads with min_pixel (%s) %s ' % (str(min_pixels), str(len(beads))))
    for i in beads:
        print(str(i))
    

if __name__ == '__main__':
    main()
