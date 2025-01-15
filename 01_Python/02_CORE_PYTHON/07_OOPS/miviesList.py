class Movies:
    """ This class is created by sayed for demo purpose """

    def __init__(self, title, actor, actress):
        self.title = title
        self.actor = actor 
        self.actress = actress
        

    def info(self):
        print("Name of the movie is: ", self.title) 
        print("Name of the actor is: ", self.actor)
        print("Name of the actress : ", self.actress) 
        

movies_List = []
while True:

    title = input("Please Enter Name of the Title: ")
    actor = input("Please Enter Name of the Actor: ")
    actress = input("Please ENter Name of the Actress: ")

    # Creating an object of the Movie class 
    m = Movies(title, actor, actress)
    movies_List.append(m) 
    flag = input("Do You want to enter more Movie Details:[Yes/No]: ")
    if flag.lower() == "no":
        break # Exit form the while loop 

print("#" * 40)
print(movies_List)
print()
for movies in movies_List:
    movies.info()
    print()  
