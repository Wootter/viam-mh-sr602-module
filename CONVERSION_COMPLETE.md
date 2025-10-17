# MH-SR602 Module Setup Complete! ✅

## 🎯 What's Been Changed

Your MH-SR602 PIR motion sensor module is now ready for deployment with all VEML7700 references replaced:

### ✅ Files Updated:

1. **meta.json** - Changed to `wootter:mh-sr602-sensor`
2. **src/mh_sr602.py** - New PIR motion sensor driver using gpiozero
3. **src/motion_sensor.py** - New Viam sensor component (replaces light_sensor.py)
4. **src/__init__.py** - Updated imports for motion sensor
5. **src/main.py** - Updated imports for motion sensor
6. **requirements.txt** - Changed to `gpiozero` and `RPi.GPIO`
7. **pyproject.toml** - All references updated to mh-sr602
8. **config.example.json** - Updated to use pin instead of bus_number
9. **README.md** - Updated documentation for motion sensor
10. **setup.sh** - Updated comments
11. **.github/workflows/deploy.yml** - Updated module name
12. **QUICKSTART.md** - Updated all references and commands

### ❌ Files Removed:
- `src/veml7700.py` - Not needed for PIR sensor
- `src/light_sensor.py` - Replaced with motion_sensor.py

## 📊 Module Configuration

**Module ID**: `wootter:mh-sr602-sensor`
**Model**: `wootter:mh-sr602-sensor:linux`
**API**: `rdk:component:sensor`

**Configuration Attributes**:
```json
{
  "pin": 17
}
```

**Sensor Output**:
```json
{
  "motion_detected": true,
  "pin": 17,
  "status": "motion"
}
```

## 🚀 Ready to Deploy

### 1. Create GitHub Repository
- Name: `viam-mh-sr602-module`
- URL: `https://github.com/Wootter/viam-mh-sr602-module`

### 2. Deploy Commands

```powershell
cd "c:\Users\WoutDeelen\Desktop\github\Github Respitories\Viam\MH-SR602"

# Initial commit
git commit -m "Initial commit: MH-SR602 PIR motion sensor module"

# Add remote
git remote add origin https://github.com/Wootter/viam-mh-sr602-module.git

# Push to GitHub
git branch -M main
git push -u origin main

# Deploy version 1.0.0
git tag 1.0.0
git push origin 1.0.0
```

### 3. Add GitHub Secrets
Same as before:
- `VIAM_API_KEY_ID`
- `VIAM_API_KEY`

## 🔌 Hardware Setup

**MH-SR602 Connections**:
- VCC → 5V (or 3.3V)
- GND → Ground
- OUT → GPIO 17 (Pin 11) or your chosen pin

**Important**: PIR sensor needs 30-60 seconds warm-up time!

## 🎓 Using in Viam

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

## 🔄 Key Differences from VEML7700

| Feature | VEML7700 | MH-SR602 |
|---------|----------|----------|
| **Type** | Light sensor | Motion sensor |
| **Interface** | I2C (bus_number) | GPIO (pin) |
| **Output** | Lux value | Motion detected (true/false) |
| **Library** | smbus2 | gpiozero |
| **Warm-up** | ~2 seconds | 30-60 seconds |

## ✨ All Set!

Your MH-SR602 module is ready to be pushed to GitHub and deployed to Viam! 🎉

Follow the **QUICKSTART.md** for deployment instructions.
