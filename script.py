destinations = ["Paris, France", 'Shanghai, China', "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for destination in destinations]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination= []
    attactions_for_destination.append(attractions[destination_index])

  
#print(test_destination_index)

print(attractions)
