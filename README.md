# QR_CODE-_Generator


A simple Python script that generates QR codes for URLs using the `qrcode` library.

## Description

This project creates a QR code that links to a web page demonstrating CSS keyframe animations. The generated QR code can be scanned with any smartphone camera or QR code reader to quickly access the linked content.

## Features

- Clean, customizable QR code generation
- Adjustable size and border settings
- Black and white color scheme for optimal scanning
- Saves output as PNG image

## Requirements

- Python 3.x
- qrcode library

## Installation

Install the required library using pip:
```bash
pip install qrcode[pil]
```

## Usage

1. Clone or download this repository
2. Update the `website_link` variable in `qr_code.py` with your desired URL
3. Run the script:
```bash
python qr_code.py
```

4. The QR code will be saved as `QR_Code.png` in the same directory

## Configuration

You can customize the QR code by modifying these parameters:

- `version`: Controls the size (1 is smallest, increases complexity)
- `box_size`: Size of each box in pixels (default: 5)
- `border`: Border thickness in boxes (default: 5)
- `fill_color`: QR code color (default: 'black')
- `back_color`: Background color (default: 'white')

## Example Output

The script generates a scannable QR code linking to: https://kishu01karb.github.io/Animate-Images-with-keyframes-using-CSS/

## License

This project is open source and available for personal and educational use.
