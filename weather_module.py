import matplotlib.pyplot as mpl
import numpy as np
import sys

bigmatrix = np.loadtxt(
    "data_temperature.txt",
    delimiter=",",
    usecols=[2, 3, 4, 5, 6, 7],
    skiprows=1,
)
NYmatrix = np.loadtxt("data_temperature.txt",
                      delimiter=",",
                      usecols=[2, 3, 4, 5, 6, 7],
                      skiprows=1,
                      max_rows=31)

LAmatrix = np.loadtxt("data_temperature.txt",
                      delimiter=",",
                      usecols=[2, 3, 4, 5, 6, 7],
                      skiprows=32,
                      max_rows=31)

LDNmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=63,
                       max_rows=31)

TKYmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=94,
                       max_rows=31)

BJmatrix = np.loadtxt("data_temperature.txt",
                      delimiter=",",
                      usecols=[2, 3, 4, 5, 6, 7],
                      skiprows=125,
                      max_rows=31)

SYDmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=156,
                       max_rows=31)

PRSmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=187,
                       max_rows=31)

BLNmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=218,
                       max_rows=31)

CROmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=249,
                       max_rows=31)

NDLmatrix = np.loadtxt("data_temperature.txt",
                       delimiter=",",
                       usecols=[2, 3, 4, 5, 6, 7],
                       skiprows=280,
                       max_rows=31)

