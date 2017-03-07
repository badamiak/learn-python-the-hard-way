def createlist(max: int, step: int) -> list:
    numbers = []
    i = 0
    while i < max:
    #   print(f"At start i is {i}")
        numbers.append(i)
        i+=step
    #   print(f"Numbers now: {numbers}")
    #   print(f"At end i is {i}")
    return numbers

def createlist2(max: int, step: int) -> list:
    numbers = []
    for i in range(0,max,step):
        numbers.append(i)
    return numbers
numbers = createlist(10, 2)
print(f"The numbers: {numbers}")

numbers = createlist2(10,2)
print(f"The numbers: {numbers}")