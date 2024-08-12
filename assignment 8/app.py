# Part A
myList = [1, 2, 3, 4, 5, 6, 7, 8]
myList2 = myList[1:]
myList3 = myList2.copy()
myList3.append(9)
myList3.pop(2)

# Part B
# count(sub,[start,[end]])
print(myList3.count(3))

# endswith(suffix,[start,[end]])
print("abcde".endswith("de"))

# find/index(sub,[start,[end]])
print("hello".find("e"))

# join()
print(",".join(["a", "b", "c"]))

# replace(old,new[,count])
print("hello".replace("e", "i"))

# split([sep[,maxsplit]])
print("a,b,c,d".split(","))

# splitlines([keepends])
print("line1\nline2".splitlines())

# startswith(prefix[,start[,end]])
print("hello".startswith("he"))

# strip([chars])
print("  hello  ".strip())

# Part C
def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

user_input = int(input("Enter a number: "))
if check_prime(user_input):
    print(f"{user_input} is a prime number")
else:
    print(f"{user_input} is not a prime number")

# Part D
def disStuInfo(schoolID, *firstName, **lastEmail):
    for i in range(len(firstName)):
        if i < len(lastEmail):
            print(f"{schoolID}{firstName[i]}{lastEmail[i]}")
        else:
            print(f"{schoolID}'unmatched'")

disStuInfo(10001, 'John', 'Smith', email1='jSmith@gmail.com', email2='Petter@yahoo.com', email3='j@gmail.com')