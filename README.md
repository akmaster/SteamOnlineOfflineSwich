# Steam Connection Controller

![GitHub release (latest by date)](https://img.shields.io/github/v/release/akmaster/SteamOnlineOfflineSwich)
![GitHub](https://img.shields.io/github/license/akmaster/SteamOnlineOfflineSwich)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/akmaster/SteamOnlineOfflineSwich/test.yml)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![GitHub issues](https://img.shields.io/github/issues/akmaster/SteamOnlineOfflineSwich)
![GitHub stars](https://img.shields.io/github/stars/akmaster/SteamOnlineOfflineSwich)
![Downloads](https://img.shields.io/github/downloads/akmaster/SteamOnlineOfflineSwich/total)

A simple and effective program to control Steam's internet connection on Windows.

> **Note:** This program only works on Windows operating systems and requires administrator privileges.

## 📥 Download

### 🎯 Latest Release: [v1.1.0](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/latest)

#### 📦 Recommended Download:
- **[Complete Package (ZIP)](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/download/v1.1.0/SteamConnectionController_v1.1.0.zip)** - Includes documentation and all files

#### ⚡ Quick Download:
- **[Standalone Executable](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/download/v1.1.0/SteamConnectionController.exe)** - Just the program file

> 💡 **First time?** Download the complete package for full documentation and setup instructions.

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
4. Report bugs on [GitHub Issues](https://github.com/akmaster/SteamOnlineOfflineSwich/issues)

## 🔗 Links

- **GitHub Repository**: [https://github.com/akmaster/SteamOnlineOfflineSwich](https://github.com/akmaster/SteamOnlineOfflineSwich)
- **Latest Release**: [Download v1.1.0](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/latest)
- **Report Issues**: [GitHub Issues](https://github.com/akmaster/SteamOnlineOfflineSwich/issues)
- **Contribute**: [Contributing Guide](CONTRIBUTING.md)

## ⭐ Star This Project

If you find this tool useful, please consider giving it a star on GitHub! It helps others discover the project.

[![GitHub stars](https://img.shields.io/github/stars/akmaster/SteamOnlineOfflineSwich?style=social)](https://github.com/akmaster/SteamOnlineOfflineSwich/stargazers)