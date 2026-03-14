# SurfNAS
A simple NAS ran by a raspberry pi

## How To Run
To Use this youll have to run a few commands in terminal first and download Raspberry Pi OS

### Install Libraries
Install [Raspberry Pi OS](https://downloads.raspberrypi.com/raspios_arm64/images/raspios_arm64-2025-12-04/2025-12-04-raspios-trixie-arm64.img.xz)
Open Terminal and Run
```
sudo apt update
sudo apt install python3-pip git
```
Then  Install Libraries
```
pip3 install adafruit-circuitpython-neopixel
pip3 install adafruit-circuitpython-ssd1306
pip3 install psutil
pip3 install pillow
```
This will Control
- OLED
- RGB LED
- system stats

### Enable I2C for the OLED
Run
```
sudo raspi-config
```
Then
```
Interface Options
→ I2C
→ Enable
```

### Run the Firmware
Make sure youve install [Nano SurfNAS.py](https://github.com/anadskman/SurfNAS/blob/main/Software/nano%20surfnas.py)

```
python3 surfnas.py
```
This Should Happen
- OLED showing stats
- LED changing color
- button shuts down system

### Start It Automatically
Create a systemd service
```
sudo nano /etc/systemd/system/surfnas.service
```
Paste
```
[Unit]
Description=SurfNAS Display Service
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/surfnas.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```
Enable It
```
sudo systemctl enable surfnas
sudo systemctl start surfnas
```
### What SurfNAS Should Show
OLED screen:
- SurfNAS
- CPU: 23%
- RAM: 41%
- Disk: 18%

LED:
| **Color** | **Meaning**
| :---: | :---:
| Green	| normal
| Orange | moderate load
| Red	heavy | load

Button:
- Power Control

## BOM
| Name | Description | URL | QTY | Price(€)
| :--: | :---------: | :-: | :-: | :-----:
| Raspberry Pi Zero 2 WH | To Run the Server | [Amazon](https://www.amazon.ie/Raspberry-Pi-Zero-2-WH/dp/B0DB2JBD9C/ref=sr_1_3?crid=75NOUMW2B30M&dib=eyJ2IjoiMSJ9.a8XewMBfs2OnePNN-x_G38hOn-Suktse4A2oxV5Tje9QZ_s28JpuIKnAaLIjiuB5OA21_Tf_XS64fLxdkS1wLoIVFrXIwxCw25WlXxFeYAiBmNpNsOYJiWVxwVSTmGlW4M4qh3J7naJ--w8vSAXS9svXSvz7osYIlDKNfma24cFyg5eqbgP7H_9vY3JgWUC-QsnEz5c7SxEPvGvmDj3FJaeZgmH6-lw9u3lX3pPFZ_tVxeR7kESPbUTsgBrTgi_gL75hQVvYcn_NRF6aMyGUsfR9x4fUnJmnwRII1JRwCHU.QaWUsuW0TnTlb2wd-jJBo0U-IPZ6ey_yj3oP0t_v9Ko&dib_tag=se&keywords=Orange+Pi+Zero+2W&qid=1773491162&s=electronics&sprefix=orange+pi+zero+2w%2Celectronics%2C353&sr=1-3) | 1 | 24.55
| MicroSD Card | 32GB | [Aliexpress](https://www.aliexpress.com/item/1005005262472106.html) | 1 | 6.66
| SSD | 128GB USB 3.0 | [Amazon](https://www.amazon.ie/gp/product/B0C1SD95B7/ref=ox_sc_act_title_2?smid=A22S87YMRWR0XZ&psc=1) | 1 | 20.99
| OLED | 0.96 I2C | [Aliexpress](https://www.aliexpress.com/item/1005006141235306.html) | 1 | 2.63
| Fan | 40mm Cooling Fan | [Amazon](https://www.amazon.ie/GeeekPi-Raspberry-Brushless-Cooling-40x40x10mm/dp/B07X93XGBD/ref=sr_1_5) | 1 | 9.99
| Button | Red Push Button 2 Pin | [Aliexpress](https://www.aliexpress.com/item/10000274959292.html) | 1 | 1.61
| RGB LED | SK6812MINI-E | Owned - Reuse From Hackpad Kit | 1 | 0.00
| Heat Sink | Blue kit | [Aliexpress](https://www.aliexpress.com/item/1005003083830470.html) | 1 | 2.36
|  |  |  | Shipping | 4.89
|  |  |  | Total | 73.68

## Images
| Schematic | Case | Finished Look
| :---: | :---: | :---:
| ![Image](https://github.com/user-attachments/assets/a97f8c04-a15a-4a98-8003-37b55bf0f6b8) | ![Image](https://github.com/user-attachments/assets/8fea5420-194c-4fa2-a3f7-f590dbe7e3d7) | ![Image](https://github.com/user-attachments/assets/f3cacc91-75bf-49c4-8f35-7c5dbf913712)
