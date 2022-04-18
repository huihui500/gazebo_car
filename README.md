# gazebo_pkg
> 该版本为第一代仿真车辆，目前只搭配了最简单的结构，只有转弯与前进；与实车相比需要对于转弯做一个映射；效果可能会不如人意

## 文件结构
### gazebo_pkg
├── CMakeLists.txt
├── launch
│   └── race.launch
├── meshes
│   ├── bot.dae
│   └── hokuyo.dae
├── package.xml
├── urdf
│   ├── robot.pdf：小车结构
│   └── waking_robot.xacro：小车模型
└── world
    └── race_with_cone.world：赛道环境

### gazebo_control
├── CMakeLists.txt
├── msg
│   └── RealCar_ctl.msg:发送给实车的控制命令
├── package.xml
└── scripts
    ├── draw_circle.py：圆形轨迹
    └── real_car_ctl_sim.py：仿真映射到实车

## Run
- 仿真环境和仿真小车启动: `roslaunch gazebo_pkg race.launch`
- 键盘控制小车运动:`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
- 小车做圆周运动:`rosrun gazebo_control draw_circle.py`
- 实车与仿真车映射:`rosrun gazebo_control real_car_ctl.py`
