class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is {}. My favorite color is {}. I weigh around {} pounds.".format(self.name, self.color, self.weight))

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

r1 = Robot("Tom", "Red", 30)


r1.introduce_self()

r2 = Robot("Ryo", "Yellow", 110)

r2.introduce_self()

p1 = Person("Alice", "Aggressive", False)
p1.robotOwned = r2


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def add_time(t1, t2):
    hr = t1.hour + t2.hour
    min = t1.minute + t2.minute
    sec = t1.second + t2.second

    if min >= 60:
        min -= 60
        hr += 1
    if sec >= 60:
        sec -= 60
        min += 1

    sum = Time(hr, min, sec)
    return sum

start = Time(9, 45, 0)
duration = Time(1, 35, 0)
print(add_time(start, duration).hour, add_time(start, duration).minute, add_time(start, duration).second)
