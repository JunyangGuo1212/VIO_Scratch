from datastruct import MotionData
from param import Param
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #将地图中的点生成；
    points = np.mat('0, 0, 0, 0, 2 2 -6 -6 -6 -6 -7 -7   -7   -7 -7.5 -7.5 -9 -9 -9 -9 -11 -11; '
                    '0, 2, 5, 6, 2 6 0  2   4  6  0  1.5  1.75 2  1     2   0 2  3   6  0   3')
    size_pts = points[0].size
    plt.scatter(y = np.asarray(points[0]),x= np.asarray(points[1]))
    links = np.mat('0 1 1 4 3 0 6 8 3 6  10 12 13 14 10 16 17 18 19 20 20 18;'
                   '1 2 4 5 5 6 7 9 9 10 11 13 7 15  16 17 15 19 9 16  21 21')
    size_link = links[0].size
    for id_link in range(size_link):
        id_s = np.asarray(links[0])[0][id_link]
        id_e = np.asarray(links[1])[0][id_link]
        x = np.asarray(points[1])[0][[id_s, id_e]]
        y = np.asarray(points[0])[0][[id_s, id_e]]
        plt.plot(x, y)
    plt.gca().invert_xaxis()
    plt.axes().set_aspect('equal')
    plt.show()





