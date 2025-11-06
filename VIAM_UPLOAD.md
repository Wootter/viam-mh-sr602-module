# Upload MH-SR602 Module to Viam

This guide shows how to upload your MH-SR602 motion sensor module to Viam registry.

## Prerequisites

1. **Viam CLI installed** on your Raspberry Pi or development machine
2. **Viam API key** (get from https://app.viam.com)

## Installation

### Install Viam CLI

On your Raspberry Pi:

```bash
sudo curl -o /usr/local/bin/viam https://storage.googleapis.com/packages.viam.com/apps/viam-cli/viam-cli-stable-linux-arm64
sudo chmod +x /usr/local/bin/viam
```

Or on Linux/Mac:

```bash
sudo curl -o /usr/local/bin/viam https://storage.googleapis.com/packages.viam.com/apps/viam-cli/viam-cli-stable-linux-amd64
sudo chmod +x /usr/local/bin/viam
```

## Upload Module

### 1. Login to Viam

```bash
viam login
```

Or with API key:

```bash
viam login api-key --key-id="YOUR_KEY_ID" --key="YOUR_KEY"
```

### 2. Create Module (First Time Only)

```bash
viam module create --name mhsr602 --public-namespace wootter
```

### 3. Upload Module

From the MH-SR602 directory:

```bash
cd /path/to/MH-SR602
viam module upload --version 1.0.0 --platform linux/arm64
```

Or upload from tarball:

```bash
tar -czf mhsr602-module.tar.gz src/ run.sh requirements.txt meta.json
viam module upload --version 1.0.0 --platform linux/arm64 --module mhsr602-module.tar.gz
```

## Using the Module

### In Viam App

1. Go to https://app.viam.com
2. Navigate to your robot's **Config** tab
3. Click **Create component** → **sensor**
4. Select model: `wootter:sensor:mhsr602`
5. Configure:

```json
{
  "pin": 17
}
```

### Configuration

```json
{
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

## Testing Locally

Test the module on your Raspberry Pi:

```bash
cd /path/to/MH-SR602
./run.sh
```

## Readings

The sensor returns:

```json
{
  "motion_detected": true,
  "status": "motion"
}
```

## Troubleshooting

### Module Not Found
- Ensure you're logged in: `viam whoami`
- Check module exists: `viam module list`

### Permission Errors
- Make sure `run.sh` is executable: `chmod +x run.sh`
- Check GPIO permissions

### Sensor Errors
- Verify wiring
- Check GPIO pin number
- PIR sensors need 30-60 seconds to warm up after power on
