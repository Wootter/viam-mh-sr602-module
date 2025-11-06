from typing import ClassVar, Mapping, Any, Optional
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger
import asyncio
import time
import RPi.GPIO as GPIO

LOGGER = getLogger(__name__)


class MH_SR602(Sensor, Reconfigurable):
    """
    MH-SR602 PIR Motion Sensor for Raspberry Pi
    This sensor detects motion using a MH-SR602 PIR sensor
    connected to a Raspberry Pi GPIO pin using RPi.GPIO library.
    """
    
    MODEL: ClassVar[Model] = Model(ModelFamily("wootter", "sensor"), "mhsr602")

    def __init__(self, name: str):
        """
        Initialize the MH-SR602 motion sensor
        
        Args:
            name: The name of the sensor component
        """
        super().__init__(name)
        self.pin = None
        LOGGER.info(f"{self.__class__.__name__} initialized.")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        """
        Create a new instance of the sensor using the configuration.
        
        Args:
            config: Component configuration containing the GPIO pin
            dependencies: Component dependencies (not used for this sensor)
            
        Returns:
            A new MH_SR602 instance
        """
        instance = cls(config.name)
        instance.reconfigure(config, dependencies)
        return instance

    @classmethod
    def validate(cls, config: ComponentConfig):
        """
        Validate the configuration for the MH-SR602 sensor.
        
        Args:
            config: Component configuration to validate
            
        Returns:
            Tuple of (dependencies, warnings)
        """
        if "pin" not in config.attributes.fields:
            raise Exception("'pin' must be defined in the configuration.")
        return ([], [])

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        """
        Reconfigure the sensor with new settings.
        
        Args:
            config: New component configuration
            dependencies: Component dependencies
        """
        self.pin = int(config.attributes.fields["pin"].number_value)
        
        # Setup GPIO using RPi.GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        
        LOGGER.info(f"MH-SR602 configured on GPIO{self.pin}")

    async def get_readings(self, extra: Optional[Mapping[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        """
        Read the motion detection state from the MH-SR602 sensor.
        
        Args:
            extra: Optional extra parameters
            **kwargs: Additional keyword arguments
            
        Returns:
            A dictionary containing motion detection status
        """
        try:
            if self.pin is None:
                raise Exception("MH-SR602 sensor not configured")
            
            # Read GPIO pin state (HIGH = motion detected, LOW = no motion)
            motion_detected = await asyncio.to_thread(GPIO.input, self.pin)
            
            # Convert to boolean (1 = True, 0 = False)
            motion_detected = bool(motion_detected)
            
            LOGGER.info(f"Motion: {'DETECTED' if motion_detected else 'None'}")
            
            return {
                "motion_detected": motion_detected,
                "status": "motion" if motion_detected else "no_motion"
            }
            
        except Exception as e:
            error_msg = f"Error reading from MH-SR602 sensor: {str(e)}"
            LOGGER.error(error_msg)
            return {
                "error": error_msg,
                "motion_detected": False
            }

    async def close(self):
        """
        Clean up GPIO resources when the module is shut down.
        """
        await asyncio.to_thread(GPIO.cleanup)
        LOGGER.info("MH-SR602 sensor closed and GPIO cleaned up")