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