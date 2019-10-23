
import one
print("TOP LEVEL TWO.PY")
one.func()


if __name__ == '__main__':
    print("Two.py being run directly")
else:
    print("two is being imported")

# OUTPUT:
# TOP LEVEL ONE.PY
# one.py has been imported
# TOP LEVEL TWO.PY
# func() in one.py
# Two.py being run directly
