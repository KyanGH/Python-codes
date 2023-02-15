name = str(input("Enter your charchter name :"))
master = 'Rex'
classtype = str(input("Choose class type Trooper or Jedi :"))
if classtype.lower() == 'jedi' :
    master = str(input("Whos is your master :"))
    leadertype = 'master'
else:
    while master == 'Rex' or master == 'rex':
        master = str(input("Whos is your captain :"))
        if master == 'Rex' or master == 'rex' :
            print('Captain Rex is unavailable')
        leadertype = 'Commander'
    
message = "Hello {classtype} {name}, I'm Captain CT-7567, Rex in short. // You have been assigned a mission by {leadertype} {master} to take back Lothal".format(name = name, master = master, classtype = classtype, leadertype = leadertype)
print (message)