from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'  # his name ends with the letter "m"

graph = {}
graph["you"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Thom", "Jonny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Thom"] = []
graph["Jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += [name]

    searched = set()

    while search_queue:
        person = search_queue.popleft()

        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True

        search_queue += graph[person]

        searched.add(person)
    return False

search("you")