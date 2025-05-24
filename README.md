# Steam Connection Controller

![GitHub release (latest by date)](https://img.shields.io/github/v/release/username/steam-connection-controller)
![GitHub](https://img.shields.io/github/license/username/steam-connection-controller)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/username/steam-connection-controller/test.yml)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![GitHub issues](https://img.shields.io/github/issues/username/steam-connection-controller)
![GitHub stars](https://img.shields.io/github/stars/username/steam-connection-controller)

A simple and effective program to control Steam's internet connection on Windows.

> **Note:** This program only works on Windows operating systems and requires administrator privileges.

## Features

- ✅ Block Steam's internet connection with one click
- ✅ Allow Steam's internet connection with one click
- ✅ **Automatic Steam closing/opening** (before and after operations)
- ✅ Real-time connection status indicator
- ✅ Automatic Steam path detection
- ✅ Steam process control and management
- ✅ Secure Windows Firewall integration
- ✅ User-friendly interface

## Requirements

- Windows 10/11
- Python 3.6 or higher
- psutil library (`pip install psutil`)
- Administrator privileges (for firewall rules)
- Steam must be installed

## Installation

1. Download these files to a folder
2. Make sure Python is installed on your system
3. Install the required library:
   ```bash
   pip install psutil
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```
4. Run `steam_controller.bat` **as administrator**

## Usage

### First Run
1. Right-click on `steam_controller.bat`
2. Select "Run as administrator"
3. The program will automatically find Steam and show the status

### Main Features

#### Block Connection
- Click the "Block Connection" button
- Steam will be automatically closed if running
- The program will block all Steam internet access
- Steam will be restarted (if it was running before)
- Status indicator will turn red

#### Allow Connection
- Click the "Allow Connection" button
- Steam will be automatically closed if running
- The program will remove Steam's internet access block
- Steam will be restarted (if it was running before)
- Status indicator will turn green

#### Status Check
- The program automatically checks status on startup
- Use "Refresh Status" button for manual checking

## Technical Details

### How It Works
The program uses Windows Firewall rules to control Steam's internet access:

1. **Steam Detection**: Scans common Steam installation paths
2. **Firewall Rules**: Blocks incoming/outgoing traffic for Steam executable files
3. **Status Tracking**: Checks existing firewall rules to show current status

### Security
- Only uses Windows built-in firewall features
- Requires no third-party software
- Does not modify Steam files
- Does not interfere with system files

### Supported Steam Files
- `steam.exe` (Main Steam application)
- `steamwebhelper.exe` (Web browser component)

### Supported Steam Paths
- `C:\Program Files (x86)\Steam\`
- `C:\Program Files\Steam\`
- `D:\Steam\`
- `E:\Steam\`

## Troubleshooting

### "Steam not found" Error
- Make sure Steam is installed in standard locations
- Supported paths:
  - `C:\Program Files (x86)\Steam\`
  - `C:\Program Files\Steam\`
  - `D:\Steam\`
  - `E:\Steam\`

### "Administrator privileges required" Error
- Always run the program with "Run as administrator"
- Windows Firewall rules require administrator privileges

### Connection Status Appears Wrong
- Click "Refresh Status" button
- Restart Steam
- Close and reopen the program

## Frequently Asked Questions

**Q: Can I use this program while Steam is open?**
A: Yes, you can use it while Steam is open. Changes take effect immediately.

**Q: Does this program damage Steam?**
A: No, it only creates firewall rules. It doesn't touch Steam files.

**Q: Do settings persist after closing the program?**
A: Yes, firewall rules are persistent in Windows. Closing the program doesn't affect settings.

**Q: Does it affect other games?**
A: No, it only creates Steam-specific rules.

## License

This program is created for educational purposes. Use at your own risk.

## Support

For issues:
1. Check the README file
2. Review the troubleshooting section
3. Make sure you're running the program as administrator