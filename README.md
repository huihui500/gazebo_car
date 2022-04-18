# gazebo_pkg
> 该版本为第一代仿真车辆，目前只搭配了最简单的结构，只有转弯与前进；与实车相比需要对于转弯做一个映射；效果可能会不如人意

## 后续改进点
|  改进点  |    难度    |  优先级  |
|   --    |     --    |    --   |
| 修改仿真小车的物理参数:大小,惯性等  |  易  | 中  |   
| 舵机映射修正 | 难  |  中  |   
| 编码器电机映射修正 |  易 | 中  |   
| 小车模型升级为阿克曼车模  | 中  | 高  |   


## 混合现实评测指标
- 给定不同的方向角与速度,小车会跑圆形轨迹,对比
  - 二者半径的相对误差: 
    $r_0 = \frac{\left\lvert {R_{real}-R_{sim}} \right\rvert}{R_{real}}$
- 给定一个指令序列,对运动轨迹差别量化:
  - 路径偏离度
   
## 文件结构介绍
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
    └── race_with_cone.world：环境

### gazebo_control
├── CMakeLists.txt
├── msg
│   └── RealCar_ctl.msg:发送给实车的控制命令
├── package.xml
└── scripts
    ├── draw_circle.py：圆形轨迹
    └── real_car_ctl_sim.py：仿真映射到实车

## demo
- 仿真环境和仿真小车启动: `roslaunch gazebo_pkg race.launch`
- 键盘控制小车运动:`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
- 小车做圆周运动:`rosrun gazebo_control draw_circle.py`
- 实车与仿真车映射(未完善):`rosrun gazebo_control real_car_ctl.py`

## Q&A
1. py文件rosrun运行失败，显示非可执行文件
> 解决: `chmod +x A.py`