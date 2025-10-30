# Args Kwargs Demo.py
# Demonstrate *args and **kwargs usage.

def printer(*args, **kwargs):
    print("ARGS:", args)
    print("KW:", kwargs)

if __name__ == '__main__':
    printer(1,2,3, a=10, b=20)

