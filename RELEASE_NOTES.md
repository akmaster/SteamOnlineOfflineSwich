# Game Client Connection Controller - Release Notes

**Note:** This project was formerly known as "Steam Connection Controller". Recent versions now support multiple game clients including Steam, Ubisoft Connect, EA Play, and Rockstar Games Launcher. The release notes below for v1.1.0 pertain to the Steam-only version. Future release notes will detail features for the multi-client versions.

---

# Steam Connection Controller v1.1.0 Release Notes (Legacy)

## 🎉 What's New

### ✨ Major Features
- **Automatic Steam Management**: Steam is now automatically closed before operations and restarted afterward
- **Enhanced User Experience**: Clear prompts and status updates throughout the process
- **Smart Process Control**: Only restarts Steam if it was running before the operation

### 🔧 Technical Improvements
- Added `psutil` library for reliable process management
- Improved error handling and user feedback
- Thread-safe operations to prevent GUI freezing
- Better timing control for Steam operations

### 🎯 User Interface
- All text and messages now in English
- Clear status indicators: "Closing Steam...", "Creating firewall rules...", "Restarting Steam..."
- User confirmation dialogs before Steam is closed
- Detailed success/failure messages

## 📦 What's Included

### Executable Files
- **SteamConnectionController.exe** - Main application (no Python required for this version!)
- **SteamConnectionController.bat** - Batch file to run as administrator (for this version)
- **test_program.py** - System compatibility checker (for this version)

### Documentation
- **README.md** - Complete usage guide
- **LICENSE** - MIT license
- **CHANGELOG.md** - Version history
- **requirements.txt** - Python dependencies (for source code)

## 🚀 Quick Start

1. **Download** the release package
2. **Extract** all files to a folder
3. **Right-click** on `SteamConnectionController.bat` (for this specific v1.1.0 release)
4. **Select** "Run as administrator"
5. **Use** the Block/Allow buttons to control Steam's connection (for this specific v1.1.0 release)

## ⚠️ Important Notes (General - Applicable to newer versions as well)

### System Requirements
- Windows 10/11
- Administrator privileges (required for firewall operations)
- Relevant game client(s) must be installed

### First Time Setup
- Windows Defender may show a warning (this is normal for new executables)
- Click "More info" → "Run anyway" if prompted
- The program is completely safe and open source

### How It Works (General Principle)
1. **Detection**: Automatically finds supported game client installations.
2. **Process Control**: Manages client processes safely (closing/restarting as needed).
3. **Firewall Rules**: Creates/removes Windows Firewall rules for selected client executables.
4. **Status Tracking**: Shows real-time connection status for the selected client.

## 🔒 Security & Privacy (General Principles)

- ✅ Uses only Windows built-in firewall
- ✅ No network connections made by the program itself for its core function
- ✅ No data collection or telemetry
- ✅ Open source code available
- ✅ Does not modify game client files
- ✅ Does not access personal data

## 🐛 Known Issues (General)

- Game clients may take a few seconds to fully close/restart.
- Some antivirus software may flag new executables (false positive).
- Requires administrator privileges for firewall operations.

## 📞 Support (General)

### Getting Help
- Check the README.md file for detailed instructions.
- Use the test_program.py to diagnose system compatibility.
- Report issues on GitHub with system information and selected client.

### Troubleshooting (General)
- **"Client not found"**: Make sure the selected client is installed in a standard location.
- **"Administrator required"**: Always run as administrator.
- **Connection status wrong**: Use "Refresh Status" button for the selected client.

## 🔄 Upgrade Notes

### From Previous Versions (e.g., v1.1.0 to newer multi-client versions)
- Newer versions support multiple game clients.
- The executable and .bat file names have changed to `GameClientController`.
- All previous firewall rules created by older versions (for Steam) should still be manageable if Steam is selected, but it's recommended to manage rules through the latest version of the application.
- No manual cleanup of old rules is strictly required, but you can remove them if you prefer to only use rules created by the new version.

### Breaking Changes
- None - fully backward compatible

### Breaking Changes
- None - fully backward compatible

## 🙏 Credits

Thank you to all users who provided feedback and suggestions for this release!

---

**Download Size**: ~15 MB  
**Installation**: Portable (no installation required)  
**License**: MIT License  
**Source Code**: Available on GitHub
