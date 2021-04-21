graph = {}
graph["CAB"] = ["CAT", "CAR"]
graph["CAT"] = ["MAT", "BAT"]
graph["CAR"] = ["BAR"]
graph["MAT"] = ["BAT"]
graph["BAR"] = ["BAT"]
graph["BAT"] = []

from collections import deque

def person_is_seller(name):
	return name[-1] == "m"

def is_BAT(name):
	return name == "BAT"

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print person + " is a mango seller!"
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False


search("BAT")