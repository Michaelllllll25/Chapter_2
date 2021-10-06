"""
- Import while file
- Import specific function(s)
"""
import math_funcs                      # dont put .py
# or
#from math_funcs import add, mult         # would then take out the math_funcs.

def main():
    print("Hello from main.py")

    result1 = math_funcs.add(5, 7)     # need to refer to the package (math_funcs.)
    print(f"5 + 7 = {result1}")

    result2 = math_funcs.mult(11, 16)   # need to refer to the package (math_funcs.)
    print(f"11 * 16 = {result2}")

if __name__ == "__main__":
    main()
