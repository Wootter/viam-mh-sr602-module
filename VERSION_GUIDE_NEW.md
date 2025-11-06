# Using MH-SR602 Module Versions in Viam

## Overview

The **MH-SR602** PIR motion sensor module for Viam.

- **Model**: `wootter:sensor:mhsr602`
- **Module ID**: `wootter:mhsr602`
- **Description**: Motion detection using MH-SR602 PIR sensor

## Quick Start

### 1. Tag and Deploy

```bash
# Navigate to your MH-SR602 directory
cd /path/to/MH-SR602

# Create a new version tag (without 'v' prefix)
git tag 1.0.0
git push origin 1.0.0

# GitHub Actions will automatically build and deploy
```

### 2. Configure in Viam

In your Viam robot configuration:

1. **Add Module**:
   - **Module ID**: `wootter:mhsr602`
   - **Version**: `1.0.0` (or `latest`)

2. **Add Component**:
   - **Type**: `sensor`
   - **Model**: `wootter:sensor:mhsr602`
   - **Name**: `motion_sensor` (or any name you want)

3. **Configure Attributes**:
```json
{
  "pin": 17
}
```

## Example Configuration

```json
{
  "modules": [
    {
      "type": "registry",
      "name": "wootter_mhsr602",
      "module_id": "wootter:mhsr602",
      "version": "1.0.0"
    }
  ],
  "components": [
    {
      "name": "motion_sensor",
      "model": "wootter:sensor:mhsr602",
      "type": "sensor",
      "namespace": "rdk",
      "attributes": {
        "pin": 17
      }
    }
  ]
}
```

## Hardware Setup

Connect your MH-SR602 sensor:
- **VCC** → 5V (Pin 2 or 4)
- **GND** → Ground (Pin 6, 9, 14, 20, 25, 30, 34, or 39)
- **OUT** → GPIO 17 (Pin 11) or any GPIO pin

## Readings

The sensor returns motion detection status:

```json
{
  "motion_detected": true,
  "status": "motion"
}
```

or when no motion:

```json
{
  "motion_detected": false,
  "status": "no_motion"
}
```

## Notes

- PIR sensors need 30-60 seconds to warm up after power-on
- The sensor will stay HIGH while motion is detected
- Sensitivity and delay can be adjusted with onboard potentiometers
