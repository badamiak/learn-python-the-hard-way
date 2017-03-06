from sys import argv
from io import FileIO

Test_file_path = "ex15_sample.txt"

def print_all(file: FileIO):
    print(file.read())

def rewind(file: FileIO):
    file.seek(0)

def print_line(count: int, file: FileIO):
    print("%d:\t %s" %(count, file.readline()))

current_file = open(Test_file_path, "r")

print("First let's print the whole file:")
print_all(current_file)

print("Now let's rewint the file:")
rewind(current_file)

print("Let's print three lines:")
line_count = 1
print_line(line_count, current_file)
line_count = line_count + 1
print_line(line_count,current_file)
line_count = line_count + 1
print_line(line_count,current_file)

current_file.close()