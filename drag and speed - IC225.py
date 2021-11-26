import matplotlib.pyplot as plt
import numpy as np
name = 'Intercity 225'
x = []
v = []
v_show = []
a = []
i_list = []
x.append(0)
v.append(0)
v_show.append(0)
i_list.append(0)
delta_t = 1
power_axle_weight = 20.375
power_car_axle = 4
power_car = 1
power_car_length = 19.4
tender_axle_weight = 0
tender_car_axle = 0
tender_car = 0
tender_car_length = 0
passenger_axle_weight = 9
passenger_car_axle = 4
passenger_car = 10
passenger_car_length = 22
total_length = power_car*power_car_length+tender_car*tender_car_length+passenger_car*passenger_car_length
total_weight_trailer = tender_car*tender_axle_weight*tender_car_axle+passenger_car*passenger_axle_weight*passenger_car_axle
total_weight_power = power_car*power_axle_weight*power_car_axle
total_weight = total_weight_power+total_weight_trailer
width = 3.1
height = 3.7
csa = width*height
peri = (width+height)*2
drag_coefficient = 0.15
gap = 0.6
bogie_drag = 0.4
cars = passenger_car+power_car+tender_car
target_slope = 0.000
target_power = 4800
transmission = 'electric'
if transmission == 'steam':
    real_power = target_power
elif transmission == 'diesel':
    real_power = target_power*0.78
elif transmission == 'electric':
    real_power = target_power*0.86
A = 6.4*total_weight_trailer+8*total_weight_power
B = 0.18*total_weight+passenger_car+0.005*power_car*real_power
C = 0.6125*drag_coefficient*csa+0.00197*peri*total_length+0.0021*peri*gap*(cars-1)+0.2061*bogie_drag*2*cars
initial_tractive_effort = 120*power_car
a.append((initial_tractive_effort-A/1000)/total_weight)
i = 0
while(v[i]<=225/3.6):
    v_temp = v[i]+0.5*a[i]*delta_t
    x.append(x[i]+v_temp*delta_t)
    total_drag = (A+B*v[i]+C*v[i]*v[i])/1000+total_weight*9.81*target_slope
    if target_power/v_temp > initial_tractive_effort:
        tractive_effort = initial_tractive_effort-total_drag
    else:
        tractive_effort = target_power/v_temp-total_drag
    a.append(tractive_effort/total_weight)
    v.append(v_temp+0.5*a[i+1]*delta_t)
    v_show.append(v[i+1]*3.6)
    i+=1
    i_list.append(i)
print(name)
print(i, x[i], v_show[i], a[i])
#a, = plt.plot(i_list, v, label = 'speed')
#b, = plt.plot(i_list, x, label = 'distance')
#plt.legend(handles=[a, b])
#plt.show()

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('speed', color=color)
ax1.plot(i_list, v_show, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('distance', color=color)  # we already handled the x-label with ax1
ax2.plot(i_list, x, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()

#plt.plot(x, v_show)
#plt.show()
