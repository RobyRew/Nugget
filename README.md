![Artboard][NuggetLogo]

# Nugget - Complete Documentation

> **Unlock your device's full potential! **
> 
> Customize your device with animated wallpapers, disable pesky daemons, and more! 

---

## ⚠️ CRITICAL WARNINGS

> [! CAUTION]
> **BACKUP YOUR DATA BEFORE USING NUGGET!**
> Nugget may cause unforeseen problems.  We are not responsible for any damage done to your device.

> [!WARNING]
> **iOS 26.2+ is NOT supported and NEVER will be. ** Apple has patched the exploits permanently. 
> Do not ask for iOS 26.2+ support — it will never happen.

> [!IMPORTANT]
> **Skip Setup does NOT work with BookRestore (iOS 18.2+)**
> If you're on iOS 18.2-26.1, the Setup Assistant may appear after applying certain tweaks.
> This is a known limitation, not a bug. 

---

## ✨ Features by iOS Version

### iOS 17.0 - 26.0+ (All Versions)

#### PosterBoard (Animated Wallpapers)
- Import community wallpapers from [cowabun. ga/wallpapers](https://cowabun.ga/wallpapers)
- Convert videos to live wallpapers
- Customize wallpapers via batter files
- Create custom tendies files

#### Status Bar Tweaks
| Tweak | Description |
|-------|-------------|
| Carrier Name | Change primary carrier text |
| Secondary Carrier | Change secondary carrier text |
| WiFi/Cellular Bars | Set custom bar count (0-4) |
| Battery Capacity | Show custom battery percentage |
| Time Text | Custom time display |
| Date Text | Custom date (iPad only) |
| Breadcrumb Text | Change "Back to..." text |
| Numeric Strength | Show actual WiFi/cellular dBm |
| Hide Icons | Hide any status bar icon |

#### Springboard Options
- Lock Screen Footnote
- Auto-Lock Time
- Disable Lock After Respring
- Disable Screen Dimming While Charging
- Disable Low Battery Alerts
- Hide AC Power on Lock Screen
- Show Supervision Text
- Dynamic Island in Screenshots
- AirPlay for Stage Manager
- Authentication Line on Lock Screen
- Disable Floating Tab Bar (iPad)

#### Internal Options
- Disable Liquid Glass (iOS 26. 0+)
- Ignore Liquid Glass App Build Check (iOS 26.0+)
- Key Flick keyboard (iOS 26.0-)
- Build Version in Status Bar
- Force Right to Left
- Show Hidden Icons
- Force Metal HUD Debug
- iMessage/IDS/VC Diagnostics
- App Store Debug Gesture
- Notes Debug Mode
- Show Touches With Debug Info
- Hide Respring Icon
- Play Sound on Paste
- Show Notifications for System Pastes

#### Disable Daemons
| Daemon | Effect |
|--------|--------|
| OTAd | Prevents OTA updates (RECOMMENDED) |
| UsageTrackingAgent | Stops usage tracking |
| Game Center | Disables Game Center |
| Screen Time Agent | Disables Screen Time |
| Logs/Dumps/Crash Reports | Reduces logging |
| ATWAKEUP | Disables wake scheduling |
| Tipsd | Disables Tips app notifications |
| VPN | Disables VPN daemon |
| Chinese WLAN | Disables WLAN service |
| HealthKit | Disables Health tracking |
| AirPrint | Disables printing |
| Assistive Touch | Disables accessibility feature |
| iCloud | Disables iCloud sync |
| Personal Hotspot | Disables tethering |
| PassBook | Disables Wallet |
| Spotlight | Disables search indexing |
| Voice Control | Disables voice control |

#### Risky Options (Hidden by Default)
> [! CAUTION]
> Enable "Show Risky Tweaks" in Settings to access these.  Use at your own risk! 

- Disable thermalmonitord (can cause overheating!)
- **Custom Resolution** (NEW - supports all devices!)

---

### iOS 17.0 - 18.1. 1 (SparseRestore)

> [!WARNING]
> **Find My iPhone MUST be disabled for these tweaks! **

| Feature | Description |
|---------|-------------|
| Dynamic Island | Enable on any device |
| iPhone X Gestures | Enable on iPhone SEs |
| Device Model Name | Change Settings app display |
| Boot Chime | Enable startup sound |
| Charge Limit | Enable 80% charge limit |
| Tap to Wake | Enable on unsupported devices |
| Collision SOS | Show in Settings |
| Stage Manager | Enable multitasking |
| Wallpaper Parallax | Disable motion effect |
| Region Restrictions | Disable shutter sound, etc. |
| Apple Pencil Tab | Show in Settings |
| Action Button Tab | Show in Settings |
| Internal Storage Info | Show in Settings (risky) |
| EU Enabler | iOS 17.6 and below |

---

### iOS 18.0 - 18. 0.1

- Feature Flags (lock screen clock animation, page duplication)
- Disable iOS 18 Photos UI (betas only)

---

### iOS 18.0 - 18. 1.1

- iPhone 16 Camera Button settings page
- Always On Display (any device)
- AOD Vibrancy

---

### iOS 18.1 - 18.1.1

- AI Enabler (Apple Intelligence on unsupported devices)
- Device Spoofing

---

## 📊 Exploit Compatibility Matrix

| iOS Version | Exploit Method | Find My iPhone | Skip Setup | MobileGestalt | Custom Resolution |
|-------------|----------------|----------------|------------|---------------|-------------------|
| 17. 0 - 18.1.1 | SparseRestore | ❌ **Must Disable** | ✅ Works | ✅ Full support | ✅ Supported |
| 18.2 - 26.1 | BookRestore | ✅ Can Stay ON | ❌ Doesn't work | ✅ Limited | ✅ Supported |
| 26. 2+ | ❌ Patched | N/A | N/A | ❌ Not supported | ❌ Not supported |

### Quick Reference: When to Disable Find My iPhone

| Situation | Disable FMI?  |
|-----------|--------------|
| iOS 17.0 - 18.1.1 (any tweak) | ✅ **YES, always** |
| iOS 18.2+ with Daemons only | ❌ No |
| iOS 18.2+ with Status Bar only | ❌ No |
| iOS 18. 2+ with MobileGestalt tweaks | ❌ No |
| iOS 18.2+ with PosterBoard/Tendies | ❌ No |

---

## 🎚️ NEW: Custom Resolution Feature

This fork includes a comprehensive custom resolution feature for ALL iPhones and iPads!

### Supported Devices (80+ models)

<details>
<summary>📱 All Supported iPhones</summary>

| Device | Model ID | Native Resolution |
|--------|----------|-------------------|
| iPhone SE (1st gen) | iPhone8,4 | 640 x 1136 |
| iPhone SE (2nd gen) | iPhone12,8 | 750 x 1334 |
| iPhone SE (3rd gen) | iPhone14,6 | 750 x 1334 |
| iPhone 6/6s/7/8 | Various | 750 x 1334 |
| iPhone 6/6s/7/8 Plus | Various | 1242 x 2208 |
| iPhone X | iPhone10,3/6 | 1125 x 2436 |
| iPhone XS | iPhone11,2 | 1125 x 2436 |
| iPhone XS Max | iPhone11,4/6 | 1242 x 2688 |
| iPhone XR | iPhone11,8 | 828 x 1792 |
| iPhone 11 | iPhone12,1 | 828 x 1792 |
| iPhone 11 Pro | iPhone12,3 | 1125 x 2436 |
| iPhone 11 Pro Max | iPhone12,5 | 1242 x 2688 |
| iPhone 12 mini | iPhone13,1 | 1080 x 2340 |
| iPhone 12/12 Pro | iPhone13,2/3 | 1170 x 2532 |
| iPhone 12 Pro Max | iPhone13,4 | 1284 x 2778 |
| iPhone 13 mini | iPhone14,4 | 1080 x 2340 |
| iPhone 13/13 Pro | iPhone14,5/2 | 1170 x 2532 |
| iPhone 13 Pro Max | iPhone14,3 | 1284 x 2778 |
| iPhone 14 | iPhone14,7 | 1170 x 2532 |
| iPhone 14 Plus | iPhone14,8 | 1284 x 2778 |
| iPhone 14 Pro | iPhone15,2 | 1179 x 2556 |
| iPhone 14 Pro Max | iPhone15,3 | 1290 x 2796 |
| iPhone 15 | iPhone15,4 | 1179 x 2556 |
| iPhone 15 Plus | iPhone15,5 | 1290 x 2796 |
| iPhone 15 Pro | iPhone16,1 | 1179 x 2556 |
| iPhone 15 Pro Max | iPhone16,2 | 1290 x 2796 |
| iPhone 16 | iPhone17,3 | 1179 x 2556 |
| iPhone 16 Plus | iPhone17,4 | 1290 x 2796 |
| iPhone 16 Pro | iPhone17,1 | 1206 x 2622 |
| **iPhone 16 Pro Max** | **iPhone17,2** | **1320 x 2868** |

</details>

<details>
<summary>📱 All Supported iPads</summary>

| Device | Model ID | Native Resolution |
|--------|----------|-------------------|
| iPad mini 4 | iPad5,1/2 | 1536 x 2048 |
| iPad mini 5 | iPad11,1/2 | 1536 x 2048 |
| iPad mini 6 | iPad14,1/2 | 1488 x 2266 |
| iPad mini 7 (A17 Pro) | iPad16,1/2 | 1488 x 2266 |
| iPad 5th gen | iPad6,11/12 | 1536 x 2048 |
| iPad 6th gen | iPad7,5/6 | 1536 x 2048 |
| iPad 7th gen | iPad7,11/12 | 1620 x 2160 |
| iPad 8th gen | iPad11,6/7 | 1620 x 2160 |
| iPad 9th gen | iPad12,1/2 | 1620 x 2160 |
| iPad 10th gen | iPad13,18/19 | 1640 x 2360 |
| iPad Air 2 | iPad5,3/4 | 1536 x 2048 |
| iPad Air 3 | iPad11,3/4 | 1668 x 2224 |
| iPad Air 4 | iPad13,1/2 | 1640 x 2360 |
| iPad Air 5 (M1) | iPad13,16/17 | 1640 x 2360 |
| iPad Air 11-inch (M2) | iPad14,8/9 | 1640 x 2360 |
| iPad Air 13-inch (M2) | iPad14,10/11 | 2048 x 2732 |
| iPad Pro 9.7" | iPad6,3/4 | 1536 x 2048 |
| iPad Pro 10.5" | iPad7,3/4 | 1668 x 2224 |
| iPad Pro 11" (1st) | iPad8,1-4 | 1668 x 2388 |
| iPad Pro 11" (2nd) | iPad8,9/10 | 1668 x 2388 |
| iPad Pro 11" (3rd, M1) | iPad13,4/5 | 1668 x 2388 |
| iPad Pro 11" (4th, M2) | iPad14,3/4 | 1668 x 2388 |
| iPad Pro 11" (5th, M4) | iPad16,3/4 | 1668 x 2420 |
| iPad Pro 12.9" (1st) | iPad6,7/8 | 2048 x 2732 |
| iPad Pro 12. 9" (2nd) | iPad7,1/2 | 2048 x 2732 |
| iPad Pro 12. 9" (3rd) | iPad8,5-8 | 2048 x 2732 |
| iPad Pro 12.9" (4th) | iPad8,11/12 | 2048 x 2732 |
| iPad Pro 12.9" (5th, M1) | iPad13,8/9 | 2048 x 2732 |
| iPad Pro 12.9" (6th, M2) | iPad14,5/6 | 2048 x 2732 |
| **iPad Pro 13" (M4)** | **iPad16,5/6** | **2064 x 2752** |

</details>

### Resolution Multiplier Options

| Option | Risk Level | Description |
|--------|------------|-------------|
| 📱 Native (1. 0x) | ✅ Safe | Reverts to original resolution |
| 🔽 0.75x | ✅ Safe | Lower resolution, better performance |
| 🔽 0. 5x | ✅ Safe | Lowest resolution |
| 🔼 1.25x | ⚠️ Low risk | Slightly higher resolution |
| 🔼 1.5x | ⚠️ Medium risk | 50% more pixels |
| ⚠️ 1.75x | 🔴 High risk | May cause issues |
| ⚠️ 2.0x | 🔴 Very high risk | Double resolution |
| ⚠️ 2. 5x | 🔴 Dangerous | Likely to fail |
| ⚠️ 3. 0x | 🔴 Extreme | Almost certainly broken |
| ✏️ Custom | ⚠️ Varies | Enter any resolution |

### Example: iPhone 16 Pro Max Resolutions

| Multiplier | Width x Height |
|------------|----------------|
| 0.5x | 660 x 1434 |
| 0.75x | 990 x 2151 |
| Native | 1320 x 2868 |
| 1.25x | 1650 x 3585 |
| 1.5x | 1980 x 4302 |
| 2.0x | 2640 x 5736 |

> [!CAUTION]
> **Resolutions above 1.5x will likely cause display issues or boot loops! **
> Always have a backup ready and know how to DFU restore before testing high resolutions. 

---

## 🛠️ Requirements

### Windows
- [Apple Devices (Microsoft Store)](https://apps. microsoft.com/detail/9np83lwlpz9k) **OR**
- [iTunes (Apple website)](https://support. apple.com/en-us/106372)

### macOS
- No additional requirements (built-in drivers)
- **Recommended:** Python 3.11 (not 3.13)

### Linux
- [usbmuxd](https://github.com/libimobiledevice/usbmuxd)
- [libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)

### Python Dependencies
- Python 3.8 or newer (3.11 recommended)
- [pymobiledevice3](https://github. com/doronz88/pymobiledevice3)
- [PySide6](https://doc.qt.io/qtforpython-6/)

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/RobyRew/Nugget.git
cd Nugget
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# macOS/Linux
python3 -m venv . env
source .env/bin/activate

# Windows
python -m venv .env
. env\Scripts\activate. bat
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Run Nugget
```bash
python main_app.py
```

> [!NOTE]
> On macOS/Linux, you may need to run with `sudo` for BookRestore tweaks:
> ```bash
> sudo python main_app.py
> ```

---

## 📱 Getting Your MobileGestalt File

**Required for:** Dynamic Island, iPadOS mode, AirDrop tweaks, device spoofing, and other MobileGestalt tweaks. 

1. Install the [Shortcuts](https://apps.apple.com/us/app/shortcuts/id915249334) app
2.  Download this shortcut: [Save MobileGestalt](https://www.icloud.com/shortcuts/66bd3c822a0145b98d46cd1c9077e6e5)
3. Run the shortcut and save the file
4. Transfer the file to your computer
5. Load it in Nugget when prompted

---

## ⚙️ Settings Explained

| Setting | Description | Recommended |
|---------|-------------|-------------|
| **Skip Setup** | Prevents Setup Assistant after tweaks | ✅ ON (but won't work with BookRestore) |
| **Auto Reboot** | Automatically reboot after applying | ✅ ON |
| **Apply Over WiFi** | Apply without USB cable | ❌ OFF (less reliable) |
| **Restore TrustStore** | Restore SSL certificates | ❌ OFF (unless needed) |
| **Supervision** | Make device appear MDM supervised | ❌ OFF |
| **Show Risky Tweaks** | Show dangerous options (incl. Resolution) | ⚠️ Only if you know what you're doing |
| **BookRestore Transfer Mode** | Method for iOS 18.2+ | Try different modes if failing |

---

## 🔧 Troubleshooting

### "Timed out waiting for download" (iOS 18.2+)

This is a BookRestore Stage 2 failure. Try:

1. **Change Transfer Mode** in Settings (try modes 0, 1, 2)
2. **Reset Books app:** Settings → Apps → Books → Delete App → Reinstall
3. **Open Books app** before applying, download a free book sample
4. **Apply fewer tweaks** at once (1-2 max)
5. **Restart both** iPhone and computer
6. **Try different USB cable/port**
7. **Disable VPN** on both devices

### "Developer Mode Required"

1. Settings → Privacy & Security → Developer Mode → ON
2.  Restart iPhone when prompted
3.  Confirm Developer Mode after restart

### "Find My must be disabled"

This only appears for **SparseRestore** (iOS 17.0-18.1. 1):
1. Settings → [Your Name] → Find My → Find My iPhone → OFF
2. Apply tweaks
3.  Turn Find My back ON after

> [!NOTE]
> **BookRestore (iOS 18.2+) does NOT require Find My to be disabled! **

### Setup Assistant Appeared After Tweaks

This happens because **Skip Setup doesn't work with BookRestore**. Your data is NOT lost:
- If restoring from iCloud, wait for it to complete
- Your iOS version will remain the same
- Tweaks may not have applied — try again after restore

### "ConnectionAbortedError"

1. Refresh device list in Nugget
2.  Reconnect USB cable
3. Trust computer on iPhone again
4. Try a different USB port

### Black Screen After Resolution Change

1. Wait 30 seconds — it may recover
2. Force restart: Volume Up → Volume Down → Hold Power
3. If stuck, DFU restore is required
4. **Always test lower resolutions first! **

---

## 📁 File Structure

```
Nugget/
├── main_app.py              # Entry point
├── requirements.txt         # Python dependencies
├── devicemanagement/        # Device communication
│   ├── device_manager.py    # Main device logic
│   ├── constants.py         # Device definitions
│   └── data_singleton.py    # Shared data
├── restore/                 # Exploit implementations
│   ├── restore. py           # SparseRestore
│   ├── bookrestore.py       # BookRestore
│   └── backup. py            # Backup handling
├── tweaks/                  # Tweak implementations
│   ├── tweaks.py            # Tweak registry
│   ├── tweak_classes.py     # Tweak classes (incl. RdarFixTweak)
│   ├── posterboard/         # Wallpaper tweaks
│   └── status_bar/          # Status bar tweaks
├── gui/                     # User interface
│   ├── main_window.py       # Main window
│   └── pages/               # UI pages
├── translations/            # Language files
└── files/                   # Static resources
```

---

## 📝 Creating Custom Wallpapers (Tendies)

### Tendies File Formats

**1. Container Format**
```
my_wallpaper. tendies/
└── container/
    └── [exact PosterBoard structure]
```
- Restores directly to app container
- UUIDs are NOT randomized

**2. Descriptor Format (Recommended)**
```
my_wallpaper. tendies/
└── descriptor/
    └── [descriptor structure]
```
- Restores to descriptors folder
- UUIDs are randomized (safer)
- More future-proof

### Descriptor Extensions (v7. 0+)

| Folder Name Contains | Target Extension |
|---------------------|------------------|
| (nothing) | Collections (`com.apple.WallpaperKit.CollectionsPoster`) |
| "video" or "photos" | Suggested Photos (`com.apple.PhotosUIPrivate.PhotosPosterProvider`) |
| "mercury" | Mercury Poster (`com.apple.MercuryPoster`) |

---

## 📝 Creating Templates (Batter Files)

### Basic Structure
```
my_template.batter/
├── config.json
└── Container/
    └── [files to restore]
```

### config.json Format
```json
{
  "title": "My Template",
  "author": "Your Name",
  "description": "What this template does",
  "format_version": "2",
  "domain": "AppDomain-com.apple.PosterBoard",
  "min_version": "17.0",
  "max_version": "26.1",
  "options": []
}
```

### Option Types

| Type | Purpose |
|------|---------|
| `replace` | Let user replace files (images, etc.) |
| `set` | Let user set values (sliders, toggles, colors) |
| `remove` | Let user optionally remove files/elements |
| `picker` | Let user choose between options |
| `bundle_id` | Let user change target app |

See [documentation. md](documentation.md) for full option format details.

---

## 🔒 Technical Details

### SparseRestore (iOS 17.0-18.1. 1)
- Uses iOS backup system vulnerability
- Writes to files outside intended restore location
- **Requires Find My iPhone disabled**
- Skip Setup files CAN be written
- More reliable but patched in iOS 18.2

### BookRestore (iOS 18.2-26.1)
- Uses Books app vulnerability
- Exploits `bookassetd` service
- **Does NOT require Find My disabled**
- Skip Setup files CANNOT be written (by design)
- Stage 1: Prepare files on computer
- Stage 2: Books app triggers exploit
- Less reliable, timeout issues possible

---

## 👥 Credits

- **Translations:** Crowdsourced via [POEditor](https://poeditor.com/join/project/UTqpVSE2UD)
- **SparseRestore/TrollRestore:** [JJTech](https://github. com/JJTech0130)
- **BookRestore:** [Duy Tran](https://github.com/khanhduytran0) & [Huy Nguyen](https://x.com/Little_34306)
- **PosterBoard:** [PosterRestore Discord](https://discord. gg/gWtzTVhMvh)
  - dootskyre, Middo, dulark, forcequitOS, pingubow
  - [SerStars](https://x.com/SerStars_lol) for the wallpapers website
  - [Snoolie](https://github.com/0xilis/python-aar-stuff) for AAR handling
- **Features:** [disfordottie](https://x.com/disfordottie), [Mikasa-san](https://github. com/Mikasa-san), [sneakyf1shy](https://github.com/f1shy-dev), [lrdsnow](https://github. com/Lrdsnow)
- **Libraries:** [pymobiledevice3](https://github.com/doronz88/pymobiledevice3), [PySide6](https://doc.qt.io/qtforpython-6/)
- **Custom Resolution Feature:** [RobyRew](https://github.com/RobyRew)

---

## 📖 Read More

For technical details about how the exploits work:
- [SparseRestore Writeup by leminlimez](https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28)

---

## 📜 License

See [LICENSE](LICENSE) file for details.

[NuggetLogo]: https://raw.githubusercontent.com/leminlimez/Nugget/refs/heads/main/credits/small_nugget. png
