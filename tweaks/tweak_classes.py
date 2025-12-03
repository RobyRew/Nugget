import re

from enum import Enum
from PySide6.QtCore import QCoreApplication

from devicemanagement.constants import Version
from .basic_plist_locations import FileLocation

class Tweak:
    def __init__(self,
            self,
            key: str,
            value: any = 1,
            owner: int = 501, group: int = 501
        ):
        self.key = key
        self.value = value
        self.owner = owner
        self.group = group
        self.enabled = False

    def set_enabled(self, value: bool):
        self.enabled = value
    def toggle_enabled(self):
        self.enabled = not self.enabled
    def set_value(self, new_value: any, toggle_enabled: bool = True):
        self.value = new_value
        if toggle_enabled:
            self.enabled = True

    def apply_tweak(self):
        raise NotImplementedError
    
class NullifyFileTweak(Tweak):
    def __init__(self,
            self,
            file_location: FileLocation,
            owner: int = 501, group: int = 501
        ):
        super().__init__(key=None, value=None, owner=owner, group=group)
        self.file_location = file_location

    def apply_tweak(self, other_tweaks: dict):
        if self.enabled:
            other_tweaks[self.file_location] = b""
    
class BasicPlistTweak(Tweak):
    def __init__(self,
            self,
            file_location: FileLocation,
            key: str,
            value: any = True,
            owner: int = 501, group: int = 501,
            is_risky: bool = False
        ):
        super().__init__(key=key, value=value, owner=owner, group=group)
        self.file_location = file_location
        self.is_risky = is_risky

    def apply_tweak(self, other_tweaks: dict, risky_allowed: bool = False) -> dict:
        if not self.enabled or (self.is_risky and not risky_allowed):
            return other_tweaks
        if self.file_location in other_tweaks:
            other_tweaks[self.file_location][self.key] = self.value
        else:
            other_tweaks[self.file_location] = {self.key: self.value}
        return other_tweaks
    
class AdvancedPlistTweak(BasicPlistTweak):
    def __init__(self,
        self,
        file_location: FileLocation,
        keyValues: dict,
        owner: int = 501, group: int = 501,
        is_risky: bool = False
    ):
        super().__init__(file_location=file_location, key=None, value=keyValues, owner=owner, group=group, is_risky=is_risky)

    def set_multiple_values(self, keys: list[str], value: any):
        for key in keys:
            self.value[key] = value

    def apply_tweak(self, other_tweaks: dict, risky_allowed: bool = False) -> dict:
        if not self.enabled or (self.is_risky and not risky_allowed):
            return other_tweaks
        plist = {}
        for key in self.value:
            plist[key] = self.value[key]
        other_tweaks[self.file_location] = plist
        return other_tweaks
    
