
#reverse a string

def reverse(str):

    str = str.split(" ")
    print str

    stack = []

    for i in str:
        stack.append(i)
    while stack:
        print "".join(stack.pop()),



reverse("this is reversed")
