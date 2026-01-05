============================================================
           DISCORD USERNAME SCANNER & CHECKER
============================================================

A lightweight, customizable Python tool designed to check the 
availability of Discord usernames based on specific character 
requirements.

--- FEATURES ---

* Resume Support: Automatically skips names already checked 
  (saves progress in checked_names.txt).
* Customization: Choose exact length and toggle between 
  letters, numbers, and periods.
* Anti-Ban Logic: Includes randomized delays and browser 
  spoofing to mimic human behavior.
* Export: Saves all available names to available_names.txt.

--- HOW TO USE ---

1. Run the main.exe (or main.py if using Python).
2. Follow the on-screen prompts to set your requirements:
   - Length: The number of characters (e.g., 3).
   - Characters: Toggle (y/n) for letters, numbers, and dots.
   - Delay: Set the speed (Recommended: 3 to 6 seconds).
3. The scanner will begin. Available names will appear in green 
   or with a [+] symbol and be saved immediately to the text file.

--- USERNAME RULES (DISCORD) ---

The tool automatically follows these Discord-enforced rules:
* No consecutive periods (e.g., "a..b" is skipped).
* Cannot start or end with a period (e.g., ".ab" is skipped).
* Only lowercase letters (a-z), numbers (0-9), and dots (.) 
  are allowed.

--- IMPORTANT NOTES & SAFETY ---

* RATE LIMITING: If you see "Rate Limited" messages, it means 
  you are checking too fast. The tool will pause for 2 minutes. 
  To avoid this, use a higher delay (5+ seconds) or a VPN.
* AVAILABILITY: A "Available" result means the Discord API 
  returned a 404. Some names may still be reserved by Discord 
  system accounts or banned users.
* TERMS OF SERVICE: Use this tool responsibly. Excessive 
  automated requests to any API can result in an IP ban.

--- FILES ---

* main.exe           - The application.
* checked_names.txt  - History of names scanned (Do not delete 
                       if you want to resume later).
* available_names.txt - Your "hits" / available usernames.
============================================================
