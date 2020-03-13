import numpy as np

class MotionData:
    def __init__(self, t):
        self.timestamp = t
        # PVQ
        self.Rwb =  np.zeros([3,3])
        self.twb =  np.zeros([3,1])
        self.velocity = np.zeros([3,1])
        # bias
        self.imu_gyro_bias = np.zeros([3,1])
        self.imu_acc_bias = np.zeros([3,1])
        # 观测值
        self.imu_gyro = np.zeros([3,1])
        self.imu_acc = np.zeros([3,1])

        # pose的其他形式
        self.theta = 0
        self.Q = np.zeros([4,1])

    def setVelocity(self, vx, vy):
        self.velocity[0] = vx
        self.velocity[1] = vy

    def setT(self, x, y):
        self.twb[0] = x
        self.twb[1] = y

    def setPose(self, theta):
        self.theta = theta
        #EulerToQuaterion()
        #EulerToR()

    def setAcc(self, x, y):
        self.imu_acc[0] = x
        self.imu_acc[1] = y

    def setGyro(self, z):
        self.imu_gyro[2] = z

    def addIMUNoise(self):
        i = 0

    def testIMU(self):
        i = 0

    def testPreintegration(self):
        i = 0


class Observation:
    # 一个观测表示一个点被一个相机观察到
    def __init__(self, id_pt, id_cam, id_uv):
        self.id_pt = id_pt
        self.id_cam = id_cam
        self.id_uv = id_uv

class Point:
    def __init__(self):
        self.data = np.zeros([4, 1]) # 状态变量中，保存的变量；
        self.ids_observation = [] # 一个点会对应多个观测。

class Camera:
    def __init__(self):
        self.uvs = []
        self.ids_observation = []
