# Project Logbook

## Reference Projects

* [ROBOMASTER S1 の CAN データを受信してみる](https://wazalabo.com/robomaster_s1_jetson_can_connection.html)  
* [JohnieBraaf / Robomaster-Micropython](https://github.com/JohnieBraaf/Robomaster-Micropython)  
* [RoboMasterS1Challenge / robomaster_s1_can_hack](https://github.com/RoboMasterS1Challenge/robomaster_s1_can_hack)  
* [RoboMasterS1Challenge / robomaster_s1_ros_reference_design](https://github.com/RoboMasterS1Challenge/robomaster_s1_ros_reference_design)

## Useful Information

### General

* Robomaster EP CAN BUS bitrate: 1 Mbps

### Robomaster EP CAN BUS Addresses

| Addresss | Description | Remarks |
| --- | --- | --- |
| x200 | 0 | self assigned |
| x201 | 1 | main control unit |
| x202 | 2 | motion control unit |
| x203 | 3 | gimbal |
| x204 | 4 | blaster |
| x211 | 5 | armor back |
| x212 | 6 |
| x213 | 7 |
| x214 | 8 |
| x215 | 9 |
| x216 | 10 | 

### Flags
| Flag | Description |
| --- | --- |
| 0x04 | chassis command flag |
| 0x08 | gimbal command flag |
| 0x1b | control message for chassis and gimbal |
| 0x15 | individual wheel control |
| 0x0E, 0x0F | control message for blaster |