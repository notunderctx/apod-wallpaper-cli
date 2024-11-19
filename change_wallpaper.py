import platform

from change_linux import change_wallpaper_linux

from change_darwin import change_wallpaper_mac

from change_windows import change_wallpaper_windows

def change_wallpaper(image_path):
    """
    Changes the desktop wallpaper based on the operating system.
    """
    current_os = platform.system()

    if current_os == "Windows":
        return change_wallpaper_windows(image_path)
    elif current_os == "Darwin":  
        return change_wallpaper_mac(image_path)
    elif current_os == "Linux":
        return change_wallpaper_linux(image_path)
    else:
        print(f"Unsupported operating system: {current_os}")
        return False
