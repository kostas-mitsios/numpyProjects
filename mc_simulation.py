import numpy as np
import matplotlib.pyplot as plt

#defaults
data_entry_time_min = 10
data_entry_time_max = 35
validation_time_min = 10
validation_time_max = 25
#work_hours_per_day = 8
#work_days_per_week = 5
total_time_limit = 50
simulations = 1000000

#data simulated entries: data entry & data validation
data_entry_times = np.random.uniform(data_entry_time_min, data_entry_time_max, simulations)
validation_times = np.random.uniform(validation_time_min, validation_time_max, simulations)

#check for <50 minutes completion
successful_cases = np.sum(data_entry_times + validation_times <= total_time_limit)

probability_success = successful_cases / simulations
time_limits = np.arange(30, 61) #np.arange(30, 61,2)
#step interval: 1
success_rates = [np.sum(data_entry_times + validation_times <= limit) / simulations for limit in time_limits]

#plot
plt.figure(figsize=(10, 6))
plt.plot(time_limits, success_rates, marker='o', color='b')
plt.title('Probability of Completing Data Entry and Validation within Time Limit')
plt.xlabel('Time Limit (minutes)')
plt.ylabel('Success Rate (%)')
plt.grid(True)

#y axis ticks
plt.yticks(np.arange(0, 1.1, 0.1))

#success within 40 minutes
success_within_range = np.sum(data_entry_times + validation_times <= 40) / simulations
success_within_range_percentage = success_within_range * 100
print(success_within_range_percentage)

#plt.show()