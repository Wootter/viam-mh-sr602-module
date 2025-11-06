# [MH-SR602 modular service](https://app.viam.com/module/wootter/sensor/mhsr602)

This module implements the [rdk sensor API](https://github.com/rdk/sensor-api) in a `wootter:sensor:mhsr602` model.
With this model, you can detect motion using an MH-SR602 PIR motion sensor.

## Requirements

The MH-SR602 sensor must be connected to a Raspberry Pi GPIO pin.

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the [`wootter:sensor:mhsr602` module](https://app.viam.com/module/wootter/sensor/mhsr602).

## Configure your sensor

> [!NOTE]  
> Before configuring your sensor, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

* Navigate to the **Config** tab of your robot's page in [the Viam app](https://app.viam.com/).
* Click on the **Components** subtab and click the `sensor` subtab.
* Select the `wootter:sensor:mhsr602` model. 
* Enter a name for your sensor and click **Create**.
* On the new component panel, copy and paste the following attribute template into your sensor's **Attributes** box:

```json
{
  "pin": 17
}
```
* Save and wait for the component to finish setup

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `wootter:sensor:mhsr602` sensor:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `pin` | integer | **Required** | GPIO pin number where the MH-SR602 output pin is connected |

### Example Configuration

```json
{
  "pin": 17
}
```

## Hardware Setup

Connect your MH-SR602 sensor:
- **VCC** → 5V
- **GND** → Ground
- **OUT** → GPIO pin (e.g., GPIO 17)

## Readings

The sensor returns:

```json
{
  "motion_detected": true
}
```
