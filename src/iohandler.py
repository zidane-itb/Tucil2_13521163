import time

import util
from point import Point
import solver


def start_io():
    print("masukkan data dengan format: dimensi<spasi>banyak_titik")

    inp: list[str]
    dim: int
    num: int

    while True:
        inp = input(">> ").split(" ")

        if len(inp) != 2:
            print("format input salah")
            continue

        try:
            dim = int(inp[0])
            num = int(inp[1])
        except ValueError:
            print("format input salah")
            continue

        if dim < 2 or num < 2:
            print("input tidak valid. batasan: dim >= 2 dan num >= 2")
            continue

        break

    start = time.time_ns()
    points = util.sort(util.generate_points(3, 20))
    Point.euclidean_count = 0
    res = solver.get_closest_points(points, points)
    end = time.time_ns()

    print("pasang titik terdekat: \n", res[1][0], '\n', res[1][1])
    print("banyak operasi euclidean distance:", Point.euclidean_count)
    print("waktu (points generation, sort, main dnc):", float(end - start) / 1000000000, "s")
    print("spesifikasi komputer: Intel Core i7-10750H, Intel UHD")

    if dim == 3:
        vis = input("tampilkan visualisasi 3d? (y/any): ")
        if vis.lower() == 'y':
            util.visualise(points, res[1])


if __name__ == '__main__':
    start_io()
