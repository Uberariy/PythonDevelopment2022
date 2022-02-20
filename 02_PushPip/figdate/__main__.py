import time
import pyfiglet
import sys
import locale

def date(form = "%Y %d %b, %A", shrft = "graceful"):
    #locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
    f = pyfiglet.Figlet(font = shrft)
    return(f.renderText(time.strftime(form, time.gmtime())))

if __name__ == '__main__':
    if (len(sys.argv) >= 1) and (len(sys.argv) <= 3):
        print(date(*sys.argv[1:]))
    else:
        print("Wrong Format")