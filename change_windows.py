import ctypes

def change_wallpaper_windows(image_path):
    """
    Changes the desktop wallpaper on Windows.
    """
    SPI_SETDESKWALLPAPER = 20 
    SPIF_UPDATEINIFILE = 0x01 
    SPIF_SENDWININICHANGE = 0x02  

    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path,
                                                   SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
      
        return True
    except Exception as e:
        print(f"Error changing wallpaper: {e}")
        return False
