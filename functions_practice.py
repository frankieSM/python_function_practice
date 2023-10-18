#PPP-1
def hello():
    print("Hello")


def pack(one, two, three):
    list = [one, two, three]
    return list

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First i eat " + list[0])
        for item in list[1:]:
            print("Next I eat " + item)

hello()
print(pack(1,2,3))
eat_lunch(["one","two","three","four"])

#PPP-2
def max_num(numbers):
    return max(numbers)
    

def mult_list(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def rev_string(string):
    result = string[::-1]
    return result

def num_within(num, beginning, end):
    if num > beginning and num < end:
        return True
    else: 
        return False

def pascal(n):
    for row in range(1, n + 1):
        for space in range(0, n - row + 1):
            print(' ', end='')
        current_element = 1
        for element_position in range(1, row + 1):
            print(' ', current_element, sep='', end='')
            current_element = current_element * (row - element_position) // element_position
        print()


print(max_num([1,5,10]))
print(mult_list([1,2,3,4,5]))
print(rev_string('word'))
print(num_within(5,10,15))
print(num_within(5,1,15))
print(pascal(10))