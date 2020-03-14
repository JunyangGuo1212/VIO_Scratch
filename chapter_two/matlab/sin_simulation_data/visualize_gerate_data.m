function [outputArg1,outputArg2] = visualize_gerate_data(app)
%VISUALIZE_GERATE_DATA 此处显示有关此函数的摘要
%   此处显示详细说明
load('data/sinmotiondata');
% for x/y
size_motion = length(motiondatas);
xs = zeros(size_motion,1);
ys = zeros(size_motion,1);
axs = zeros(size_motion,1);
ays = zeros(size_motion,1);
vxs = zeros(size_motion,1);
vys = zeros(size_motion,1);
thetas = zeros(size_motion,1);
for i = 1:size_motion
    motiondata = motiondatas(i);
    xs(i,1) = motiondata.x;
    ys(i,1) = motiondata.y;  
    axs(i,1) = motiondata.ax;
    ays(i,1) = motiondata.ay;
    vxs(i,1) = motiondata.vx;
    vys(i,1) = motiondata.vy;
    thetas(i,1) = motiondata.theta;
end

scatter(app.UIAxes,xs,ys);
%velocity 
plot(app.UIAxes_2, vxs);
hold(app.UIAxes_2, 'on'); plot(app.UIAxes_2, vys);
legend(app.UIAxes_2, 'velocity x','velocity y');
% acceleration
plot(app.UIAxes_3, axs);
hold(app.UIAxes_3, 'on'); plot(app.UIAxes_3, ays);
legend(app.UIAxes_3, 'accelerate x','accelerate y');
end