class RdarFixTweak(BasicPlistTweak):
    """
    Custom Resolution Tweak - Supports ALL iPhones and iPads
    Allows exponential resolution scaling and custom resolution input
    
    WARNING: Resolutions above 1.5x may cause display issues or boot loops!
    """
    
    # Native resolutions for ALL iPhone models (height, width)
    NATIVE_RESOLUTIONS = {
        # ============== iPhones ==============
        # iPhone SE series
        "iPhone8,4": (1136, 640),       # iPhone SE 1st gen
        "iPhone12,8": (1334, 750),      # iPhone SE 2nd gen
        "iPhone14,6": (1334, 750),      # iPhone SE 3rd gen
        
        # iPhone 6/6S/7/8 series
        "iPhone7,2": (1334, 750),       # iPhone 6
        "iPhone8,1": (1334, 750),       # iPhone 6s
        "iPhone9,1": (1334, 750),       # iPhone 7
        "iPhone9,3": (1334, 750),       # iPhone 7
        "iPhone10,1": (1334, 750),      # iPhone 8
        "iPhone10,4": (1334, 750),      # iPhone 8
        
        # iPhone 6/6S/7/8 Plus series
        "iPhone7,1": (2208, 1242),      # iPhone 6 Plus
        "iPhone8,2": (2208, 1242),      # iPhone 6s Plus
        "iPhone9,2": (2208, 1242),      # iPhone 7 Plus
        "iPhone9,4": (2208, 1242),      # iPhone 7 Plus
        "iPhone10,2": (2208, 1242),     # iPhone 8 Plus
        "iPhone10,5": (2208, 1242),     # iPhone 8 Plus
        
        # iPhone X series
        "iPhone10,3": (2436, 1125),     # iPhone X
        "iPhone10,6": (2436, 1125),     # iPhone X
        "iPhone11,2": (2436, 1125),     # iPhone XS
        "iPhone11,4": (2688, 1242),     # iPhone XS Max
        "iPhone11,6": (2688, 1242),     # iPhone XS Max
        "iPhone11,8": (1792, 828),      # iPhone XR
        
        # iPhone 11 series
        "iPhone12,1": (1792, 828),      # iPhone 11
        "iPhone12,3": (2436, 1125),     # iPhone 11 Pro
        "iPhone12,5": (2688, 1242),     # iPhone 11 Pro Max
        
        # iPhone 12 series
        "iPhone13,1": (2340, 1080),     # iPhone 12 mini
        "iPhone13,2": (2532, 1170),     # iPhone 12
        "iPhone13,3": (2532, 1170),     # iPhone 12 Pro
        "iPhone13,4": (2778, 1284),     # iPhone 12 Pro Max
        
        # iPhone 13 series
        "iPhone14,4": (2340, 1080),     # iPhone 13 mini
        "iPhone14,5": (2532, 1170),     # iPhone 13
        "iPhone14,2": (2532, 1170),     # iPhone 13 Pro
        "iPhone14,3": (2778, 1284),     # iPhone 13 Pro Max
        
        # iPhone 14 series
        "iPhone14,7": (2532, 1170),     # iPhone 14
        "iPhone14,8": (2778, 1284),     # iPhone 14 Plus
        "iPhone15,2": (2556, 1179),     # iPhone 14 Pro
        "iPhone15,3": (2796, 1290),     # iPhone 14 Pro Max
        
        # iPhone 15 series
        "iPhone15,4": (2556, 1179),     # iPhone 15
        "iPhone15,5": (2796, 1290),     # iPhone 15 Plus
        "iPhone16,1": (2556, 1179),     # iPhone 15 Pro
        "iPhone16,2": (2796, 1290),     # iPhone 15 Pro Max
        
        # iPhone 16 series
        "iPhone17,3": (2556, 1179),     # iPhone 16
        "iPhone17,4": (2796, 1290),     # iPhone 16 Plus
        "iPhone17,1": (2622, 1206),     # iPhone 16 Pro
        "iPhone17,2": (2868, 1320),     # iPhone 16 Pro Max
        
        # iPhone 17 series (future)
        "iPhone17,5": (2868, 1320),     # iPhone 17 (placeholder)
        "iPhone18,1": (2868, 1320),     # iPhone 17 Pro (placeholder)
        "iPhone18,2": (2868, 1320),     # iPhone 17 Pro Max (placeholder)
        "iPhone18,3": (2868, 1320),     # iPhone 17 (placeholder)
        
        # ============== iPads ==============
        # iPad mini series
        "iPad5,1": (2048, 1536),        # iPad mini 4 (WiFi)
        "iPad5,2": (2048, 1536),        # iPad mini 4 (Cellular)
        "iPad11,1": (2048, 1536),       # iPad mini 5th gen (WiFi)
        "iPad11,2": (2048, 1536),       # iPad mini 5th gen (Cellular)
        "iPad14,1": (2266, 1488),       # iPad mini 6th gen (WiFi)
        "iPad14,2": (2266, 1488),       # iPad mini 6th gen (Cellular)
        "iPad16,1": (2266, 1488),       # iPad mini 7th gen A17 Pro (WiFi)
        "iPad16,2": (2266, 1488),       # iPad mini 7th gen A17 Pro (Cellular)
        
        # iPad (standard) series
        "iPad6,11": (2048, 1536),       # iPad 5th gen (WiFi)
        "iPad6,12": (2048, 1536),       # iPad 5th gen (Cellular)
        "iPad7,5": (2048, 1536),        # iPad 6th gen (WiFi)
        "iPad7,6": (2048, 1536),        # iPad 6th gen (Cellular)
        "iPad7,11": (2160, 1620),       # iPad 7th gen (WiFi)
        "iPad7,12": (2160, 1620),       # iPad 7th gen (Cellular)
        "iPad11,6": (2160, 1620),       # iPad 8th gen (WiFi)
        "iPad11,7": (2160, 1620),       # iPad 8th gen (Cellular)
        "iPad12,1": (2160, 1620),       # iPad 9th gen (WiFi)
        "iPad12,2": (2160, 1620),       # iPad 9th gen (Cellular)
        "iPad13,18": (2360, 1640),      # iPad 10th gen (WiFi)
        "iPad13,19": (2360, 1640),      # iPad 10th gen (Cellular)
        
        # iPad Air series
        "iPad5,3": (2048, 1536),        # iPad Air 2 (WiFi)
        "iPad5,4": (2048, 1536),        # iPad Air 2 (Cellular)
        "iPad11,3": (2224, 1668),       # iPad Air 3rd gen (WiFi)
        "iPad11,4": (2224, 1668),       # iPad Air 3rd gen (Cellular)
        "iPad13,1": (2360, 1640),       # iPad Air 4th gen (WiFi)
        "iPad13,2": (2360, 1640),       # iPad Air 4th gen (Cellular)
        "iPad13,16": (2360, 1640),      # iPad Air 5th gen M1 (WiFi)
        "iPad13,17": (2360, 1640),      # iPad Air 5th gen M1 (Cellular)
        "iPad14,8": (2360, 1640),       # iPad Air 11-inch M2 (WiFi)
        "iPad14,9": (2360, 1640),       # iPad Air 11-inch M2 (Cellular)
        "iPad14,10": (2732, 2048),      # iPad Air 13-inch M2 (WiFi)
        "iPad14,11": (2732, 2048),      # iPad Air 13-inch M2 (Cellular)
        
        # iPad Pro 9.7-inch
        "iPad6,3": (2048, 1536),        # iPad Pro 9.7 (WiFi)
        "iPad6,4": (2048, 1536),        # iPad Pro 9.7 (Cellular)
        
        # iPad Pro 10.5-inch
        "iPad7,3": (2224, 1668),        # iPad Pro 10.5 (WiFi)
        "iPad7,4": (2224, 1668),        # iPad Pro 10.5 (Cellular)
        
        # iPad Pro 11-inch series
        "iPad8,1": (2388, 1668),        # iPad Pro 11 1st gen (WiFi)
        "iPad8,2": (2388, 1668),        # iPad Pro 11 1st gen (WiFi, 1TB)
        "iPad8,3": (2388, 1668),        # iPad Pro 11 1st gen (Cellular)
        "iPad8,4": (2388, 1668),        # iPad Pro 11 1st gen (Cellular, 1TB)
        "iPad8,9": (2388, 1668),        # iPad Pro 11 2nd gen (WiFi)
        "iPad8,10": (2388, 1668),       # iPad Pro 11 2nd gen (Cellular)
        "iPad13,4": (2388, 1668),       # iPad Pro 11 3rd gen M1 (WiFi)
        "iPad13,5": (2388, 1668),       # iPad Pro 11 3rd gen M1 (Cellular)
        "iPad14,3": (2388, 1668),       # iPad Pro 11 4th gen M2 (WiFi)
        "iPad14,4": (2388, 1668),       # iPad Pro 11 4th gen M2 (Cellular)
        "iPad16,3": (2420, 1668),       # iPad Pro 11 5th gen M4 (WiFi)
        "iPad16,4": (2420, 1668),       # iPad Pro 11 5th gen M4 (Cellular)
        
        # iPad Pro 12.9-inch series
        "iPad6,7": (2732, 2048),        # iPad Pro 12.9 1st gen (WiFi)
        "iPad6,8": (2732, 2048),        # iPad Pro 12.9 1st gen (Cellular)
        "iPad7,1": (2732, 2048),        # iPad Pro 12.9 2nd gen (WiFi)
        "iPad7,2": (2732, 2048),        # iPad Pro 12.9 2nd gen (Cellular)
        "iPad8,5": (2732, 2048),        # iPad Pro 12.9 3rd gen (WiFi)
        "iPad8,6": (2732, 2048),        # iPad Pro 12.9 3rd gen (WiFi, 1TB)
        "iPad8,7": (2732, 2048),        # iPad Pro 12.9 3rd gen (Cellular)
        "iPad8,8": (2732, 2048),        # iPad Pro 12.9 3rd gen (Cellular, 1TB)
        "iPad8,11": (2732, 2048),       # iPad Pro 12.9 4th gen (WiFi)
        "iPad8,12": (2732, 2048),       # iPad Pro 12.9 4th gen (Cellular)
        "iPad13,8": (2732, 2048),       # iPad Pro 12.9 5th gen M1 (WiFi)
        "iPad13,9": (2732, 2048),       # iPad Pro 12.9 5th gen M1 (Cellular)
        "iPad14,5": (2732, 2048),       # iPad Pro 12.9 6th gen M2 (WiFi)
        "iPad14,6": (2732, 2048),       # iPad Pro 12.9 6th gen M2 (Cellular)
        
        # iPad Pro 13-inch M4
        "iPad16,5": (2752, 2064),       # iPad Pro 13 M4 (WiFi)
        "iPad16,6": (2752, 2064),       # iPad Pro 13 M4 (Cellular)
    }
    
    # Resolution multipliers for dropdown (multiplier, display_name)
    RESOLUTION_MULTIPLIERS = [
        (1.0, "Native (1.0x)"),
        (0.75, "0.75x (Lower)"),
        (0.5, "0.5x (Lowest)"),
        (1.25, "1.25x"),
        (1.5, "1.5x"),
        (1.75, "1.75x (Risky)"),
        (2.0, "2.0x (Very Risky)"),
        (2.5, "2.5x (Dangerous)"),
        (3.0, "3.0x (Extreme)"),
        (0, "Custom..."),  # 0 means custom input
    ]

    def __init__(self):
        super().__init__(file_location=FileLocation.resolution, key=None)
        self.mode = 0  # 0 = not supported/disabled, 1 = supported
        self.di_type = -1  # -1 = revert, other = apply
        self.device_model = ""
        self.selected_multiplier = 0  # index in RESOLUTION_MULTIPLIERS
        self.custom_width = 0
        self.custom_height = 0
        self.native_width = 0
        self.native_height = 0

    def get_rdar_mode(self, model: str) -> int:
        """Determine if device is supported and get native resolution"""
        self.device_model = model
        if model in self.NATIVE_RESOLUTIONS:
            self.native_height, self.native_width = self.NATIVE_RESOLUTIONS[model]
            self.custom_height = self.native_height
            self.custom_width = self.native_width
            self.mode = 1  # Supported
        else:
            self.mode = 0  # Not in database, but we'll still allow it
            # Try to set a reasonable default for unknown devices
            if model.startswith("iPhone"):
                self.native_height, self.native_width = (2556, 1179)  # Default iPhone
            elif model.startswith("iPad"):
                self.native_height, self.native_width = (2388, 1668)  # Default iPad
            else:
                self.native_height, self.native_width = (1920, 1080)  # Generic default
            self.custom_height = self.native_height
            self.custom_width = self.native_width
            self.mode = 1  # Allow anyway
        return self.mode
        
    def get_rdar_title(self) -> str:
        """Get display title for the resolution tweak"""
        if self.mode == 0:
            return "hide"
        if self.di_type == -1 or self.selected_multiplier == 0:
            return QCoreApplication.tr("Revert Resolution")
        
        multiplier_name = self.RESOLUTION_MULTIPLIERS[self.selected_multiplier][1]
        return QCoreApplication.tr(f"Custom Resolution ({multiplier_name})")
    
    def set_di_type(self, type: int):
        """Set whether to apply or revert the tweak"""
        self.di_type = type

    def set_multiplier(self, index: int):
        """Set resolution multiplier from dropdown selection"""
        self.selected_multiplier = index
        if index < len(self.RESOLUTION_MULTIPLIERS) - 1 and index > 0:  # Not "Custom" and not "Native"
            multiplier = self.RESOLUTION_MULTIPLIERS[index][0]
            self.custom_height = int(self.native_height * multiplier)
            self.custom_width = int(self.native_width * multiplier)
            self.di_type = 1  # Enable
        elif index == 0:  # Native
            self.custom_height = self.native_height
            self.custom_width = self.native_width
            self.di_type = -1  # Revert to native
    
    def set_custom_resolution(self, width: int, height: int):
        """Set a fully custom resolution"""
        self.custom_width = width
        self.custom_height = height
        self.selected_multiplier = len(self.RESOLUTION_MULTIPLIERS) - 1  # Set to "Custom"
        self.di_type = 1  # Enable
    
    def get_calculated_resolution(self) -> tuple:
        """Returns (height, width) tuple of current resolution setting"""
        return (self.custom_height, self.custom_width)
    
    def get_native_resolution(self) -> tuple:
        """Returns (height, width) tuple of native resolution"""
        return (self.native_height, self.native_width)
    
    def get_device_name(self) -> str:
        """Get friendly device name from model identifier"""
        device_names = {
            # iPhones
            "iPhone8,4": "iPhone SE (1st gen)",
            "iPhone12,8": "iPhone SE (2nd gen)",
            "iPhone14,6": "iPhone SE (3rd gen)",
            "iPhone10,3": "iPhone X",
            "iPhone10,6": "iPhone X",
            "iPhone11,2": "iPhone XS",
            "iPhone11,4": "iPhone XS Max",
            "iPhone11,6": "iPhone XS Max",
            "iPhone11,8": "iPhone XR",
            "iPhone12,1": "iPhone 11",
            "iPhone12,3": "iPhone 11 Pro",
            "iPhone12,5": "iPhone 11 Pro Max",
            "iPhone13,1": "iPhone 12 mini",
            "iPhone13,2": "iPhone 12",
            "iPhone13,3": "iPhone 12 Pro",
            "iPhone13,4": "iPhone 12 Pro Max",
            "iPhone14,4": "iPhone 13 mini",
            "iPhone14,5": "iPhone 13",
            "iPhone14,2": "iPhone 13 Pro",
            "iPhone14,3": "iPhone 13 Pro Max",
            "iPhone14,7": "iPhone 14",
            "iPhone14,8": "iPhone 14 Plus",
            "iPhone15,2": "iPhone 14 Pro",
            "iPhone15,3": "iPhone 14 Pro Max",
            "iPhone15,4": "iPhone 15",
            "iPhone15,5": "iPhone 15 Plus",
            "iPhone16,1": "iPhone 15 Pro",
            "iPhone16,2": "iPhone 15 Pro Max",
            "iPhone17,3": "iPhone 16",
            "iPhone17,4": "iPhone 16 Plus",
            "iPhone17,1": "iPhone 16 Pro",
            "iPhone17,2": "iPhone 16 Pro Max",
            # iPads
            "iPad14,1": "iPad mini (6th gen)",
            "iPad14,2": "iPad mini (6th gen)",
            "iPad16,1": "iPad mini (7th gen)",
            "iPad16,2": "iPad mini (7th gen)",
            "iPad13,18": "iPad (10th gen)",
            "iPad13,19": "iPad (10th gen)",
            "iPad14,8": "iPad Air 11-inch (M2)",
            "iPad14,9": "iPad Air 11-inch (M2)",
            "iPad14,10": "iPad Air 13-inch (M2)",
            "iPad14,11": "iPad Air 13-inch (M2)",
            "iPad16,3": "iPad Pro 11-inch (M4)",
            "iPad16,4": "iPad Pro 11-inch (M4)",
            "iPad16,5": "iPad Pro 13-inch (M4)",
            "iPad16,6": "iPad Pro 13-inch (M4)",
        }
        return device_names.get(self.device_model, self.device_model)
    
    def get_multiplier_options(self) -> list:
        """Returns list of resolution options with calculated values for dropdown"""
        options = []
        for multiplier, name in self.RESOLUTION_MULTIPLIERS:
            if multiplier == 0:  # Custom option
                options.append(f"✏️ {name}")
            elif multiplier == 1.0:  # Native
                options.append(f"📱 {name} - {self.native_width}x{self.native_height}")
            elif multiplier < 1.0:  # Lower than native
                calc_height = int(self.native_height * multiplier)
                calc_width = int(self.native_width * multiplier)
                options.append(f"🔽 {name} - {calc_width}x{calc_height}")
            elif multiplier <= 1.5:  # Safe-ish
                calc_height = int(self.native_height * multiplier)
                calc_width = int(self.native_width * multiplier)
                options.append(f"🔼 {name} - {calc_width}x{calc_height}")
            else:  # Risky
                calc_height = int(self.native_height * multiplier)
                calc_width = int(self.native_width * multiplier)
                options.append(f"⚠️ {name} - {calc_width}x{calc_height}")
        return options

    def apply_tweak(self, other_tweaks: dict, risky_allowed: bool = False) -> dict:
        """Apply the resolution tweak"""
        if not self.enabled:
            return other_tweaks
        
        if self.di_type == -1:
            # Revert - set empty dict to remove custom resolution
            other_tweaks[self.file_location] = {}
            return other_tweaks
        
        if self.mode == 0:
            # Device not supported at all
            return other_tweaks
        
        # Apply custom resolution
        plist = {
            "canvas_height": self.custom_height,
            "canvas_width": self.custom_width
        }
        other_tweaks[self.file_location] = plist
        return other_tweaks


