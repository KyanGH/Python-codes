def main_3():
    # Getting user input
    num_children = int(input('Enter number of children: '))
    salary = int(input('Enter your monthly salary: '))
    army = input('Military or civil service? (y/n): ').lower()[:1] == 'y'
    
    # Checking 3 conditions
    cond1 = army and salary >= 15000
    cond2 = num_children >= 5 and salary >= 14000
    cond3 = salary > 17500
    
    # Printing the appropriate message
    if not (cond1 or cond2 or cond3):
        print('The mortgage is not approved.')
    elif cond3:
        mortgage = salary * 0.35
        print('The mortgage is approved with a monthly payment of %d.' % mortgage)
    elif cond1 or cond2:
        mortgage = salary * 0.25
        print('The mortgage is approved with a monthly payment of %d.' % mortgage)
main_3()