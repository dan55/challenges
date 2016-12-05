'''
Thoughts: 

Don't be afraid to have a number of properties. We're saving space by

tracking these rather than stroing all temperatures. 

Initializing numbers to None is interesting. Don't forget you have to check

for this when doing the comparisons, though.


Source:

https://www.interviewcake.com/question/python/temperature-tracker
'''

class TempTracker():
    def __init__(self):
        self.min = None
        self.max = None

        self.counter = 0
        self.total = 0
        self.mean = 0.0

        self.mode = None
        self.temps = {}

    def insert(self, temp): 
        if self.min is None or temp < self.min:
            self.min = temp

        if self.max is None or temp > self.max:
            self.max = temp

        self.counter += 1
        self.total += temp
        self.mean = self.total / self.counter

        try:
            self.temps[temp] += 1

            if self.temps is None or self.temps[temp] > self.mode:
                self.mode = self.temps[temp]
        except KeyError:
            self.temps[temp] = 1

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_mean(self):
        return self.mean

    def get_mode(self):
       return self.mode

tracker = TempTracker() 
temps = [77, 34, 34, 101, 98.6]

for temp in temps:
    tracker.insert(temp)

print tracker.get_min()
print tracker.get_max()
print tracker.get_mean()
print tracker.get_mode()