import requests as rq
import sys
from . import *

def get_page(url):
    try:
        page = rq.get(url, timeout=3)
    except Exception as E:
        return -1
    return(page.text)

if __name__ == '__main__':
    if (len(sys.argv) > 1) and (len(sys.argv) < 4):
        if sys.argv[1].startswith("https://") or sys.argv[1].startswith("http://") or sys.argv[1].startswith("http3://"):
            wordict = get_page(sys.argv[1]).split()
        else:
            try:
                with open(sys.argv[1], "r") as f:
                    wordict = f.read().split()
            except Exception as E:
                print("File does not exsit")
        if (len(sys.argv) == 3):
            wordict = [i for i in wordict if len(i) == int(sys.argv[2])]
        res = gameplay(ask, inform, wordict)
        print("Congratulations! Attempts count: ", res)
    else:
        print("Wrong Format")