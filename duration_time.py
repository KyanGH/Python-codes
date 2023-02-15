def mainq2():
    #Get user input
    start_hour = int(input("Enter the hour of start time: "))
    start_minute = int(input("Enter the minutes of start time: "))
    #Check user input, if input is correct continue
    if start_hour > 23 or start_minute > 59 :
        print("Wrong input")
    else :
        stop_hour = int(input("Enter the hour of stop time: "))
        stop_minute = int(input("Enter the minutes of stop time: "))
    #Check user input, if input is correct continue
        if stop_hour > 23 or stop_minute > 59 :
            print("Wrong input")
        else :
            #Calculate the duration
            hour = stop_hour - start_hour
            minute = stop_minute - start_minute
            #Conver into time units
            if minute < 0 :
                minute += 60
                hour -= 1
            if hour <= 0 :
                hour += 24
            #Check if duration is longer than 24 hours!
            if hour >= 24 :
                print("Duration time can't be longer than 24 hours!")
            else:
                #print duration
                print("The duration is : %d hours, %d minutes" %(hour,minute))
    
    
mainq2()