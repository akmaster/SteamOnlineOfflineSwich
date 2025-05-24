# Steam Connection Controller v1.1.0 Release Notes

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
- **SteamConnectionController.exe** - Main application (no Python required!)
- **SteamConnectionController.bat** - Batch file to run as administrator
- **test_program.py** - System compatibility checker

### Documentation
- **README.md** - Complete usage guide
- **LICENSE** - MIT license
- **CHANGELOG.md** - Version history
- **requirements.txt** - Python dependencies (for source code)

## 🚀 Quick Start

1. **Download** the release package
2. **Extract** all files to a folder
3. **Right-click** on `SteamConnectionController.bat`
4. **Select** "Run as administrator"
5. **Use** the Block/Allow buttons to control Steam's connection

## ⚠️ Important Notes

### System Requirements
- Windows 10/11
- Administrator privileges (required for firewall operations)
- Steam must be installed

### First Time Setup
- Windows Defender may show a warning (this is normal for new executables)
- Click "More info" → "Run anyway" if prompted
- The program is completely safe and open source

### How It Works
1. **Detection**: Automatically finds Steam installation
2. **Process Control**: Manages Steam processes safely
3. **Firewall Rules**: Creates/removes Windows Firewall rules
4. **Status Tracking**: Shows real-time connection status

## 🔒 Security & Privacy

- ✅ Uses only Windows built-in firewall
- ✅ No network connections made by the program
- ✅ No data collection or telemetry
- ✅ Open source code available
- ✅ Does not modify Steam files
- ✅ Does not access personal data

## 🐛 Known Issues

- Steam may take a few seconds to fully close/restart
- Some antivirus software may flag new executables (false positive)
- Requires administrator privileges for firewall operations

## 📞 Support

### Getting Help
- Check the README.md file for detailed instructions
- Use the test_program.py to diagnose system compatibility
- Report issues on GitHub with system information

### Troubleshooting
- **"Steam not found"**: Make sure Steam is installed in a standard location
- **"Administrator required"**: Always run as administrator
- **Connection status wrong**: Use "Refresh Status" button

## 🔄 Upgrade Notes

### From Previous Versions
- This version includes automatic Steam management
- All previous firewall rules will continue to work
- No manual cleanup required

### Breaking Changes
- None - fully backward compatible

## 🙏 Credits

Thank you to all users who provided feedback and suggestions for this release!

---

**Download Size**: ~15 MB  
**Installation**: Portable (no installation required)  
**License**: MIT License  
**Source Code**: Available on GitHub