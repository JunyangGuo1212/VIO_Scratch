import numpy as np

class MotionData:
    def __init__(self):
        self.timestamp = 0.0
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

