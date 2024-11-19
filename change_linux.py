import subprocess

def change_wallpaper_linux(image_path):
    """
    Changes the desktop wallpaper on Linux (GNOME-based environments).
    """
    try:
       
        subprocess.run(
            ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{image_path}"],
            check=True
        )
      
        return True
    except Exception as e:
        print(f"Error changing wallpaper: {e}")
        return False
