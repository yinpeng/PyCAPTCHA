'''Captcha.Visual.PILImports

This package is used for wrapping the PIL modules to support both PIL and Pillow.
Pillow is a PIL fork. Pillow 2.0.0 adds Python 3 support and includes many bug fixes from around the Internet.
Details about Pillow: https://pypi.python.org/pypi/Pillow/2.0.0
'''

try:
    from PIL import Image, ImageDraw, ImageFont
except:
    import Image, ImageDraw, ImageFont
