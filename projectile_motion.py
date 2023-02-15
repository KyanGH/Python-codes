import math
#Recieve angle a and turn it into radian
def deg2rad(a):
    return a * (math.pi / 180)
#Recieve angle,velocity and time and calculate hight of object based on time
def height(a,v,t):
    return (v * math.sin(deg2rad(a))) * t - (9.81 * t**2) / 2
#Recieve velocity,angle and time and calculate distance of object baed on time
def horizontal(v,a,t):
    return (v * math.cos(deg2rad(a))) * t

def main():
    t = 0.1
    H = 1
    #Get speed from user iput
    v = float(input("Enter speed 0-100 (m/s): "))
    #check user input
    if v < 0 or v > 100 :
        print("Finish")
    else:
        #Get angle from user input
        a = float(input("Enter angel 0-90 (degrees): "))
        #Check user input
        if a < 0 or a > 90 :
            print("Finish")
        else:
            #Calculate and print object hight and distance based on time
            #by using two built functions
            while v >= 0 and v <101 and a >= 0 and a < 91 and H > 0 :
                H = height(a,v,t)
                S = horizontal(v,a,t)
                #print calculations
                print("Time:%.1f"%t,"S=%.2f"%S,"H=%.2f"%H)
                t += 0.1
            print("Fallen!")

main()
    
