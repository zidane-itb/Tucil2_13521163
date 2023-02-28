import random
import matplotlib.pyplot as plt

from point import Point


def generate_points(dim: int, length: int) -> list[Point]:
    points: list[Point] = []

    for i in range(length):
        # generate bounded float point number
        points.append(Point(dim, [round(random.uniform(-2000.0, 2000.0), 1) for _ in range(dim)]))

    return points


def visualise(points: list[Point], closest_pair: tuple[Point, Point]):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for point in points:
        if not (point.equals(closest_pair[0]) or point.equals(closest_pair[1])):
            ax.scatter(point.points[0], point.points[1], point.points[2], c=['#d62728'])  # red
        else:
            ax.scatter(point.points[0], point.points[1], point.points[2], c=['#9467bd'])  # purple

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def sort(points: list[Point]) -> list[Point]:
    size = len(points)
    if size == 1:
        return points

    mid = size//2
    left_arr = sort(points[:mid])
    right_arr = sort(points[mid:])

    l_idx = r_idx = m_idx = 0

    while l_idx < len(left_arr) and r_idx < len(right_arr):
        if left_arr[l_idx].points[0] > right_arr[r_idx].points[0]:
            points[m_idx] = right_arr[r_idx]
            r_idx += 1
        else:
            points[m_idx] = left_arr[l_idx]
            l_idx += 1
        m_idx += 1

    while l_idx < len(left_arr):
        points[m_idx] = left_arr[l_idx]
        l_idx += 1
        m_idx += 1

    while r_idx < len(right_arr):
        points[m_idx] = right_arr[r_idx]
        r_idx += 1
        m_idx += 1

    return points
