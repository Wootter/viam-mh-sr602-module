import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from .MH_SR602 import MHSR602, MHSR602Result


class MySensor(Sensor):
    """
    MH-SR602 PIR Motion Sensor for Raspberry Pi
    This sensor module detects motion using a MH-SR602 PIR sensor
    connected to a Raspberry Pi GPIO pin.
    """
    
    # Define the model of the sensor
    MODEL: ClassVar[Model] = Model(ModelFamily("wootter", "mh-sr602-sensor"), "linux")

    def __init__(self, name: str, pin: int):
        """
        Initialize the MH-SR602 motion sensor with the name and GPIO pin.
        
        Args:
            name: The name of the sensor component
            pin: The GPIO pin number where the MH-SR602 is connected
        """
        super().__init__(name)
        self.pin = pin
        # Create MH-SR602 sensor instance
        self.sensor = MHSR602(pin)
        # Initialize the sensor
        try:
            self.sensor.initialize()
        except Exception as e:
            print(f"Warning: Failed to initialize MH-SR602 sensor: {e}")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> "MySensor":
        """
        Create a new instance of the sensor using the configuration.
        
        Args:
            config: Component configuration containing the GPIO pin
            dependencies: Component dependencies (not used for this sensor)
            
        Returns:
            A new MySensor instance
        """
        # Extract the pin number from the configuration attributes
        pin = config.attributes.fields["pin"].number_value
        if not pin:
            raise ValueError("GPIO pin number must be specified in configuration")
        
        sensor = cls(config.name, int(pin))
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        """
        Read the motion detection state from the MH-SR602 sensor.
        
        Args:
            extra: Optional extra parameters
            **kwargs: Additional keyword arguments
            
        Returns:
            A dictionary containing motion detection status and timestamp,
            or an error message if reading fails
        """
        # Read from the MH-SR602 sensor
        result = self.sensor.read()
        
        if result.is_valid():
            return {
                "motion_detected": result.motion_detected,
                "pin": self.pin,
                "status": "motion" if result.motion_detected else "no_motion"
            }
        else:
            error_messages = {
                MHSR602Result.ERR_NOT_FOUND: "MH-SR602 sensor not responding on GPIO pin",
                MHSR602Result.ERR_READ_ERROR: "Error reading from MH-SR602 sensor"
            }
            error_msg = error_messages.get(result.error_code, "Unknown error from MH-SR602 sensor")
            return {
                "error": error_msg,
                "error_code": result.error_code,
                "pin": self.pin
            }


async def main():
    """
    Test function to verify sensor readings.
    This will be called when the module is run standalone.
    """
    # Create a new sensor object and get readings (using GPIO pin 17 as default)
    my_sensor = MySensor(name="motion_sensor", pin=17)
    print("MH-SR602 Motion Sensor Readings:")
    for i in range(10):
        readings = await my_sensor.get_readings()
        print(readings)
        await asyncio.sleep(1)


# Run the main function when the script is executed directly
if __name__ == '__main__':
    asyncio.run(main())