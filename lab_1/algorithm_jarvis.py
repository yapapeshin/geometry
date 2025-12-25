import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0  # коллинеарны
    return 1 if val > 0 else 2  # 1 - по часовой, 2 - против часовой

def convex_hull_jarvis(points):
    n = len(points)
    if n < 3: return points
    
    hull = []
    
    leftmost = min(range(n), key=lambda i: points[i][0])
    
    p = leftmost
    while True:
        hull.append(points[p])
        
        q = (p + 1) % n
        for r in range(n):
            if orientation(points[p], points[r], points[q]) == 2:
                q = r
        
        p = q
        if p == leftmost:
            break
    
    return hull

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title('Convex Hull - Jarvis Algorithm')

all_points = []
hull_line, = ax.plot([], [], 'r-', lw=2)
scatter = ax.scatter([], [], c='blue', alpha=0.6)

def init():
    hull_line.set_data([], [])
    scatter.set_offsets(np.empty((0, 2)))
    return hull_line, scatter

def update(frame):
    new_point = np.random.rand(2) * 9 + 0.5
    all_points.append(new_point)
    
    if len(all_points) > 1:
        hull = convex_hull_jarvis(all_points)
        if hull:

            hull.append(hull[0])
            hull_x, hull_y = zip(*hull)
            hull_line.set_data(hull_x, hull_y)
    

    scatter.set_offsets(all_points)
    
    return hull_line, scatter

ani = FuncAnimation(fig, update, frames=50, 
                    init_func=init, blit=True, interval=500)

plt.show()