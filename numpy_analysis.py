import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',',skip_header = True)


speed= taxi[:, 7]/(taxi[:, 8]/3600)
mean_speed = speed.mean()
print(mean_speed)


feb_rides = taxi[taxi[:, 1] == 2, 1]
print(feb_rides.shape[0])


big_tips= taxi[taxi[:,-3]>50 ,-3]
print(big_tips.shape[0])


dropoff_jfk= taxi[taxi[:, 6]==2 , 6]
print(dropoff_jfk.shape[0])