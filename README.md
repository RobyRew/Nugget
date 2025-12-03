![Nugget Logo](https://raw.githubusercontent.com/leminlimez/Nugget/refs/heads/main/credits/small_nugget.png)

# Nugget

[![License](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-5.2.0-green.svg)](version.txt)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

A Python-based desktop application for iOS device customization using the PySide6/Qt GUI framework. Nugget enables users to apply various customizations to iOS devices by utilizing USB-based communication through the `pymobiledevice3` library.

> [!CAUTION]
> **ALWAYS backup your data before using Nugget.** This tool modifies system files and may cause unforeseen issues. We are not responsible for any damage to your device.

---

## 📱 iOS Version Compatibility

Nugget uses different exploit methods depending on your iOS version:

| iOS Version | Method | MobileGestalt Support | Find My Requirement | Skip Setup | Status |
|------------|--------|----------------------|-------------------|-----------|--------|
| **17.0 - 17.7.0** | SparseRestore | ✅ Full | ❌ Must Disable | ✅ Works | Supported |
| **17.7.1 - 17.x** | ❌ Patched | ❌ None | N/A | N/A | Not Supported |
| **18.0 - 18.0.1** | SparseRestore | ✅ Full | ❌ Must Disable | ✅ Works | Supported |
| **18.1 Beta (specific)** | SparseRestore | ✅ Full | ❌ Must Disable | ✅ Works | Supported* |
| **18.1.x - 18.1.x** | Partial SparseRestore | ⚠️ Domains Only | ❌ Must Disable | ✅ Works | Partial |
| **18.2 Beta (specific)** | Partial SparseRestore | ⚠️ Domains Only | ❌ Must Disable | ✅ Works | Partial* |
| **18.2+ to 26.1** | BookRestore | ✅ Limited | ✅ Can Stay On | ❌ Doesn't Work | Supported |
| **26.2 Beta 2+** | ❌ Fully Patched | ❌ None | N/A | N/A | Not Supported |

\* **Specific supported iOS 18.1 beta builds:** 22B5007p, 22B5023e, 22B5034e, 22B5045g  
\* **Specific supported iOS 18.2 beta builds:** 22C5109p, 22C5125e  
\* **iOS 26.1 build 23C5027f** is also supported with BookRestore

---

## 🚀 Key Features

### Available on All Supported iOS Versions

#### 📺 PosterBoard Wallpapers
- Import animated wallpapers (`.tendies` files)
- Convert videos to live wallpapers
- Community wallpapers available
- Create custom templates (`.batter` files)

#### 📊 Status Bar Customization
- Custom carrier text (primary and secondary)
- WiFi/Cellular signal bars (0-4)
- Battery percentage display
- Custom time and date text
- Breadcrumb text modification
- Numeric signal strength (dBm)
- Hide individual status bar icons

#### ⚙️ Springboard Options
- Lock screen footnote
- Custom auto-lock time
- Disable lock after respring/crash
- Disable screen dimming while charging
- Hide low battery alerts
- Hide AC power indicator on lock screen
- Show supervision text
- AirDrop time limit removal
- Never show breadcrumb
- Disable floating tab bar (iPad)

#### 🔧 Internal Options
- Build number in status bar
- Force RTL/LTR text direction
- Metal HUD debug
- iMessage/IDS/VC diagnostics
- Touch visualization with debug info
- App Store debug gestures
- Notes debug mode
- Hide Apple logo on launch
- System paste notifications

#### 🛑 Daemon Management
Disable various system daemons including:
- OTA updates (OTAd)
- Usage tracking
- Game Center
- Screen Time
- Crash reporting
- Tips notifications
- VPN services
- iCloud sync
- Spotlight indexing
- And many more...

#### ⚠️ Risky Options
- **Custom Resolution** - Change device display resolution (80+ devices supported)
- OTA update disable
- RDAR fixes for specific iPhone models

### MobileGestalt Tweaks (Requires `.mga` file)

Available on iOS 17.0 - 18.0.1 and 18.1 betas (Full SparseRestore):

- **Dynamic Island** - Simulate Dynamic Island on any device (multiple sizes)
- **Model Name Spoofing** - Change device name in Settings
- **Boot Chime** - Enable startup sound
- **Charge Limit** - Enable 80% charge limit
- **Collision SOS** - Enable in Settings
- **Tap to Wake** - Enable on unsupported devices
- **Camera Button** - iPhone 16-style camera button settings
- **Parallax** - Disable wallpaper motion effect
- **Stage Manager** - Enable multitasking
- **iPadOS Mode** - Enable iPad features on iPhone
- **Shutter Sound Region** - Change camera shutter behavior
- **Apple Pencil Support** - Show settings tab
- **Action Button** - Show settings tab
- **Internal Storage Mode** - Show internal storage info
- **Always On Display** - Enable on any device (iOS 18.0-18.1.1)
- **AOD Vibrancy** - Customize AOD appearance (iOS 18.0-18.1.1)
- **Device Spoofing** - Spoof hardware/CPU for Apple Intelligence (iOS 18.1+)

### Eligibility Tweaks

- **EU Enabler** - Enable sideloading and alternative app stores
- **Apple Intelligence** - Enable on unsupported devices (iOS 18.1+)
- **Region Code Customization**

### Feature Flags (iOS < 18.1)

- Clock animation
- Lock screen effects
- Photos UI (Lemonade)
- AI features

---

## 🔧 How It Works

### SparseRestore Method (iOS 17.0 - 18.1.x)

SparseRestore is the primary exploit method for earlier iOS versions:

1. **Backup Manipulation**: Creates a fake iOS backup with specially crafted metadata
2. **Path Traversal**: Uses `SysContainerDomain-../../../../../../../..` to escape the intended restore directory
3. **File Writing**: Writes files to arbitrary locations on the device during the restore process
4. **Reboot**: Automatically reboots the device to apply changes

**Requirements:**
- Find My iPhone must be disabled
- Device must trust the computer
- Not supported on MDM-managed devices with encrypted backups

**Advantages:**
- More reliable
- Supports Skip Setup
- Full MobileGestalt support

**Limitations:**
- Requires Find My to be disabled
- Patched on iOS 18.2+

### BookRestore Method (iOS 18.2 - 26.1)

BookRestore is a fallback exploit for newer iOS versions where SparseRestore is patched:

1. **Tunnel Creation**: Uses `pymobiledevice3` to create a secure tunnel to the device
2. **HTTP Server**: Hosts a local server to serve files to the device
3. **Books Exploit**: Manipulates the Books app download mechanism
4. **Database Modification**: Modifies `downloads.28.sqlitedb` and `BLDatabaseManager.sqlite`
5. **Respring**: Performs a respring instead of full reboot

**Requirements:**
- Developer Mode enabled on iOS 18.2+
- Device must trust the computer

**Advantages:**
- Find My can remain enabled
- Works on newer iOS versions

**Limitations:**
- Skip Setup doesn't work
- Less reliable (timeout issues possible)
- Limited MobileGestalt support
- Setup Assistant may appear after applying tweaks

---

## 💾 File Formats

### .tendies Files (PosterBoard Wallpapers)

Two formats are supported:

**Container Format:**
```
wallpaper.tendies/
└── container/
    └── [PosterBoard app structure]
```
- Restores directly to app container
- UUIDs are NOT randomized

**Descriptor Format (Recommended):**
```
wallpaper.tendies/
└── descriptor/
    └── [descriptor structure]
```
- Restores to descriptors folder with randomized UUIDs
- More future-proof
- Extension determined by folder name:
  - Default: Collections (`com.apple.WallpaperKit.CollectionsPoster`)
  - "video" or "photos": Suggested Photos (`com.apple.PhotosUIPrivate.PhotosPosterProvider`)
  - "mercury": Mercury Poster (`com.apple.MercuryPoster`)

### .batter Files (Templates)

Templates allow user-customizable options:

```
template.batter/
├── config.json
└── Container/
    └── [files to restore]
```

**config.json structure:**
```json
{
  "title": "Template Name",
  "author": "Your Name",
  "description": "Description",
  "format_version": "2",
  "domain": "AppDomain-com.apple.PosterBoard",
  "min_version": "17.0",
  "max_version": "26.1",
  "options": [...]
}
```

**Supported option types:**
- `replace` - Replace files (images, etc.)
- `set` - Set values (sliders, toggles, colors)
- `remove` - Optionally remove files/elements
- `picker` - Choose between options
- `bundle_id` - Change target app

Files can use `nuggetId` identifiers in `.caml` files for targeted modifications.

See [documentation.md](documentation.md) for complete format specifications.

---

## 📋 Requirements

### Platform-Specific Requirements

**Windows:**
- [Apple Devices app (Microsoft Store)](https://apps.microsoft.com/detail/9np83lwlpz9k) **OR**
- [iTunes (Apple)](https://support.apple.com/en-us/106372)

**macOS:**
- Native support (no additional drivers needed)

**Linux:**
- `usbmuxd`
- `libimobiledevice`

### Python Dependencies

- **Python 3.8+** (Python 3.11 recommended)
- `pymobiledevice3` - iOS device communication
- `PySide6-Essentials` (Windows/macOS) or `PySide6` (Linux) - GUI framework
- `PyInstaller` - Application building
- `ffmpeg` and `ffmpeg-python` - Video processing
- `opencv-python` - Image processing
- `pyperclip` - Clipboard operations
- `pyuac` (Windows only) - UAC elevation

See [requirements.txt](requirements.txt) for complete dependency list.

### Device Requirements

- iOS device running a supported version
- USB cable connection (wireless mode less reliable)
- Device must trust the computer
- Find My must be disabled for SparseRestore (iOS 17.0-18.1.x)
- Developer Mode required for BookRestore on iOS 18.2+
- MobileGestalt cache file (`.mga`) required for certain tweaks

---

## 🚀 Installation

### Method 1: Run from Source

```bash
# Clone the repository
git clone https://github.com/RobyRew/Nugget.git
cd Nugget

# Create virtual environment (recommended)
python3 -m venv .env
source .env/bin/activate  # On Windows: .env\Scripts\activate.bat

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run Nugget
python main_app.py
```

> [!NOTE]
> On macOS/Linux, you may need to run with `sudo` for BookRestore:
> ```bash
> sudo python main_app.py
> ```

### Method 2: Pre-built Binaries

Check the [Releases](https://github.com/RobyRew/Nugget/releases) page for pre-built executables for your platform.

---

## 📖 Usage Guide

### Getting Your MobileGestalt File

Required for Dynamic Island, device spoofing, and other MobileGestalt tweaks:

1. Install [Shortcuts](https://apps.apple.com/us/app/shortcuts/id915249334) on your iOS device
2. Download the [Save MobileGestalt shortcut](https://www.icloud.com/shortcuts/66bd3c822a0145b98d46cd1c9077e6e5)
3. Run the shortcut and save the `.mga` file
4. Transfer the file to your computer
5. Load it in Nugget when prompted

### Applying Tweaks

1. Connect your iOS device via USB
2. Trust the computer on your device
3. Open Nugget and select your device
4. **For SparseRestore (iOS 17.0-18.1.x):** Disable Find My iPhone
5. **For BookRestore (iOS 18.2+):** Enable Developer Mode
6. Select desired tweaks
7. Click "Apply" and wait for completion
8. Device will reboot (SparseRestore) or respring (BookRestore)

---

## 🔧 Troubleshooting

### "Developer Mode Required" (iOS 18.2+)
1. Go to Settings → Privacy & Security → Developer Mode
2. Enable Developer Mode
3. Restart your device when prompted
4. Confirm activation after restart

### "Find My must be disabled" (iOS 17.0-18.1.x)
1. Go to Settings → [Your Name] → Find My → Find My iPhone
2. Toggle OFF
3. Apply tweaks
4. You can re-enable Find My after completion

### "Timed out waiting for download" (BookRestore)
Try these solutions:
1. Change Transfer Mode in Settings (try modes 0, 1, or 2)
2. Reset Books app: Settings → Apps → Books → Delete App → Reinstall
3. Open Books app before applying and download a free sample
4. Apply fewer tweaks at once (1-2 maximum)
5. Restart both device and computer
6. Try a different USB cable or port
7. Disable VPN on both devices

### Setup Assistant Appeared After Applying Tweaks
This is expected with BookRestore - Skip Setup does not work on iOS 18.2+. Your data is not lost. Wait for any restore process to complete. Your iOS version remains unchanged.

### Custom Resolution Black Screen
1. Wait 30 seconds for potential recovery
2. Force restart: Volume Up → Volume Down → Hold Power button
3. If device doesn't boot, use DFU restore
4. **Always test lower resolutions first (0.75x or 0.5x)**

### Connection Issues
1. Refresh device list in Nugget
2. Reconnect USB cable
3. Trust computer again on device
4. Try a different USB port
5. Restart both device and Nugget

---

## ⚠️ Important Notes

- **MDM-managed devices** with encrypted backups are not supported
- **iOS 26.2 beta 2+** is permanently patched and will never be supported
- **Backup your data** before applying any tweaks
- **Custom resolutions above 1.5x** are dangerous and may cause boot loops
- **Skip Setup does not work** with BookRestore (iOS 18.2+)
- Some tweaks may conflict with each other - apply cautiously

---

## 👥 Credits

**Original Author:**
- [LeminLimez](https://github.com/leminlimez) - Original Nugget creator

**Fork Author:**
- [RobyRew](https://github.com/RobyRew) - Custom resolution feature and enhancements

**Exploit Methods:**
- [JJTech0130](https://github.com/JJTech0130) - SparseRestore/TrollRestore
- [Duy Tran (khanhduytran0)](https://github.com/khanhduytran0) - BookRestore
- [Huy Nguyen (Little_34306)](https://x.com/Little_34306) - BookRestore

**PosterBoard & Wallpapers:**
- dootskyre, Middo, dulark, forcequitOS, pingubow - PosterBoard development
- [SerStars](https://x.com/SerStars_lol) - Wallpaper website
- [Snoolie (0xilis)](https://github.com/0xilis/python-aar-stuff) - AAR handling

**Additional Features:**
- [disfordottie](https://x.com/disfordottie)
- [Mikasa-san](https://github.com/Mikasa-san)
- [sneakyf1shy (f1shy-dev)](https://github.com/f1shy-dev)
- [lrdsnow](https://github.com/Lrdsnow)

**Libraries:**
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) - iOS device communication
- [PySide6](https://doc.qt.io/qtforpython-6/) - Qt GUI framework

**Translations:**
- Community contributors via [POEditor](https://poeditor.com/join/project/UTqpVSE2UD)

**Learn More:**
- [SparseRestore Technical Writeup](https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28) by LeminLimez

---

## 📜 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **Repository:** [https://github.com/RobyRew/Nugget](https://github.com/RobyRew/Nugget)
- **Original Repository:** [https://github.com/leminlimez/Nugget](https://github.com/leminlimez/Nugget)
- **Issues:** [https://github.com/RobyRew/Nugget/issues](https://github.com/RobyRew/Nugget/issues)
- **Releases:** [https://github.com/RobyRew/Nugget/releases](https://github.com/RobyRew/Nugget/releases)
