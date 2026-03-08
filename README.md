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
- safe shutdown

## BOM
| Name | Description | URL | QTY | Price(€)
| :--: | :---------: | :-: | :-: | :-----:
| Raspberry Pi | 4 Model B 4GB | [Amazon](https://www.amazon.ie/Raspberry-Pi-ARM-Cortex-A72-1-50GHz-Bluetooth/dp/B07TC2BK1X/ref=sr_1_4) | 1 | 96
| MicroSD Card | 32GB | [Aliexpress](https://www.aliexpress.com/item/1005005262472106.html) | 1 | 6.66
| SSD | 500GB USB 3.0 | [Amazon](https://www.amazon.ie/Sonnics-External-Portable-transfer-Windows/dp/B0771LDDCW/ref=asc_df_B0771LDDCW) | 1 | 35.97
| OLED | 0.96 I2C | [Aliexpress](https://www.aliexpress.com/item/1005006141235306.html) | 1 | 2.63
| Fan | 40mm Cooling Fan | [Amazon](https://www.amazon.ie/GeeekPi-Raspberry-Brushless-Cooling-40x40x10mm/dp/B07X93XGBD/ref=sr_1_5) | 1 | 9.99
| Button | Red Push Button 2 Pin | [Aliexpress](https://www.aliexpress.com/item/10000274959292.html) | 1 | 1.61
| RGB LED | SK6812MINI-E | Owned - Reuse From Hackpad Kit | 1 | 0.00
| Power Supply | Offical Supply | [Aliexpress](https://www.aliexpress.com/item/1005004625705701.html) | 1 | 5.07
| Heat Sink | Blue kit | [Aliexpress](https://www.aliexpress.com/item/1005003083830470.html) | 1 | 2.36
|  |  |  | Shipping | 8.85
|  |  |  | Total | 161.51

## Images
| Schematic | Case | Finished Look
| :---: | :---: | :---:
| ![Image](https://github.com/user-attachments/assets/a97f8c04-a15a-4a98-8003-37b55bf0f6b8) | ![Image](https://github.com/user-attachments/assets/8fea5420-194c-4fa2-a3f7-f590dbe7e3d7) | ![Image](https://github.com/user-attachments/assets/f3cacc91-75bf-49c4-8f35-7c5dbf913712)
