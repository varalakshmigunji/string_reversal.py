def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string
print(reverse_string("hello"))  
print(reverse_string("cognifyz"))  
print(reverse_string("internship"))