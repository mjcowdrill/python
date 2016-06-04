

def f(x):
    for i in range(10):
        u = unicode("{}\n".format(i))
        x.write(u)


import gzip, io

    
with io.open('x.txt.gz', 'wb') as underlying:
    with gzip.GzipFile(fileobj=underlying, mode='wb') as wrapper:
        f(io.TextIOWrapper(wrapper, 'utf8'))

        
