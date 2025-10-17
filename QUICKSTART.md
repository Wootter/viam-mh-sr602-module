# Quick Start - Deploy MH-SR602 Module

## 🚀 Fast Track to Deployment

### 1. Create GitHub Repository
Go to: https://github.com/new
- Repository name: `viam-mh-sr602-module`
- Public repository
- Don't initialize with README

### 2. Push Code to GitHub

```bash
cd "c:\Users\WoutDeelen\Desktop\github\Github Respitories\Viam\MH-SR602"

# Initialize git
git init
git add .
git commit -m "Initial commit: VEML7700 Viam module"

# Add remote and push
git remote add origin https://github.com/Wootter/viam-mh-sr602-module.git
git branch -M main
git push -u origin main
```

### 3. Get Viam API Keys

1. Visit: https://app.viam.com
2. Go to Organization Settings → API Keys
3. Click "Generate API Key"
4. **SAVE BOTH**: Key ID and Key Value

### 4. Add GitHub Secrets

1. Go to: https://github.com/Wootter/viam-veml7700-module/settings/secrets/actions
2. Add two secrets:
   - `VIAM_API_KEY_ID` = [your key ID]
   - `VIAM_API_KEY` = [your key value]

### 5. Deploy First Version

```bash
# Create and push version tag
git tag 1.0.0
git push origin 1.0.0
```

✅ **Done!** Watch the deployment at: https://github.com/Wootter/viam-mh-sr602-module/actions

### 6. Use in Viam

Add to your robot configuration:

```json
{
  "name": "my-motion-sensor",
  "model": "wootter:mh-sr602-sensor:linux",
  "type": "sensor",
  "namespace": "rdk",
  "attributes": {
    "pin": 17
  }
}
```

## 📝 Update Module Later

```bash
# Make changes, commit, and push
git add .
git commit -m "Your changes"
git push

# Create new version
git tag 1.0.1
git push origin 1.0.1
```

## 🔍 Verify Hardware

On your Raspberry Pi:

```bash
# Test GPIO access
gpio readall

# The sensor needs 30-60 seconds to warm up after power on
```

## ⚡ Test Sensor Locally

```bash
# On your Raspberry Pi
cd /path/to/MH-SR602
./setup.sh
source .env
$PYTHON -m src.motion_sensor
```

---

**Need help?** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.
