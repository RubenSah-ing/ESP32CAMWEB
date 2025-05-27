# Author / Ingeniero: Ruben Sahuquillo Redondo
# Version: 1.0.0
# License: CC BY (Creative Commons License Atribution)
# Description: This sketch allows to control an ESP32 CAM via HTTP. ESP32 CAM uses default Arduino IDE sketch named "CameraWebServer.ino"
#======================================================================#

#LIBRARIES
import requests
import numpy as np

#CLASS
class ESP32CAM:

    #CONSTRUCTOR
    def __init__(self, ip):
        """Definition: Iniciate ESP32 CAM with default parameters"""
        self.ip = ip
        self.url = f'http://{ip}'
        self.resolution = 5
        self.quality = 0
        self.brightness = 0
        self.contrast = 0
        self.saturation = 0
        self.effect = 0
        self.awb = 1
        self.auto_exposition = 0
        self.led_intensity = 0

    #STR
    def __str__(self):
        return f"ESP32CAM @ {self.ip} | Resolución: {self.resolution}, Calidad: {self.quality}"

    #REPR
    def __repr__(self):
        return (f"ESP32CAM(ip='{self.ip}', resolution={self.resolution}, quality={self.quality}, "
                f"brightness={self.brightness}, contrast={self.contrast}, saturation={self.saturation}, "
                f"effect={self.effect}, awb={self.awb}, auto_exposition={self.auto_exposition}, "
                f"led_intensity={self.led_intensity})")

    #CAPTURE IMAGE
    def captureImage(self):
        """Definition: Take a photo with ESP32 CAM"""
        response = requests.get(f"{self.url}/capture", stream=True)
        if response.status_code == 200:
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            return img_array
        else:
            print("Error al capturar la imagen.")
            return None

    #PRIVATE METHODE
    def _setControl(self, var, value):
        try:
            requests.get(f"{self.url}/control?var={var}&val={value}")
        except requests.RequestException as e:
            return False

    #SETTERS
    def setResolution(self, resolution:str):
        """Definition: Set an image resolution
        Resolutions available: 
        96x96: 0    QQVGA: 1    QCIF: 2     HQVGA: 3    QVGA: 4     CIF: 5      VGA: 6      SVGA: 7     XGA: 8      SXGA: 9
        UXGA: 10    FHD: 11     PHD: 12     HD: 13      VGA2: 14    QVGA2: 15"""
        
        resolutions = {"96X96": 0, "QQVGA": 1, "QCIF": 2, "HQVGA": 3,"QVGA": 4, "CIF": 5, "VGA": 6, "SVGA": 7,"XGA": 8, "SXGA": 9, "UXGA": 10, "FHD": 11,"PHD": 12, "HD": 13, "VGA2": 14, "QVGA2": 15}
        self.resolution = resolutions.get(resolution.upper(), 5)
        self._setControl("framesize", self.resolution)

    def setQuality(self, value:int):
        """Defintiion: Set image quality"""
        if (4 <= value <= 63):
            self.quality = value
            self._setControl("quality", self.quality)
        else:
            print("Quality no valid (4 - 63)")
            return

    def setBrightness(self, value:int):
        """Definition: Set image brightness"""
        if (-2 <= value <= 2):
            self.brightness = value
            self._setControl("brightness", self.brightness)
        else:
            print("Brightness no valid (-2 - +2)")
            return

    def setContrast(self, value:int):
        """Definition: Set image contrast"""
        if (-2 <= value <= 2):
            self.contrast = value
            self._setControl("contrast", self.contrast)
        else:
            print("Contrast no valid (-2 - +2)")
            return

    def setSaturation(self, value:int):
        """Definition: Set image saturation"""
        if (-2 <= value <= 2):
            self.saturation = value
            self._setControl("saturation", self.saturation)
        else:
            print("Saturation no valid (-2 - +2)")
            return
   
    def setEffect(self, value:int):
        """Definition: Set image effect"""
        self.effect = value
        self._setControl("special:effect", self.effect)

    def setAWB(self, value:int):
        """Definition: Set Auto White Balance"""
        if value in (0, 1):
            self.awb = value
            self._setControl("framesize", self.awb)
        else:
            print("AWB no valid (0 or 1)")
            return

    def setAutoExposition(self, value):
        """Definition: Set Auto Exposition"""
        if (-2 <= value <= 2):
            self.auto_exposition = value
            self._setControl("ae", self.auto_exposition)
        else:
            print("AE no valid (0 or 1)")
            return

    def setLedIntensity(self, value:int):
        """Definition: Set LED Intensity"""
        if (0 <= value <= 255):
            self.led_intensity = value
            self._setControl("led_intensity", self.led_intensity)
        else:
            print("LED intensity no valid (0 - 255)")
            return

    #GETTERS
    def getIP(self) -> str:
        """Definition: return ESP32CAM IP"""
        return self.ip

    def getResolutions(self):
        """Definition: return resolutions available"""
        return "96x96: 0\nQQVGA: 1\nQCIF: 2\nHQVGA: 3\nQVGA: 4\nCIF: 5\nVGA: 6\nSVGA: 7\nXGA: 8\nSXGA: 9\nUXGA: 10\nFHD: 11\nPHD: 12\nHD: 13\nVGA2: 14\nQVGA2: 15"  

    def getParameters(self):
        """Definition: return all ESP32 CAM actual parameters"""
        return {
        "resolution": self.resolution,
        "quality": self.quality,
        "brightness": self.brightness,
        "contrast": self.contrast,
        "saturation": self.saturation,
        "effect": self.effect,
        "awb": self.awb,
        "auto_exposition": self.auto_exposition,
        "led_intensity": self.led_intensity
        }