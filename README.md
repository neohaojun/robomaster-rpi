# Raspberry Pi CAN Controller for DJI Robomaster

## Reference Projects

* [ROBOMASTER S1 の CAN データを受信してみる](https://wazalabo.com/robomaster_s1_jetson_can_connection.html)  
* [JohnieBraaf / Robomaster-Micropython](https://github.com/JohnieBraaf/Robomaster-Micropython)  
* [RoboMasterS1Challenge / robomaster_s1_can_hack](https://github.com/RoboMasterS1Challenge/robomaster_s1_can_hack)  
* [RoboMasterS1Challenge / robomaster_s1_ros_reference_design](https://github.com/RoboMasterS1Challenge/robomaster_s1_ros_reference_design)

## Technologies

This project was built with Python for the Raspberry Pi 4B with Waveshare's RS485 CAN HAT. It allows the RPi to control the DJI Robomaster S1 or EP without DJI's propietary Intelligent Controller.

## Usage and Installation

Connect the CANH and CANL wires on the Robomaster to the CANH and CANL pins on the RS485 CAN HAT. The Robomaster's CAN BUS can be intercepted at any CAN BUS port on the robot.

## Useful Information

### General

* Robomaster EP CAN BUS bitrate: 1 Mbps

### Robomaster EP CAN BUS Arbitration IDs

| ID | Description |
| --- | --- |
| 0x200 | self assigned |
| 0x201 | intelligent controller |
| 0x202 | motion controller |
| 0x203 | pitch motor (gimbal ???) |
| 0x204 | blaster |
| 0x211 | chassis rear armour |
| 0x212 | chassis front armour |
| 0x213 | chassis right armour |
| 0x214 | chassis left armour |
| 0x215 | gimbal right armour |
| 0x216 | gimbal left armour |
| 0x221 | turret infared distance sensor |

### Flags
| Flag | Description |
| --- | --- |
| 0x04 | chassis command flag |
| 0x08 | gimbal command flag |
| 0x1b | control message for chassis and gimbal |
| 0x15 | individual wheel control |
| 0x0E, 0x0F | control message for blaster |
