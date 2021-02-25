import sys
from mainGaussianBlurentry import *
from mainGaussianBlurexit  import *
import detect1

if __name__== '__main__':
    argument = sys.argv
    del argument[0]

a, b = detect1.detect()


print('Empty   : {:03d}'.format(a))
print('Occupied : {:03d}'.format(b))

print('# of Entry : {:03d}'.format(entry))
print('# of Exit  : {:03d}'.format(exit))