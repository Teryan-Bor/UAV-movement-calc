import matplotlib.pyplot as plt
import numpy as np

class Drone:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.x_dest = 100
    self.y_dest = 100
    self.v = 200
    self.v_step = 5
    self.full_battery = 100
    self.battery_drop = 1

  def move(self):
    dx = self.x_dest - self.x
    dy = self.y_dest - self.y
    distance = np.sqrt(dx**2 + dy**2)

    if distance > self.v_step:
      self.x += self.v_step * (dx / distance)
      self.y += self.v_step * (dy / distance)
      self.full_battery -= self.battery_drop
    else:
      self.x = self.x_dest
      self.y = self.y_dest
      print("Drone achieved the aim!")

class Simulation:
  def __init__(self):
    self.drone = Drone()

    self.x_history = []
    self.y_history = []
    self.battery_history = []
  
  def run(self):
    while(self.drone.x != self.drone.x_dest | self.drone.y != self.drone.y_dest):
      self.x_history.append(self.drone.x)
      self.y_history.append(self.drone.y)
      self.battery_history.append(self.drone.full_battery)

      self.drone.move()

   
