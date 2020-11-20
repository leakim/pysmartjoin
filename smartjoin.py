#!/usr/bin/env python3
"""
Wi-Fi settings as a QR-code

https://smartjoin.us/

https://smartjoin.us/rfcs/wifi-url.html
"""


import sys
import argparse
import qrcode


def main():
    parser = argparse.ArgumentParser(description='Generate QR from wifi settings')
    parser.add_argument('ssid')
    parser.add_argument('passwd')
    parser.add_argument('file', default='wifi.png')
    opt = parser.parse_args(sys.argv[1:])

    wifiuri = f'WIFI:S:{opt.ssid};T:WPA;P:{opt.passwd};;'

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(wifiuri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(opt.file)


if __name__ == '__main__':
    main()
