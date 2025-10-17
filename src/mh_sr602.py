from gpiozero import MotionSensor
import time


class MHSR602Result:
    """Result object for MH-SR602 readings"""
    ERR_NO_ERROR = 0
    ERR_NOT_FOUND = 1
    ERR_READ_ERROR = 2

    def __init__(self, error_code, motion_detected):
        self.error_code = error_code
        self.motion_detected = motion_detected

    def is_valid(self):
        return self.error_code == MHSR602Result.ERR_NO_ERROR


class MHSR602:
    """
    MH-SR602 PIR Motion Sensor Driver
    This sensor detects motion using a PIR (Passive Infrared) sensor.
    """
    
    def __init__(self, pin):
        """
        Initialize the MH-SR602 motion sensor
        
        Args:
            pin: GPIO pin number where the sensor is connected
        """
        self.pin = pin
        self.pir = None
        self.initialized = False
        
    def initialize(self):
        """Initialize the motion sensor"""
        try:
            self.pir = MotionSensor(self.pin)
            # Give sensor time to warm up (PIR sensors need ~30-60 seconds)
            print(f"MH-SR602 on GPIO{self.pin} initializing... (warming up)")
            # Note: For production use, you may want to wait for inactive state
            # self.pir.wait_for_inactive()
            time.sleep(2)  # Short delay for initial setup
            self.initialized = True
            print(f"MH-SR602 on GPIO{self.pin} ready!")
        except Exception as e:
            raise Exception(f"Failed to initialize MH-SR602 sensor on GPIO{self.pin}: {e}")
    
    def read(self):
        """
        Read the motion detection state from the sensor
        
        Returns:
            MHSR602Result object containing the motion state or error code
        """
        try:
            if not self.initialized or self.pir is None:
                self.initialize()
            
            # Check if motion is detected
            motion_detected = self.pir.motion_detected
            
            return MHSR602Result(MHSR602Result.ERR_NO_ERROR, motion_detected)
            
        except AttributeError as e:
            # Sensor not properly initialized or found
            return MHSR602Result(MHSR602Result.ERR_NOT_FOUND, False)
        except Exception as e:
            # Other read errors
            return MHSR602Result(MHSR602Result.ERR_READ_ERROR, False)
    
    def cleanup(self):
        """Clean up GPIO resources"""
        if self.pir is not None:
            try:
                self.pir.close()
            except:
                pass
