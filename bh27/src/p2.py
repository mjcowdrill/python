import gzip, io

with io.open("x.txt.gz", "rb") as underlying:
    with gzip.GzipFile(fileobj=underlying, mode="rb") as wrapper:
        for line in wrapper:
            x = str(line.decode("utf8"))
            print x[0:-1]

#from getpass import getpass

#getpass()

#import curses

