import subprocess

def change_wallpaper_mac(image_path):
    """
    Changes the desktop wallpaper on macOS.
    """
    try:
        script = f"""
            tell application "System Events"
                tell current desktop
                    set picture to "{image_path}"
                end tell
            end tell
        """

        subprocess.run(["osascript", "-e", script], check=True)
       
        return True
    except Exception as e:
        print(f"Error changing wallpaper: {e}")
        return False