city_names = []
with open("data_temperature.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        data = line.split(",")
        city = data[1]
        if city not in city_names:
            city_names.append(city)

dates = np.loadtxt("data_temperature.txt", delimiter=",", dtype=str, usecols=[1], skiprows=1, max_rows=31)
 

city_matrices = [
    NYmatrix, LAmatrix, LDNmatrix, TKYmatrix, BJmatrix, SYDmatrix, PRSmatrix,
    BLNmatrix, CROmatrix, NDLmatrix
]






def average_temperature(matrix):
  sum_temp = 0
  for line in matrix:
    sum_temp += (int(line[0]) + int(line[1]) / 2
                 )  # average temperature of the day
  return sum_temp / len(matrix)  # total average temperature


def total_precipitation(matrix):
  total = 0
  for line in matrix:
    total += int(line[2])
  return total


def max_min_wind_speed(matrix):
  max_speed = float('-inf')
  min_speed = float('inf')
  for line in matrix:
    if int(line[3]) > max_speed:
      max_speed = int(line[3])
    elif int(line[3]) < min_speed:
      min_speed = int(line[3])
  return max_speed, min_speed


def city_wise_analysis():
  for i in range(len(city_names)):
    print(
        f"The average temperature in {city_names[i]} is {average_temperature(city_matrices[i])}"
    )
    print(
        f"The total precipitation in {city_names[i]} is {total_precipitation(city_matrices[i])}"
    )
    print(
        f"The max wind speed in {city_names[i]} is {max_min_wind_speed(city_matrices[i])[0]} and minimum wind speed is {max_min_wind_speed(city_matrices[i])[1]}"
    )


def temp_over_time(matrix):
  temp_over_time = []
  for line in matrix:
    average = (int(line[0]) + int(line[1])) / 2
    temp_over_time.append(average)
  #temp_over_time.append(0)

  return temp_over_time
#print(temp_over_time(LDNmatrix),len(temp_over_time(LDNmatrix)))

def visualise_temp(city_matrices, cities):  #LINE CHART
  for i in range(len(city_matrices)):
    mpl.plot(list(range(1, 31)),
             temp_over_time(city_matrices[i]),
             label=cities[i])
  mpl.xlabel("Days")
  mpl.ylabel('Temperature/Cº')
  mpl.legend(loc=(0, 1), mode="shrink", ncol=len(cities))
  mpl.show()


def compare_avg_temp(city_matrices, cities):  #BAR CHART
  fig, ax = mpl.subplots()

  avg_temps = []
  for city in city_matrices:
    avg_temps.append(average_temperature(city))
  ax.bar(cities, avg_temps, label=cities)
  ax.set_xlabel("Cities")
  ax.set_ylabel("Average Temperature/Cº")
  mpl.show()


#visualise_temp(city_matrices)

#Exercice 4

# 4.1
def categorized_day_city(city_matrix):
  average_temp = average_temperature(city_matrix)
  categorized_day_city_matrix = []
  for i in range(np.size(city_matrix, 0)):
    daily_average_temp = (city_matrix[i][0] + city_matrix[i][1]) / 2
    if average_temp * 0.9 < daily_average_temp < average_temp * 1.1:
      categorized_day_city_matrix.append("moderate")
    elif daily_average_temp < average_temp:
      categorized_day_city_matrix.append("cold")
    else:
      categorized_day_city_matrix.append("hot")
  return categorized_day_city_matrix

def categorize_all_cities():
  i = 0
  for city in city_matrices:
    print(city_names[i], categorized_day_city(city))
    i += 1
#print(categorize_all_cities())


#4.2
def find_hottest_day_city(city_matrix):
  max_temp, index = city_matrix[0][0], 0
  for i in range(np.size(city_matrix, 0)):
    if city_matrix[i][0] > max_temp:
      max_temp, index = city_matrix[i][0], i
  min_temp = city_matrix[index][1]
  return max_temp, min_temp, index

def find_coldest_day_city(city_matrix):
  min_temp, index = city_matrix[0][0], 0
  for i in range(np.size(city_matrix, 0)):
    if city_matrix[i][1] < min_temp:
      min_temp, index = city_matrix[i][1], i
  max_temp = city_matrix[index][0]
  return max_temp, min_temp, index

def find_hottest_and_coolest_day_city(city_matrix):
  max_temp1, min_temp1, index_max = find_hottest_day_city(city_matrix)
  max_temp2, min_temp2, index_min = find_coldest_day_city(city_matrix)
  date_max = dates[index_max]
  date_min = dates[index_min]
  return (max_temp1, min_temp1, date_max), (max_temp2, min_temp2, date_min)
#print(find_hotest_and_coolest_day_city(NYmatrix))


#4.3
def find_hottest_and_coolest_day_all_cities():
  hottest_and_coolest_days = []
  i = 0
  for city in city_matrices:
    hottest_and_coolest_days += [
        city_names[i], find_hottest_and_coolest_day_city(city)
    ]  #could add some space
    i += 1
  return hottest_and_coolest_days
#print(find_hotest_and_coolest_day_all_cities())

# question 4.4 
def correlation_matrix(city_matrix):
  corr_matrix = np.corrcoef(city_matrix, rowvar=False)
  first_two_columns = corr_matrix[:, :2]
  return first_two_columns  # plus de description serait utile(pandas)
#print(correlation_matrix(NYmatrix))

#4.5
def find_hottest_day_all_cities(matrix):
  max_temp, min_temp,index = find_hottest_day_city(matrix)
  date = dates[index%31]
  city_index = (index - (index%31))//31
  return city_names[city_index],date,max_temp, min_temp, 
#print(find_hottest_day_all_cities(bigmatrix))

#4.6
def find_coldest_day_all_citis(matrix):
  max_temp, min_temp,index = find_coldest_day_city(matrix)
  date = dates[index%31]
  city_index = (index - (index%31))//31
  return city_names[city_index],date,max_temp, min_temp
#print(find_coldest_day_all_citis(bigmatrix))


#question 5
paris_matrix = np.loadtxt("Paris_data_climate.txt",
                          delimiter=',',
                          skiprows=1,
                          usecols=[2, 3, 4, 5, 6, 7, 8, 9],
                          dtype='float')

def get_data(matrix):
  temp = temp_over_time(matrix)
  precipitation = []
  C02 = []
  SeaLevelRise = []
  for line in matrix:
    precipitation.append(int(line[2]))
    C02.append(int(line[-2]))
    SeaLevelRise.append(int(line[-1]))
  return temp, precipitation, C02, SeaLevelRise
temp, precipitation, C02, SeaLevelRise = get_data(paris_matrix)

def temp_C02(C02,temp):
    mpl.plot(C02,temp)
    mpl.xlabel('C02/ppm')
    mpl.ylabel('Temperature/Cº')
    mpl.show()
def temp_sea(sea,temp):
    mpl.plot(sea,temp)
    mpl.xlabel('Rise in Sea Level/mm')
    mpl.ylabel('Temperature/Cº')
    mpl.show()
def precipitation_sea(sea,rain):
    mpl.plot(sea,rain)
    mpl.ylabel("Precipitation/mm")
    mpl.xlabel("Rise in Sea Level/mm")
    mpl.show()
def C02_precipitation(rain,C02):
    mpl.plot(C02,rain)
    mpl.xlabel('C02/ppm')
    mpl.ylabel("Precipitation/mm")
    mpl.show()

#Exercice 6

def plot_city_data(city):
  if city not in city_names:
    return "The city is not included in the data"
  else:  
    city_index = city_names.index(city)
    city_matrix = city_matrices[city_index]
    print(f'average temperature of {city} is {average_temperature(city_matrix)}')
    print(f'total precipitation of {city} is {total_precipitation(city_matrix)}')
    print(f'"The max wind speed in {city} is {max_min_wind_speed(city_matrix)[0]} and minimum wind speed is {max_min_wind_speed(city_matrix)[1]}")
      
    
    
  

#plot_city_data(sys.arv[1])
