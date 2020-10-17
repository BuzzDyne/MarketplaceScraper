import sys

import app

"""
    Must be called with either one of two params
        --update    = to update listing data
        --create    = to retrieve new listing data (Continouosly)
"""

def checkArgs():
    argsCount = len(sys.argv)

    if(argsCount != 2):
        print("One and only one argument required!")
    else:
        if(sys.argv[1] == "--update"):
            print('daily')
        elif(sys.argv[1] == "--create"):
            print('cont')
        else:
            print("Wrong argument!\n('--update' or '--create'")

if __name__ == '__main__':
  checkArgs()
