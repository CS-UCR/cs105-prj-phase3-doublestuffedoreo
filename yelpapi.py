import requests
import pandas as pd
import csv

# define business id
business_id = '4AErMBEoNzbk7Q8g45kKaQ'


# define api key, define endpoint, define header
API_KEY = "muZLsvNtMFfLfe8-iAbB-v7WmtU78ICYwRVOhftWshzDBb5yyNFMH7gRmD6qIubBOyId_kI5yUYQHH5DpcyhBkO_BOstBWRV9VgT-ZXyO1PwebWDNW0EljvJokjHXXYx"
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY} #%s puts the % value (api_key) into it

#define the parameters of query
#limit is number of restaurants, radius is meters in area
#insert 'offset': 50 to get next 50, from range 50-100
P1 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 50,
				'location':'Riverside, CA'}
P2 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 100,
				'location':'Riverside, CA'}
P3 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 150,
				'location':'Riverside, CA'}
P4 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 200,
				'location':'Riverside, CA'}
P5 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 250,
				'location':'Riverside, CA'}
P6 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 300,
				'location':'Riverside, CA'}
P7 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 350,
				'location':'Riverside, CA'}
P8 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 400,
				'location':'Riverside, CA'}
P9 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 450,
				'location':'Riverside, CA'}
P10 = {'term':'restaurants',
				'limit': 50,
				'radius': 10000,
				'offset': 500,
				'location':'Riverside, CA'}

restaurantParams = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
csvFile = csv.writer(open('restaurants.csv', 'a'), lineterminator='\n')
csvFile.writerow(['name', 'price', 'rating', 'review_count', 'address', 'city', 'state', 'zip_code'])
for i in restaurantParams:
	response = requests.get(url = ENDPOINT, params = i, headers = HEADERS)
	business_data = response.json()
	for biz in business_data['businesses']:
		n = biz.get('price', None)
		csvFile.writerow([biz['name'], n, biz['rating'], biz['review_count'], biz['location']['address1'], biz['location']['city'], biz['location']['state'], biz['location']['zip_code']])

# print(business_data)
	
# R1 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 50,
# 				'location':'Riverside, CA'}
# R2 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 100,
# 				'location':'Riverside, CA'}
# R3 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 150,
# 				'location':'Riverside, CA'}
# R4 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 200,
# 				'location':'Riverside, CA'}
# R5 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 250,
# 				'location':'Riverside, CA'}
# R6 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 300,
# 				'location':'Riverside, CA'}
# R7 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 350,
# 				'location':'Riverside, CA'}
# R8 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 400,
# 				'location':'Riverside, CA'}
# R9 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 450,
# 				'location':'Riverside, CA'}
# R10 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 500,
# 				'location':'Riverside, CA'}
# R11 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 550,
# 				'location':'Riverside, CA'}
# R12 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 600,
# 				'location':'Riverside, CA'}
# R13 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 650,
# 				'location':'Riverside, CA'}
# R14 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 700,
# 				'location':'Riverside, CA'}
# R15 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 750,
# 				'location':'Riverside, CA'}
# R16 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 800,
# 				'location':'Riverside, CA'}
# R17 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 850,
# 				'location':'Riverside, CA'}
# R18 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 900,
# 				'location':'Riverside, CA'}
# R19 = {'term':'businesses',
# 				'limit': 50,
# 				'radius': 10000,
# 				'offset': 950,
# 				'location':'Riverside, CA'}
# # R20 = {'term':'businesses',
# # 				'limit': 50,
# # 				'radius': 10000,
# # 				'offset': 1000,
# # 				'location':'Riverside, CA'}
# busParams = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19]
# for j in busParams:
# 	response = requests.get(url = ENDPOINT, params = j, headers = HEADERS)
# 	business_data = response.json()
# 	csvFile2 = csv.writer(open('localBus.csv', 'a'), lineterminator='\n')
# 	for biz in business_data['businesses']:
# 		csvFile.writerow([biz['name'], biz['categories'], biz['rating'], biz['review_count'], biz['location']['address1'], biz['location']['city'], biz['location']['state'], biz['location']['zip_code']])


# PARAMETERS = {'term': 'good food',
# 				'location': 'San Diego',
# 				'latitude': 32.23423,
# 				'longitude': -113.34589,
# 				'radius': 10000,
# 				'categories': 'bars,french',
# 				'locale':'en_US',
# 				'limit':50,
# 				'offset':150,
# 				'sort_by':'best_match',
# 				'price':'1',
# 				'open_now:':True,
# 				'open_at':1523498,
# 				'attributes':'hot_and_new'
# 				}
