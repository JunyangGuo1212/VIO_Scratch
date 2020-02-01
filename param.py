import numpy as np

class Param:
    def __init__(self):
        ### USER SETTING ###
        self.noise_cam = False
        self.noise_gyro = False
        self.noise_acc = False

        self.imu_frequency = 100 #IMU的频率100hz
        self.cam_frequency = 10
        self.imu_timestep = 1./self.imu_frequency #时间间隔计算方式，0.01s
        self.cam_timestep = 1./self.cam_frequency
        self.t_start = 0.0 # 时间起始时间，０
        self.t_end = 20  # 持续时间

        # noise
        self.gyro_bias_sigma = 1.0e-5; # 陀螺仪偏置的标准差
        self.acc_bias_sigma = 0.0001; # 加速度计偏置的标准差

        self.gyro_noise_sigma = 0.015;   # 陀螺仪测量值的标准差 // rad/s * 1/sqrt(hz)　
        self.acc_noise_sigma = 0.019;    # 加速度计测量值的标准差  //　m/(s^2) * 1/sqrt(hz)

        self.pixel_noise = 1;             #1 pixel noise

        if ~self.noise_cam:
            self.pixel_noise = 0
        if ~self.noise_gyro:
            self.gyro_noise_sigma = 0
        if ~self.noise_acc:
            self.acc_noise_sigma = 0

        # cam f
        self.fx = 500
        self.fy = 500
        self.cx = 0
        self.cy = 0
        self.image_w = 1000
        self.image_h = 500

        # 外参数
        self.R_bc = np.zeros([3,3])   # cam to body
        self.t_bc = np.zeros([3,1])     # cam to body

        # visualize;
        self.if_visualize = True