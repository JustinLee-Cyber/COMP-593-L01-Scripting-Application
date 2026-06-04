
#Student name: Justin Lee
#demo - to learn about dictionary

#Function to print data from the dictionary created from main - in this case player name, number and to split name
def print_name_and_number(data):

	full_name = data['name']
	First_name = full_name.split()
	print(f"My full name is {data['name']} and you can call me {First_name[1]}. \nMy player number is {data["playernumber"]}")

	return

#Function to print data from the dictionary created from main - in this case to print stadium
def print_stadium_list(data):

	#for loop to find what is inside data['stadiums']
	print("Fifa Stadium City Locations: ")
	for _ in data['stadiums']:
		print(_)

	return

#Function to add into the dictionary into data
def add_new_stadium(data, new_stadium):

	#Add whatever string into list of data in dictonary
	data['stadiums'].extend(new_stadium)

	#sort the city in list
	data['stadiums'].sort()

	return 

#function to add match into data dictionary of teams and stages
def add_match(data, teams, stages):

	New_matches = {'team':teams, 'stage':stages}

	data['matches'].append(New_matches)

	return

def main():

	# Main program logic
	#Fifa Dictionary 
	fifa_data = {
		'name':'Lionel Messi', #player name
		'playernumber':'10', #plyer number
		'stadiums':['Toronto','New York','Azteco'], #location in list
		'matches':[ #added dictionary list
			{'team':'Protogal vs Argintena', 'stage':'Finals'}, #information is teams who are facing and stage - semi-finals or finals
			{'team':'Sinegal vs Holand', 'stage':'Semi-Finals'}
		]
	}

	print_name_and_number(fifa_data)
	print_stadium_list(fifa_data)

	add_new_stadium(fifa_data, ('Peterborough', 'Ottawa'))
	print_stadium_list(fifa_data)
	
	add_match(fifa_data, 'Germary vs France', 'quarter-final')
	print(fifa_data['matches'])
	return

if __name__ == '__main__':
	main()