# E000, E1940: PowArmor

## Drop Item Types

The 0th bit of I (integer) in the param determines the type of item it will drop upon death. The mapping is as follows:

0 - Red Weapon  
1 - Blue Weapon  
2 - Yellow Weapon  
3 - Missile  
4 - Bit

## Behavior After Generation

After PowArmor is generated, it will default to flying forward. It seems there is no way to control its posture after generation through parameters. If it hits an obstacle while flying forward, it will fall vertically. Therefore, if you want it to fall vertically after generation, place an obstacle in front of its spawn location.
