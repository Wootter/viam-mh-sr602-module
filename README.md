# MH-SR602 PIR Motion Sensor Module for Viam

This is a Viam module for the MH-SR602 PIR (Passive Infrared) motion sensor on Raspberry Pi. The MH-SR602 is a mini PIR motion sensor that detects movement.

## Features

- Detects motion/movement
- GPIO interface
- Low power consumption
- Automatic sensor initialization
- Error handling and reporting

## Configuration

Add the sensor to your robot configuration:

```json
{
  "name": "motion-sensor",
  "model": "wootter:mh-sr602-sensor:linux",
  "type": "sensor",
  "namespace": "rdk",
  "attributes": {
    "pin": 17
  }
}
```

### Attributes

- `pin` (required): GPIO pin number where the sensor is connected

## Hardware Setup

1. Connect the MH-SR602 sensor to your Raspberry Pi:
   - VCC → 5V (or 3.3V depending on your model)
   - GND → Ground
   - OUT → GPIO pin (e.g., GPIO 17 / Pin 11)

2. Note: The sensor needs about 30-60 seconds to warm up when first powered on.

## Readings

The sensor returns the following readings:

```json
{
  "motion_detected": true,
  "pin": 17,
  "status": "motion"
}
```

When no motion is detected:

```json
{
  "motion_detected": false,
  "pin": 17,
  "status": "no_motion"
}
```

## Building

To build the module:

```bash
make module.tar.gz
```

## License

Apache-2.0
