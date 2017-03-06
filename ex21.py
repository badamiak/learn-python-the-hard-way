def add(a: int, b: int) -> int:
    print(f"Adding {a} + {b}")
    return a+b

def subtract(a: int, b: int) -> int:
    print(f"Subtract {a} - {b}")
    return a-b

def multiply(a: int, b: int) -> int:
    print(f"Multiply {a} * {b}")
    return a*b

def divide(a:int, b: int) -> float:
    print(f"Divide {a} / {b}")
    return a/b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}")

print("here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print(f"That becomes: {what}, can you do it by hand")