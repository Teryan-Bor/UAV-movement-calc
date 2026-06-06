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
    self.battery_drop = 5

  def move(self, wind):
    dx = self.x_dest - self.x
    dy = self.y_dest - self.y
    distance = np.sqrt(dx**2 + dy**2)

    if distance > self.v_step:
      drone_step_x = self.v_step * (dx / distance)
      drone_step_y = self.v_step * (dy / distance)

      self.x += drone_step_x + wind[0]
      self.y += drone_step_y + wind[1]

      wind_force = np.sqrt(wind[0]**2 + wind[1]**2)
      actual_drop = self.battery_drop + (wind_force * 0.2)
      self.full_battery -= actual_drop
    else:
      self.x = self.x_dest
      self.y = self.y_dest
      print("Drone achieved the aim!")

class Simulation:
  def __init__(self):
    self.drone = Drone()

    self.wind = [2.5, 0.5]

    self.x_history = []
    self.y_history = []
    self.battery_history = []
  
  def run(self):
    while(self.drone.x != self.drone.x_dest or self.drone.y != self.drone.y_dest) and self.drone.full_battery >= 0:
      self.x_history.append(self.drone.x)
      self.y_history.append(self.drone.y)
      self.battery_history.append(self.drone.full_battery)

      self.drone.move(self.wind)

if __name__ == "__main__":
    # 1. Создаем объект симуляции
    sim = Simulation()
    
    # 2. Запускаем цикл расчетов
    sim.run()

    plt.figure(figsize=(10, 5)) 

    plt.subplot(1, 2, 1)
    plt.plot(sim.x_history, sim.y_history,  label="Drone traectory", color="green")
    plt.scatter([0], [0], label="Start point", color="blue")
    plt.scatter([100], [100], label="End point", color="red")
    plt.title("UAV fly map")
    plt.xlabel("Coordinate X")
    plt.ylabel("Coordinate Y")
    plt.grid(True)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(sim.battery_history, color="orange", label="battery level %")
    plt.scatter([20], color="yellow", label="minimum percentage of drone battery")
    plt.title("Battery drop dynamic")
    plt.xlabel("Time steps(sec)")
    plt.ylabel("Battery %")
    plt.grid(True)
    plt.legend()

    plt.show()