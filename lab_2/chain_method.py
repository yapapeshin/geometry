import matplotlib.pyplot as plt
import numpy as np
import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0  
    return 1 if val > 0 else 2  

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def gift_wrapping(points):
    if len(points) < 3:
        return points
    
    hull = []
    leftmost = min(points, key=lambda p: p[0])
    current = leftmost
    
    while True:
        hull.append(current)
        endpoint = points[0]
        
        for point in points:
            if endpoint == current or orientation(current, endpoint, point) == 2:
                endpoint = point
        
        current = endpoint
        if current == leftmost:
            break
    
    return hull

def chain_method_convex_hull(points):
    """
    Метод цепей (алгоритм Чена)
    Комбинация быстрой сортировки и заворачивания подарка
    """
    if len(points) <= 6:
        return gift_wrapping(points)
    
    m = max(2, len(points) // 3)  
    subsets = np.array_split(points, m)

    hulls = []
    for subset in subsets:
        if len(subset) >= 3:
            hull = gift_wrapping(subset.tolist())
            hulls.append(hull)

    all_hull_points = []
    for hull in hulls:
        all_hull_points.extend(hull)
    
    return gift_wrapping(all_hull_points)


def visualize_chains(points, hull):
    plt.figure(figsize=(10, 6))
    
    x, y = zip(*points) if points else ([], [])
    plt.scatter(x, y, c='blue', alpha=0.6, label='Точки')
    
    if hull:
        hull.append(hull[0])
        hx, hy = zip(*hull)
        plt.plot(hx, hy, 'r-', linewidth=2, label='Выпуклая оболочка')
        plt.scatter(hx, hy, c='red', s=100, marker='o', label='Вершины оболочки')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Метод цепей для построения выпуклой оболочки')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.axis('equal')
    plt.show()


if __name__ == "__main__":

    np.random.seed(42)
    num_points = 50
    points = np.random.rand(num_points, 2) * 10

    hull = chain_method_convex_hull(points.tolist())
    
    print(f"Всего точек: {len(points)}")
    print(f"Вершин в оболочке: {len(hull)}")
    print(f"Вершины оболочки: {hull}")
    
    visualize_chains(points.tolist(), hull)