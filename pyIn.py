import sys

def pyIn(l, s):
    if l == "%s":
        get = input(s)
        return get
    elif l == "%i":
        while True:
            try:
                 geti = int(input(s))
                 return geti
            except ValueError:
                 print("Please Enter A Valid Number")
                 continue                     

    elif l == "%f":
        while True:
            try:
                getf = float(input(s))
                return getf
            except ValueError:
                print("Please Enter A Valid Float Number")
                continue

        
