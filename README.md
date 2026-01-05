============================================================
           DISCORD USERNAME SCANNER (PYTHON VERSION)
============================================================

A customizable Python tool to check for available Discord 
usernames. This version runs directly via the Python 
interpreter.

--- PREREQUISITES ---

1. Python 3.x installed on your system.
2. The 'requests' library.

If you don't have the library, install it via your terminal:
   pip install requests

--- HOW TO RUN ---

1. Open your terminal or command prompt.
2. Navigate to the folder containing 'main.py'.
3. Run the script using:
   python main.py

--- CONFIGURATION OPTIONS ---

Upon startup, the script will ask for:
* Length: How many characters the name should be (e.g., 3).
* Letters/Numbers/Dots: Toggle each character type (y/n).
* Delay: Time in seconds between checks. 
  - Recommended: 3.0 to 6.0 seconds to avoid IP bans.

--- AUTOMATIC LOGGING ---

The script generates two files in the same directory:
1. checked_names.txt:  A list of every name already checked.
                       This allows you to close the script 
                       and resume exactly where you left off.
2. available_names.txt: A list of names that returned a 404 
                       (Available) status from Discord.

--- IMPORTANT SAFETY & LIMITS ---

* RATE LIMITING: Discord's API is protected by Cloudflare. 
  If you check names too quickly, you will be rate limited 
  (Status 429). The script will automatically detect this 
  and pause for 2 minutes before trying again.
* INVALID NAMES: The script automatically skips names that 
  start/end with a dot or contain ".." as per Discord's rules.
* DISCLAIMER: Use this tool responsibly. Excessive automated 
  requests can lead to temporary or permanent IP blocks.

============================================================