class MobileGestaltTweak(Tweak):
    def __init__(self,
            self,
            key: str, subkey: str = None,
            value: any = 1,
            owner: int = 501, group: int = 501
        ):
        super().__init__(key, value, owner, group)
        self.subkey = subkey

    def apply_tweak(self, plist: dict):
        if not self.enabled:
            return plist
        new_value = self.value
        if self.subkey == None:
            plist["CacheExtra"][self.key] = new_value
        else:
            plist["CacheExtra"][self.key][self.subkey] = new_value
        return plist
    
class MobileGestaltPickerTweak(Tweak):
    def __init__(self,
            self,
            key: str, subkey: str = None,
            values: list = [1]
        ):
        super().__init__(key=key, value=values)
        self.subkey = subkey
        self.selected_option = 0 # index of the selected option

    def apply_tweak(self, plist: dict):
        if not self.enabled or self.value[self.selected_option] == "Placeholder":
            return plist
        new_value = self.value[self.selected_option]
        if self.subkey == None:
            plist["CacheExtra"][self.key] = new_value
        else:
            plist["CacheExtra"][self.key][self.subkey] = new_value
            if self.subkey == "ArtworkDeviceSubType":
                plist["CacheExtra"]["YlEtTtHlNesRBMal1CqRaA"] = 1
        return plist
    
    def set_selected_option(self, new_option: int, is_enabled: bool = True):
        self.selected_option = new_option
        self.enabled = is_enabled

    def get_selected_option(self) -> int:
        return self.selected_option
    
