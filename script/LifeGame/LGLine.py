
from .LifeGameGui import LifeGameGui, default_quick_fname
import itertools


class LifeGameGui_Base(LifeGameGui):
    def __init__(self, size, scale, nbegin, nsteps, quick_fname):
        LifeGameGui.__init__(self, size, scale, \
                             self.generator(nbegin), \
                             nsteps, quick_fname)

class LifeGameGui_Line(LifeGameGui_Base):
    def generator(self, nbegin):
        return (set((x, 0) for x in range(i)) \
                for i in itertools.count(nbegin))


class LifeGameGui_Cross(LifeGameGui_Base):
    def generator(self, nbegin):
        return (set(xy for z in range(i) for xy in [(-z, 0), (z,0), (0,-z), (0,z)]) \
                for i in itertools.count(nbegin))


class LifeGameGui_L(LifeGameGui_Base):
    def generator(self, nbegin):
        return (set(xy for z in range(i) for xy in [(z,0), (0,z)]) \
                for i in itertools.count(nbegin))




names = ['Line', 'Cross', 'L']
def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='Life Game - {}'.format(' '.join(names)))

    parser.add_argument('-b', '--begin', type=int, \
                        nargs='?', default=3,
                        help='to determine the number of lives in the first game')
    
    parser.add_argument('-s', '--scale', type=int, \
                        nargs='?', default=3,
                        help='the size of each life on screen')

    parser.add_argument('--nsteps', type=int, \
                        nargs='?', default=100,
                        help='skip next <nsteps> states while middle mouse clicked')

    parser.add_argument('-q', '--quick', type=str, \
                        nargs='?', default=default_quick_fname,
                        help='file name for quick save/load')
    
    parser.add_argument('-W', '--width', type=int, \
                        nargs='?', default=800,
                        help='window width')

    parser.add_argument('-H', '--height', type=int, \
                        nargs='?', default=600,
                        help='window height')
    
    parser.add_argument('-P', '--pattern', type=str, choices=names, \
                        nargs='?', default='Line',
                        help='game pattern')

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    args.size = args.width, args.height
    lg = eval('LifeGameGui_' + args.pattern)(args.size, args.scale, args.begin, args.nsteps, args.quick)
    
    sys.exit(lg.run())

if __name__ == "__main__":
    main()
