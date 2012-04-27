#! /usr/bin/env python

from __future__ import division
import sys
from subprocess import call
import timeit


def sh(cmd):
    try:
        call(cmd)
    except:
        pass


def clear():
    sh('find . -name "__pycache__" -delete')
    sh('find . -name "*.pyc" -delete')
    sh('find . -name "*~" -delete')


def main():
    clear()

    if not (len(sys.argv) == 2 or len(sys.argv) == 3):
        print 'usage: run.py n <y>'
        print 'where:'
        print '\tn is the exercise number'
        print '\ty the number of times to measure performance (default 1000)'
        sys.exit(-1)

    m = 1000
    if len(sys.argv) == 3:
        m = int(sys.argv[2])

    problem = __import__('p' + sys.argv[1]).problem
    t = timeit.Timer(stmt=problem.run)
    try:
        print 'avg time: %.5fms' % (1000 * t.timeit(number=m) / m)
        print 'result: ' + str(problem.run())
    except:
        t.print_exc()

    clear()


if __name__ == '__main__':
    main()