class MobileGestaltMultiTweak(Tweak):
    def __init__(self, keyValues: dict):
        super().__init__(key=None)
        self.keyValues = keyValues
        # key values looks like ["key name" = value]

    def apply_tweak(self, plist: dict):
        if not self.enabled:
            return plist
        for key in self.keyValues:
            plist["CacheExtra"][key] = self.keyValues[key]
        return plist
    
class MobileGestaltCacheDataTweak(Tweak):
    def __init__(self, slice_start: int, slice_length: int):
        super().__init__(key=None)
        self.slice_start = slice_start
        self.slice_len = slice_length

    def apply_tweak(self, plist: dict):
        if not self.enabled:
            return plist
        data = bytes(plist["CacheData"]).hex().lower()
        if len(data) <= self.slice_start:
            raise Exception("CacheData is too short!")
        # skip the padding and get the last 2 bytes for every instance to find the offset
        pattern = re.compile(r"0+(?:5555)*([0-9a-f]{4})")
        offset = None
        value = None
        for match in pattern.finditer(data[self.slice_start : self.slice_start + self.slice_len]):
            value = match.group(1)
            if sum(c != "0" for c in value) >= 3:
                offset = self.slice_start + match.start(1)
                break
        
        # Error handling
        if offset is None:
            raise Exception("Pattern not found")
        # Get the extrema offset
        loffset = offset - 67 # real
        # TODO: Finish error handling checks

        # Set the value of the left offset to 3 to enable iPadOS
        data_list = list(data)
        data_list[loffset] = "3"
        data = "".join(data_list)
        plist["CacheData"] = bytes.fromhex(data)
        return plist
        
        
class FeatureFlagTweak(Tweak):
    def __init__(self,
            self,
                flag_category: str, flag_names: list,
                is_list: bool=True, inverted: bool=False
            ):
        super().__init__(key=None)
        self.flag_category = flag_category
        self.flag_names = flag_names
        self.is_list = is_list
        self.inverted = inverted
        
    def apply_tweak(self, plist: dict):
        to_enable = self.enabled
        if self.inverted:
            to_enable = not self.enabled
        # create the category list if it doesn't exist
        if not self.flag_category in plist:
            plist[self.flag_category] = {}
        for flag in self.flag_names:
            if self.is_list:
                plist[self.flag_category][flag] = {
                    'Enabled': to_enable
                }
            else:
                plist[self.flag_category][flag] = to_enable
        return plist