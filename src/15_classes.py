# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
# self === coord here
class LatLon:
    obj_type = "LatLon" # static/class variable, shared among all instances of this class
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# to change static/class variable:
# LatLon.obj_type = "new type"

c1 = LatLon(55, 55)
print("C1 lat:", c1.lat)
print("C1 lon:", c1.lon)
print("C1 static variable:", c1.obj_type)

c2 = LatLon(66, 66)
print("C2 lat:", c2.lat)
print("C2 lon:", c2.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    
    # increasing readability
    def __str__(self):
        # return 'Waypoint( name = '+self.name+', lat = '+str(self.lat)+', lon = '+str(self.lon)+' )'
        return f'Waypoint: name = "{self.name}", lat = {self.lat}, lon = {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    # increasing readability
    def __str__(self):
        # return 'Geocache( name = '+self.name+', difficulty = '+str(self.difficulty)+', size = '+str(self.size)+', lat = '+str(self.lat)+', lon = '+str(self.lon)+' )'
        return f'Geocache: name = "{self.name}", {self.difficulty}, size = {self.size}, lat = {self.lat}, lon = {self.lon}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
w1 = Waypoint("Catacombs", 41.70505, -121.51521)
print(f'"{w1.name}", {w1.lat}, {w1.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(w1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
g1 = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(f'"{g1.name}", diff {g1.difficulty}, size {g1.size}, {g1.lat}, {g1.lon}')

# Print it--also make this print more nicely
print(g1)
