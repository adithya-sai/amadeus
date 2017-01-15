import sys

def val(sex, name):
   
   response = 'You are ' + name + ' and of sex ' + sex
   return response
   
if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = do_something(arg)