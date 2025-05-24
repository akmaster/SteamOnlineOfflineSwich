# Changelog

This file contains all notable changes to the Steam Connection Controller project.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- Timer feature (automatic on/off at specific times)
- Profile system (different setting sets)
- System tray integration
- Support for more Steam paths
- Support for other gaming platforms (Epic Games, Origin, etc.)

## [1.1.0] - 2025-01-24

### Added Features
- ✨ **Automatic Steam closing/opening system**: Steam is automatically closed before connection changes and then reopened
- 🔍 Steam process control and management (psutil integration)
- ⚡ Enhanced user feedback (warning about Steam being closed)
- 📋 Detailed operation status display
- 🔄 Smart Steam restart (only if it was running before)

### Improved
- 🚀 More effective connection control (by closing Steam)
- 💬 Enhanced user interface messages
- 📊 More detailed operation reporting
- ⏱️ Optimized timing for Steam operations

### Technical Improvements
- psutil library integration
- Enhanced error handling
- Thread-safe Steam operations
- More reliable process control

## [1.0.0] - 2025-01-24

### Added Features
- ✨ Block/allow Steam's internet connection with one click
- 🎯 Real-time connection status indicator
- 🔍 Automatic Steam path detection
- 🛡️ Secure Windows Firewall integration
- 🖥️ User-friendly GUI interface
- ⚡ Automatic administrator privilege control
- 📊 System compatibility test tool
- 🔄 Status refresh feature

### Technical Features
- Python 3.6+ support
- tkinter-based GUI
- Windows Firewall API integration
- Multiple Steam installation path support
- Thread-safe operations
- Error handling and user feedback

### Supported Steam Files
- `steam.exe` (Main Steam application)
- `steamwebhelper.exe` (Web browser component)

### Supported Steam Paths
- `C:\Program Files (x86)\Steam\`
- `C:\Program Files\Steam\`
- `D:\Steam\`
- `E:\Steam\`

### Security
- Only uses Windows built-in firewall
- Requires no third-party software
- Does not interfere with Steam files
- Does not modify system files

### Documentation
- 📖 Comprehensive README file
- 🤝 Contributing guide
- 🐛 Issue templates
- 📋 Pull request template
- 🔧 System test tool

### GitHub Integration
- 🔄 Automatic test workflow
- 📦 Automatic release creation
- 🏷️ Issue and PR templates
- 📊 Code quality checks
- 🔒 Security scans

## Release Notes

### About [1.0.0]
This first stable release includes all essential features needed to safely and easily control Steam's internet connection. The program uses Windows Firewall rules to manage Steam's internet access and provides a user-friendly interface.

### Known Limitations
- Only works on Windows operating systems
- Requires administrator privileges
- Supports standard Steam installation paths
- Firewall rules can be manually deleted

### Future Releases
Future releases will include more features, better error handling, and expanded platform support.

---

## Tag Descriptions

- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Features that will be removed soon
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security-related changes

## Contributing

To contribute to the changelog:
1. Add relevant changes to the `[Unreleased]` section in each PR
2. Use appropriate tags
3. Write user-friendly descriptions
4. Add technical details if necessary

For more information, see [CONTRIBUTING.md](CONTRIBUTING.md).