cars = 100 #一共有100辆车
space_in_a_car = 4 #每一辆车都有4个空位
drivers = 30  #驾驶员有30个
passengers = 90  #有90位乘客
cars_not_driven = cars - drivers  #没有驾驶员的车数量
cars_driven = drivers  #拥有驾驶员的车数量
carpool_capacity = cars_driven * space_in_a_car #能驾驶的车一共有的位置
average_passengers_per_car = passengers / cars_driven  #可以驾驶的每辆车,所要载乘客数量
print('There ar', cars, 'cars available.')
print('There are only',drivers, 'drivers available')
print('There will be', cars_not_driven, 'empty cars today.')
print('We car transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We to put about', average_passengers_per_car, 'in each car.')