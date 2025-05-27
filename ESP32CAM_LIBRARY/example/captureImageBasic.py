import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from ESP32CAMWEB.ESP32CAM import ESP32CAM

# Create object with your camera IP
cam = ESP32CAM("192.168.1.100")

# Configure parameters
cam.setResolution("CIF")
cam.setQuality(10)
cam.setBrightness(0)

# Capture image
img = cam.capture()
if img is not None:
    with open("photo.jpg", "wb") as f:
        f.write(img.tobytes())
