# Python-Project



import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',',skip_header = True)



# Mean speed of all the rides

speed= taxi[:, 7]/(taxi[:, 8]/3600)
mean_speed = speed.mean()
print(mean_speed)



# Number of rides taken in february

feb_rides = taxi[taxi[:, 1] == 2, 1]
print(feb_rides.shape[0])



# Number of rides wkere tip more than 50$

big_tips= taxi[taxi[:,-3]>50 ,-3]
print(big_tips.shape[0])



# Number of rides wkere drop was JFK airport

dropoff_jfk= taxi[taxi[:, 6]==2 , 6]
print(dropoff_jfk.shape[0])
