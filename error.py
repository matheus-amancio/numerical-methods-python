# module error
''' err(string).
    Imprime 'string' e encerra o programa.
'''
import sys


def err(string):
    print(string)
    input('Press return to exit')
    sys.exit()
