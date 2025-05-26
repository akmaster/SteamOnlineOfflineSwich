# Game Client Connection Controller

![GitHub release (latest by date)](https://img.shields.io/github/v/release/akmaster/SteamOnlineOfflineSwich) <!-- TODO: Update repo name in URL if changed -->
![GitHub](https://img.shields.io/github/license/akmaster/SteamOnlineOfflineSwich) <!-- TODO: Update repo name in URL if changed -->
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/akmaster/SteamOnlineOfflineSwich/test.yml) <!-- TODO: Update repo name in URL if changed -->
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![GitHub issues](https://img.shields.io/github/issues/akmaster/SteamOnlineOfflineSwich) <!-- TODO: Update repo name in URL if changed -->
![GitHub stars](https://img.shields.io/github/stars/akmaster/SteamOnlineOfflineSwich) <!-- TODO: Update repo name in URL if changed -->
![Downloads](https://img.shields.io/github/downloads/akmaster/SteamOnlineOfflineSwich/total) <!-- TODO: Update repo name in URL if changed -->

A simple and effective program to control the internet connection of various game clients (Steam, Ubisoft Connect, EA Play, Rockstar Launcher) on Windows.

> **Note:** This program only works on Windows operating systems and requires administrator privileges.

## 📥 Download

### 🎯 Latest Release: [v1.2.0 (Example)](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/latest) <!-- TODO: Update version and repo name -->

#### 📦 Recommended Download:
- **[Complete Package (ZIP)](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/download/v1.2.0/GameClientController_v1.2.0.zip)** <!-- TODO: Update version and repo name --> - Includes documentation and all files

#### ⚡ Quick Download:
- **[Standalone Executable](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/download/v1.2.0/GameClientController.exe)** <!-- TODO: Update version and repo name --> - Just the program file

> 💡 **First time?** Download the complete package for full documentation and setup instructions.

## Features

- ✅ Control internet connection for multiple game clients:
  - Steam
  - Ubisoft Connect (Uplay)
  - EA Play (EA Desktop/Origin)
  - Rockstar Games Launcher
  - Epic Games Launcher
- ✅ Block client's internet connection with one click
- ✅ Allow client's internet connection with one click
- ✅ **Automatic client closing/opening** (before and after operations)
- ✅ Real-time connection status indicator
- ✅ Automatic client path detection for supported clients
- ✅ Client process control and management
- ✅ Secure Windows Firewall integration
- ✅ User-friendly interface

## Requirements

- Windows 10/11
- Python 3.8 or higher (for source code usage)
- psutil library (`pip install psutil`)
- Administrator privileges (for firewall rules)
- Supported game client(s) must be installed

## Installation

1. Download these files to a folder (or use the pre-built executable from Releases).
2. If running from source:
   - Make sure Python is installed on your system.
   - Install the required library:
     ```bash
     pip install psutil
     ```
     or
     ```bash
     pip install -r requirements.txt
     ```
3. Run `game_client_controller.bat` **as administrator**.

## Usage

### First Run
1. Right-click on `game_client_controller.bat` (or the `.exe` file).
2. Select "Run as administrator".
3. The program will automatically try to find installed clients and show the status for the default selected client (Steam).
4. Use the radio buttons to select the desired game client.

### Main Features

#### Block Connection
- Select the desired game client from the radio buttons.
- Click the "Block Connection" button.
- The selected client will be automatically closed if running.
- The program will block all internet access for the selected client's executables.
- The client will be restarted (if it was running before).
- Status indicator will turn red for the selected client.

#### Allow Connection
- Select the desired game client.
- Click the "Allow Connection" button.
- The selected client will be automatically closed if running.
- The program will remove the internet access block for the selected client.
- The client will be restarted (if it was running before).
- Status indicator will turn green for the selected client.

#### Status Check
- The program automatically checks status on startup for the default client.
- When a client is selected, its status is checked.
- Use "Refresh Status" button for manual checking of the currently selected client.

## Technical Details

### How It Works
The program uses Windows Firewall rules to control game clients' internet access:

1. **Client Detection**: Scans common installation paths for supported game clients (Steam, Ubisoft Connect, EA Play, Rockstar Launcher).
2. **Firewall Rules**: Blocks incoming/outgoing traffic for the executable files of the selected client.
3. **Status Tracking**: Checks existing firewall rules to show current status for the selected client.

### Security
- Only uses Windows built-in firewall features.
- Requires no third-party software.
- Does not modify game client files.
- Does not interfere with system files.

### Supported Client Executables (Examples)
- **Steam**: `steam.exe`, `steamwebhelper.exe`
- **Ubisoft Connect**: `upc.exe`, `UbisoftGameLauncher.exe`, `UbisoftConnect.exe`, `UbisoftGameLauncherService.exe`
- **EA Play**: `EADesktop.exe`, `EALauncher.exe`, `EABackgroundService.exe`
- **Rockstar Launcher**: `Launcher.exe`, `LauncherPatcher.exe`, `RockstarService.exe`
- **Epic Games Launcher**: `EpicGamesLauncher.exe`, `EpicWebHelper.exe`
(The program attempts to find a comprehensive list of executables for each client.)

### Supported Client Paths (Examples)
- `C:\Program Files (x86)\Steam\`
- `C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\`
- `C:\Program Files\Electronic Arts\EA Desktop\EA Desktop\`
- `C:\Program Files\Rockstar Games\Launcher\`
- `C:\Program Files (x86)\Epic Games\Launcher\`
(And other common installation locations on different drives.)

## Troubleshooting

### "Client not found" Error
- Make sure the selected game client is installed in standard locations.
- The program scans common paths; if your client is in a very custom location, it might not be detected.

### "Administrator privileges required" Error
- Always run the program with "Run as administrator".
- Windows Firewall rules require administrator privileges.

### Connection Status Appears Wrong
- Click "Refresh Status" button for the selected client.
- Restart the game client.
- Close and reopen the program.

## Frequently Asked Questions

**Q: Can I use this program while a game client is open?**
A: Yes, you can use it while a client is open. The program will attempt to close and restart the client to apply changes.

**Q: Does this program damage game clients?**
A: No, it only creates firewall rules. It doesn't touch client files.

**Q: Do settings persist after closing the program?**
A: Yes, firewall rules are persistent in Windows. Closing the program doesn't affect settings.

**Q: Does it affect other games or applications?**
A: No, it only creates rules specific to the executables of the selected game client.

## License

This program is created for educational and personal use. Use at your own risk.

## Support

For issues:
1. Check this README file.
2. Review the troubleshooting section.
3. Make sure you're running the program as administrator.
4. Report bugs on [GitHub Issues](https://github.com/akmaster/SteamOnlineOfflineSwich/issues). <!-- TODO: Update repo name in URL if changed -->

## 🔗 Links

- **GitHub Repository**: [https://github.com/akmaster/SteamOnlineOfflineSwich](https://github.com/akmaster/SteamOnlineOfflineSwich) <!-- TODO: Update repo name in URL if changed -->
- **Latest Release**: [Download Latest Version](https://github.com/akmaster/SteamOnlineOfflineSwich/releases/latest) <!-- TODO: Update repo name in URL if changed -->
- **Report Issues**: [GitHub Issues](https://github.com/akmaster/SteamOnlineOfflineSwich/issues) <!-- TODO: Update repo name in URL if changed -->
- **Contribute**: [Contributing Guide](CONTRIBUTING.md)

## ⭐ Star This Project

If you find this tool useful, please consider giving it a star on GitHub! It helps others discover the project.

[![GitHub stars](https://img.shields.io/github/stars/akmaster/SteamOnlineOfflineSwich?style=social)](https://github.com/akmaster/SteamOnlineOfflineSwich/stargazers) <!-- TODO: Update repo name in URL if changed -->
