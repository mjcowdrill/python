
def func(**keyword_args):
# -->keyword_args is a dictionary
    print('func:')
    print(keyword_args)
    if keyword_args.has_key('b'): print(keyword_args['b'])
    if keyword_args.has_key('c'): print(keyword_args['c'])

def func2(*positional_args):
# -->positional_args is a tuple
    print('func2:')
    print(positional_args)
    if len(positional_args) > 1:
        print(positional_args[1])

def func3(*positional_args, **keyword_args):
    # It is an error to switch the order ie. def func3(**keyword_args, *positional_args):
    print('func3:')
    print(positional_args)
    print(keyword_args)  # @IndentOk

func(a='apple', b='banana')
func(c='candle')
func2('apple', 'banana')  # It is an error to do func2(a='apple',b='banana')
func3('apple', 'banana', a='apple', b='banana')
func3('apple', b='banana')  # It is an error to do func3(b='banana','apple')