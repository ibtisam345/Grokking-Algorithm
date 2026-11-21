from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'  # his name ends with the letter "m"

graph = {}    # <---- This is an empty dictionary
graph["you"] = ["Alice", "Bob", "Claire"]   # <--- Every vertices is connected by its neighbours
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Thom"] = []
graph["Jonny"] = []

def breadth_first_search(name):
    search_queue = deque()  # Creates a new queue
    search_queue += [name]  # Adds all of your out-neighbors to the search list

    searched = set()

    while search_queue:     # While the queue isn't empty...
        person = search_queue.popleft() # ...grabs the first person out of the queue.

        if person in searched:
            continue
        if person_is_seller(person):    # Checks whether the person is a mango seller
            print(person + " is a mango seller!")
            return True
        
        # No, they aren't. Add all of this person's friends to the queue
        search_queue += graph[person]   

        searched.add(person)
    return False    

breadth_first_search("you")