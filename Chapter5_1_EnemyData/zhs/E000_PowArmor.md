# E000、E1940：PowArmor

## 掉落物类型

param中I（整数）的0号位决定了其在死亡后掉落的道具类型，对应关系如下

0 - 红色武器
1 - 蓝色武器
2 - 黄色武器
3 - 导弹
4 - Bit

## 生成后行为

PowArmor生成后默认会向前飞行，似乎没有办法通过参数控制生成后的姿态。向前飞行时如果碰到障碍物就会垂直下落，所以如果需要其生成后垂直下落，请在它生成位置的前方放置一个障碍物。