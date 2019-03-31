from Satellite import simulate

Earth_mass = 5.9722 * (10 ** 24)
Earth_radius = 6371000
Earth = [0, 0, Earth_mass]
planets = [Earth]
time = 10000
l = 1000
r = 9000
while r > l + 1:
    m = (l + r) / 2
    initial_velocity = [m, 0]
    Satellite = [0, 6371000]
    tr_x, tr_y = simulate(planets, Satellite, initial_velocity, time)
    min_y = min(tr_y)
    if min_y < -Earth_radius:
        r = m
    else:
        l = m
print(l)