#Student Name: Justin Lee
#Student Number: 10152040
#Lab 3

# Create functions

#Step 3:
#function to print name - grab information from created dictinary to print, split and show ID
def printName(data):
	
      Fullname = data['name']
      first_name = Fullname.split()

      print(f'My name is {data['name']}, but you can call me Sir {first_name[0]}.\nMy student ID is {data['student_ID']}')

      return

#Step 4:
#function to print pizza toppings that Justin like!
def printtoppings(data):
	
      print("My favourite pizza toppings are:")

      for _ in data['pizza_toppings']:
          print(_)

      return

#Step 5:
def addtoppings(data,toppings):
      
      data['pizza_toppings'].extend(toppings)

      data['pizza_toppings'].sort()

      return

def main():
      #Main function

      #Step 2:
      information = {
            'name':'Justin Lee',
            'student_ID': '10152040',
            'pizza_toppings':['Cheese', 'Bacon', 'Pepperoni'],
            'movies':[
                  {'title':'fast & furious', 'genre':'action'},
                  {'title':'the batman', 'genre':'crime/mystery'}
            ]
      }

      printName(information)
      printtoppings(information)

      addtoppings(information, ('Pineapple', 'sausesage', 'extra_cheese'))
      printtoppings(information)

      return
if __name__ == '__main__':
	main()