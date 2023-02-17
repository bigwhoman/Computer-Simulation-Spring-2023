from random import *


def calculate_pi(itterations):
    distinct_points = 0
    generated_points = []
    points_in_circle = 0
    for i in range(itterations):
        x = uniform(-1,1) 
        y = uniform(-1,1) 
        if (x,y) not in generated_points:
            distinct_points += 1
            generated_points.append((x,y))
            if x*x + y*y <= 1 :
                points_in_circle +=1
                
    print(4 * points_in_circle/distinct_points)



if __name__ == '__main__':
    itterations = 100000
    calculate_pi(itterations)