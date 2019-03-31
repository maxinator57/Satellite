from Satellite import simulate
import matplotlib.pyplot as plt
import numpy as np
import math

Earth_mass = 5.9722 * (10 ** 24)
Earth_radius = 6371000
Earth = [0, 0, Earth_mass]
planets = [Earth]
sat = [0, Earth_radius]
v = 12000
initial_velocity = [v, 0]
time = 10000
tr_x, tr_y = simulate(planets, sat, initial_velocity, time)
figure = plt.figure(1, figsize=(8, 8))
plot = figure.add_subplot(111)
for i in range(len(tr_x)):
    tr_x[i] /= 1000
    tr_y[i] /= 1000
plt.axis([-25000, 25000, -25000, 25000])
plt.plot(tr_x, tr_y, 'blue')
plt.scatter(Earth[0] / 1000, 0, color='red')
plt.scatter(sat[0] / 1000, sat[1] / 1000, color='green')
plt.show()