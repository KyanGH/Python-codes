def all_even(num):
    if num == 0:
        return True
    if num % 2 == 1:
        return False
    return all_even(num//10)

def count_even(num):
    if num == 0:
        return 0
    if num % 2 == 0:
        return 1 + count_even(num//10)
    return count_even(num//10)

def main():
    print(all_even(3463))
    print(count_even(3463))
main()