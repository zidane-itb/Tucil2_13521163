from point import Point
import util


def __get_brute_force__(points: list[Point]) -> tuple[float, tuple[Point, Point]]:
    closest: tuple[float, tuple[Point, Point]] = None
    size = len(points)

    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            dist = points[i].get_distance_to(points[j])
            if closest is None or dist < closest[0]:
                closest = dist, (points[i], points[j])

    return closest


def get_closest_points(points: list[Point], intact_p: list[Point]) -> tuple[float, tuple[Point, Point]]:
    size = len(points)

    if size <= 3:
        return __get_brute_force__(points)

    mid = int(size / 2)
    left_arr, right_arr = points[:mid], points[mid:]
    left_closest = get_closest_points(left_arr, intact_p)
    right_closest = get_closest_points(right_arr, intact_p)

    closest = left_closest if left_closest[0] < right_closest[0] else right_closest

    mid_point = points[mid]
    left_arr = list(filter(lambda point: abs(point.points[0] - mid_point.points[0]) <= closest[0], left_arr))
    right_arr = list(filter(lambda point: abs(point.points[0] - mid_point.points[0]) <= closest[0], right_arr))

    for left_el in left_arr:
        for right_el in right_arr:
            if left_el.dim != right_el.dim:
                raise Exception("fatal error")
            found_bigger = False
            for j in range(left_el.dim):
                if abs(left_el.points[j] - right_el.points[j]) > closest[0]:
                    found_bigger = True
                    break
            if found_bigger:
                continue
            dist = left_el.get_distance_to(right_el)
            if dist < closest[0]:
                closest = dist, (left_el, right_el)

    return closest


if __name__ == "__main__":
    for _ in range(200):
        points = util.sort(util.generate_points(3, 20))
        Point.euclidean_count = 0
        dnc = get_closest_points(points, points)
        divnconq_num = Point.euclidean_count
        # Point.euclidean_count = 0
        brute = __get_brute_force__(points)
        # brute_num = Point.euclidean_count

        if not (brute[1][0] == dnc[1][0] and brute[1][1] == dnc[1][1]):
            print("ratna kontoooooooooool")

        print("brute: ", divnconq_num)
        util.visualise(points, dnc[1])
