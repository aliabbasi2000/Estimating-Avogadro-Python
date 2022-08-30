
class Blob:
    '''
    Blob is an object that each Blob at least have 25pixels(min_pixels)
    and minimum luminance of Blob is 180(tau)
    '''

    def __init__(self):
        self.center = [0, 0]
        # list of center coordinates
        self.pixels = []
        # coordinates of blob's pixels [(x, y)]

    def add(self, x, y):
        '''
        this function add the pixel with coordination(x, y) to the Blob
        '''

        # update the center
        self.center[0] = (self.center[0] * self.mass() + x) / (self.mass() + 1)
        self.center[1] = (self.center[1] * self.mass() + y) / (self.mass() + 1)
        self.pixels.append((x, y))

    def mass(self):
        '''
        Returns the number of Blobs pixels
        '''
        return len(self.pixels)

    def distanceTo(self, c):
        '''
        Returns distance between two Blobs
        '''
        dx = (c.center[0] - self.center[0]) ** 2
        dy = (c.center[1] - self.center[1]) ** 2
        return (dx + dy) ** 0.5
    
    def __str__(self):
        '''
        Returns the number of Blobs pixels and the coordination of Blobs center
        '''
        return str(self.mass()) + ' (%s, %s)' % (str(self.center[0]), str(self.center[1]))

if __name__ == '__main__':
    b = Blob()

    print(b)
    tau = 180
    # color threshold
    min_pixels = 25
    # min of pixels to make a blob

