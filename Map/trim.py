#Python CSV Trimming script
import csv

file = open('locations.csv', 'w')


with open("yellow_tripdata_2016-02.csv") as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		file.write(row['pickup_longitude'] + ',' + row['pickup_latitude'] + ',' + row['dropoff_longitude'] + ',' + row['dropoff_latitude'] + '\n')



file.close()





