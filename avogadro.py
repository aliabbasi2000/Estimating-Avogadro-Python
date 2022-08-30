
import math
import sys


def main():
    '''
    Variables:
         var: Self propagation D
         eta: viscosity of water at room temperature
         rho: The Radius of Beads
         T: Absolute temperature
         R: Universal gas constant
         k: Boltzmann's constant
         N_A: Avogadro's number
         s: Sigma ** 2
    '''

    n = 0
    s = 0.00
    # read data
    for line in sys.stdin:
        try:
            # Change data units from pixel to meter
            a = float(input()) * (0.175 * (10 ** -6))
            s += a * a
            n += 1
        except ValueError:
            pass

    var = s / (2 * n)
    eta = 9.135 * (10 ** -4)
    rho = 0.5 * (10 ** -6)
    T = 297.0
    R = 8.31446
    k = 6 * math.pi * var * eta * rho / T
    N_A = R / k

    print('Boltzmann = %0.4e' % k)
    print('Avogadro = %0.4e' % N_A)


if __name__ == '__main__':
    main()
