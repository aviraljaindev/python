def odd(num):
    if num % 2 != 0:
        return "Weird"
    else:
        return even(num)

def even(num):
    if 2 <= num <= 5:
        return "Not Weird"
    elif 6 <= num <= 20:
        return "Weird"
    elif num > 20:
        return "Not Weird"

N = int(input())
print(odd(N))