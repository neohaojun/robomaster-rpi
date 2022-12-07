# Project Logbook

## Exisiting Projects

[JohnieBraaf / Robomaster-Micropython](https://github.com/JohnieBraaf/Robomaster-Micropython)  
[RoboMasterS1Challenge / robomaster_s1_can_hack](https://github.com/RoboMasterS1Challenge/robomaster_s1_can_hack)
[RoboMasterS1Challenge / robomaster_s1_ros_reference_design](https://github.com/RoboMasterS1Challenge/robomaster_s1_ros_reference_design)

## Useful Information

### General

* Robomaster EP CAN BUS bitrate: 1 Mbps

### Robomaster EP CAN BUS Addresses (pulled from  JohnieBraaf / Robomaster-Micropython)

| Addresss | Description | Remarks |
| --- | --- | --- |
| x200 | 0 | self assigned |
| x201 | 1 | main control unit <-- we use this one |
| x202 | 2 | motion control unit |
| x203 | 3 | gimal |
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

## 2022-12-06

Original output with sample code:

Timestamp: 1670313186.882588        ID: 0004    S Rx E              DL:  8    00 04 00 00 00 00 00 00     Channel: can0  
Timestamp: 1670313186.887829        ID: 0004    S Rx E              DL:  8    00 10 00 00 00 00 00 00     Channel: can0

Output is errorneous (see 'E'); doing more comprehensive diagnostics tomorrow.

## 2022-12-07

Fixed faulty readings from yesterday by changing CAN BUS bitrate to 1Mbps (originally 100kbps)
