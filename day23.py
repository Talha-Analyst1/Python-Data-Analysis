#Default Arguments(using for defualt value preventing from error)
def sum_of(*nums):
    total=sum(nums)
    print(total)
sum_of(9+3+4+6)

#(example "i need 4 cricket players score(45, 60, 33, 80)Total)")

def add_all(*scores):
    total=sum(scores)
    count=len(scores)
    print(total)
add_all(45, 60, 33, 80) 