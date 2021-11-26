import matplotlib.pyplot as plt
import numpy as np
power_axle_weight = 21
power_car_axle = 4
power_car = 2
power_car_length = 20
tender_axle_weight = 19
tender_car_axle = 2
tender_car = 2
tender_car_length = 0
passenger_axle_weight = 9
passenger_car_axle = 4
passenger_car = 8
passenger_car_length = 23
total_length = power_car*power_car_length+tender_car*tender_car_length+passenger_car*passenger_car_length
total_weight_trailer = tender_car*tender_axle_weight*tender_car_axle+passenger_car*passenger_axle_weight*passenger_car_axle
total_weight_power = power_car*power_axle_weight*power_car_axle
total_weight = total_weight_power+total_weight_trailer
width = 3.1
height = 3.8
csa = width*height
peri = (width+height)*2
drag_coefficient = 0.15
gap = 0.5
bogie_drag = 0.3
cars = passenger_car+power_car+tender_car
target_slope = 0.033
mode = 'speed'
transmission = 'diesel'
if mode == 'power':
    target_speed = 276/3.6
    A = 6.4*total_weight_trailer+8*total_weight_power
    C = 0.6125*drag_coefficient*csa+0.00197*peri*total_length+0.0021*peri*gap*(cars-1)+0.2061*bogie_drag*2*cars
    power = []
    calculated_power = []
    for i in range (0, 10000, 1):
        power.append(i)
    for i in range(len(power)):
        B = 0.18*total_weight+passenger_car+0.005*power_car*power[i]
        total_drag = (A+B*target_speed+C*target_speed*target_speed)/1000+total_weight*9.81*target_slope
        temp = total_drag*target_speed
        calculated_power.append(temp)
        if abs(temp-power[i])<0.5:
            if transmission == 'steam':
                print(round(power[i]))
            elif transmission == 'diesel':
                print(round(power[i]/0.78))
            elif transmission == 'electric':
                print(round(power[i]/0.86))
elif mode == 'speed':
    target_power = 7320
    if transmission == 'steam':
        real_power = target_power
    elif transmission == 'diesel':
        real_power = target_power*0.78
    elif transmission == 'electric':
        real_power = target_power*0.86
    speed = []
    calculated_speed = []
    A = 6.4*total_weight_trailer+8*total_weight_power
    B = 0.18*total_weight+passenger_car+0.005*power_car*real_power
    C = 0.6125*drag_coefficient*csa+0.00197*peri*total_length+0.0021*peri*gap*(cars-1)+0.2061*bogie_drag*2*cars
    for i in np.arange(0, 100, 0.01):
        speed.append(i)
    for i in range(len(speed)):
        total_drag = (A+B*speed[i]+C*speed[i]*speed[i])/1000+total_weight*9.81*target_slope
        temp = real_power/total_drag
        calculated_speed.append(temp)
        if(abs(temp-speed[i])<0.005+speed[i]*0.0002):
            sp = speed[i]*3.6
            print("speed is", round(sp, 1), "km/h")
            print("total drag force is", round(total_drag, 1), "kn")
if mode == 'power':
    a, = plt.plot(power, calculated_power, label = 'calculated speed')
    b, = plt.plot(power, power, label = 'speed')
    plt.legend(handles=[a, b])
    plt.show()

elif mode == 'speed':
    a, = plt.plot(speed, calculated_speed, label = 'calculated speed')
    b, = plt.plot(speed, speed, label = 'speed')
    plt.legend(handles=[a, b])
    plt.show()