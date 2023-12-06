import base64

with open('test.png', 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    print(base64_bytes)
