#Student Name: Justin Lee
#Student Number: 10152040
#Lab 3
#Step 1 - start writing the scripts :D

# Create functions
# Step 3:
# Function to print name - grab information from created dictinary to print, split and show ID
def printName(data):
	
      Fullname = data['name']
      first_name = Fullname.split()

      print(f'My name is {data['name']}, but you can call me Sir {first_name[0]}.\nMy student ID is {data['student_ID']}')

      return

# Step 4:
# Function to print pizza toppings that Justin like!
def printtoppings(data):
	
      print("My favourite pizza toppings are:")

      for _ in data['pizza_toppings']:
          print(f'- {_}')

      return

# Step 5:
# Function: Added extra likeable toppings using a tuple into the data key 'pizza_toppings' list
def addtoppings(data,toppings):
      
      data['pizza_toppings'].extend(toppings)

      data['pizza_toppings'].sort()

      data['pizza_toppings'] = list(map(str.lower, data['pizza_toppings']))

      return

# Step 6: 
# Function: Added movies from title and genre string - from main
def addmovies(data, title, genre):

      Add_NewMovie = {'title':title, 'genre':genre}

      data['movies'].append(Add_NewMovie)

      return

# Step 7:
# Function: Printed the data key movies but the genre only
def printgenre(data):
      
      print("I like to watch", end=" ")

      for i in range(len(data['movies'])):
            if i == len(data['movies']) - 1:
                  print(f"and {data['movies'][i]['genre']} movies.")
            else:  
                  print(f"{data['movies'][i]['genre']}", end=", ")
      return

# Step 8: 
# Function: printed movie titles from the data key title
def printtitle(data):

      print ("Some of my favourite movies are", end=" ")

      for i in range(len(data['movies'])):
            if i == len(data['movies']) - 1:
                  print(f'and {data['movies'][i]['title'].title()}!')
            else:
                  print(f'{data['movies'][i]['title'].title()}', end=', ')

      return

def main():
      #Main function

      #Step 2:
      information = {
            'name':'Justin Lee',
            'student_ID': '10152040',
            'pizza_toppings':['CHEESE', 'BACON', 'PEPPERONI'],
            'movies':[
                  {'title':'fast & furious', 'genre':'action'},
                  {'title':'thor', 'genre':'fantasy'}
            ]
      }

      #Calling the functions in order to create the results using the functions
      print("Lab 3 print results:")

      printName(information) #Step 3 print
      print('------------------') 

      printtoppings(information)#Step 4 print
      print('------------------') 

      addtoppings(information, ('Pineapple', 'sausesage', 'extra_cheese')) #Step 5 Add new toppings
      printtoppings(information)#Step 4 with adjustments from Step 5
      print('------------------')

      addmovies(information, 'spider-man 2', 'romance')
      printgenre(information) #Step 7 print
      print('------------------') 

      printtitle(information)#Step 8 print
      print('------------------') 

      return

if __name__ == '__main__':
	main()