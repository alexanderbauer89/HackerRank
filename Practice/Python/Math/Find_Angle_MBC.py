import math 
AB, BC = int(input()), int(input())
print(str(int(round(math.degrees(math.atan2(AB,BC)))))+chr(176))
