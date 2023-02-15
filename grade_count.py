def main():
    count = 0
    count_pass = 0
    grade = int(input("Enter grade, end with -1 :"))
    while grade != -1 :
        count += 1
        if grade >= 55 :
            print("%.2F"%grade)
            count_pass += 1
        grade = int(input("Enter grade, end with -1 :"))
    print("%.2F"%((count_pass/count)*100))
main()