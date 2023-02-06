def main():
    #TODO: step 2 - Create a complex data structure
    about_me={
    'full_name' : 'Mahaldeep Singh',
    'student_id' :'10284922',
    'pizza_toppings' :[
        'PINEAPPLE',
        'SAUSAGE',
        'PEPPERONI'],
        'movies':[
            { 
            'title': 'Dune',
            'genre': 'sci-fic'},
            {
            'title': 'The Hangover',
            'genre': 'comedy'}
            ]
            }
   #TODO step 3 - Add another movie to the data structure
    new_movie={
        'title': 'The Lord of the Rings',
        'genre': 'fantasy'}

    

   
    #Add another movie
    about_me['movies'].append({'title' : 'The Lord of the Rings'})

    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me,('bacon','hot papper') )
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles("dangal, krish3")
    return

    #TODO Step 4 - Function that prints student name and ID

def print_student_name_and_id(about_me):

 print(f"My name is {about_me['full_name'].title()}, you can call me Mr.{about_me['full_name'].split()[0]}")
 print (f"My student ID is {about_me['student_id']}")

     

#TODO: step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
      about_me['pizza_toppings'].append(toppings)
      #about_me['pizza_toppings'].sort(about_me)

      for i, p in enumerate(about_me['pizza_toppings']) :
       about_me['pizza_toppings'] [i] = p.lower()

#TODO: step-6 Function that prints bullet list of pizza toppings

def print_pizza_toppings(about_me):
        #about_me['pizza toppings'].extend()
    
        print(f'My favourite pizza toppings are : ')

        for p in  about_me['pizza_toppings']:
          print(f'- {p.capitalize()}')

        return
# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return

if __name__== '__main__':
         main() 