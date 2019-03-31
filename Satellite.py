import math

def simulate(planets, startpoint, v, time):
    G = 6.674083131 * (10 ** (-11))
    C = 0.0001
    time_interval = 1
    curvel = v.copy()
    curpoint = startpoint.copy()
    tr_x = [startpoint[0]]
    tr_y = [startpoint[1]]
    steps = time // time_interval
    for step in range(steps):
        curpoint[0] += curvel[0] * time_interval
        curpoint[1] += curvel[1] * time_interval
        tr_x.append(curpoint[0])
        tr_y.append(curpoint[1])
        for i in range(len(planets)):
            r1 = planets[i][0] - curpoint[0]
            r2 = planets[i][1] - curpoint[1]
            rr = r1 * r1 + r2 * r2
            r = math.sqrt(rr)
            if r < C:
                return tr_x, tr_y
            curvel[0] += G * planets[i][2] / rr * r1 / r
            curvel[1] += G * planets[i][2] / rr * r2 / r
    return tr_x, tr_y