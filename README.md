# QR Code Scanner

This Python program uses OpenCV and Pyzbar to scan QR codes using the webcam.  
It splits QR code data into separate columns and saves it to a CSV file with a timestamp.

## Features
- Live webcam QR detection
- Mirrored camera view
- Automatically saves QR data into CSV
- Avoids duplicate entries until a new QR appears

## Requirements
- Python 3.8+
- Libraries:
  - OpenCV (`opencv-python`)
  - Pyzbar (`pyzbar`)
  - Numpy (`numpy`)

Install dependencies using:
```bash
pip install -r requirements.txt
