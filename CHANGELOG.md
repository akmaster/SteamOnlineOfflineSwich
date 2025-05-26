# Changelog

This file contains all notable changes to the Game Client Connection Controller project.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Support for Ubisoft Connect
- Support for EA Play (EA Desktop/Origin)
- Support for Rockstar Games Launcher
- General refactoring for multi-client support
- Updated UI to select different game clients
- Updated build scripts and GitHub actions for the new project name and scope.
- Updated documentation (README, ISSUE_TEMPLATES, etc.) to reflect multi-client support.

### Planned Features
- Timer feature (automatic on/off at specific times)
- Profile system (different setting sets for each client)
- System tray integration
- Support for more client installation paths
- Support for other gaming platforms (e.g., Epic Games Store, GOG Galaxy)

## [1.2.0] - YYYY-MM-DD <!-- TODO: Update with actual release date -->
### Added
- **Multi-Client Support**: Added functionality to control internet connection for:
  - Steam
  - Ubisoft Connect (Uplay)
  - EA Play (EA Desktop/Origin)
  - Rockstar Games Launcher
- UI updated with radio buttons to select the active client.
- Detection logic for all supported clients.
- Firewall rule management generalized for all clients.
- Process management (close/restart) generalized for all clients.
- Project files (build scripts, test programs, GitHub workflows, documentation) updated to reflect the new "Game Client Connection Controller" name and scope.

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
- Thread-safe client operations
- More reliable process control

## [1.0.0] - 2025-01-24

### Added Features (Initially for Steam)
- ✨ Block/allow Steam's internet connection with one click
- 🎯 Real-time connection status indicator
- 🔍 Automatic Steam path detection
- 🛡️ Secure Windows Firewall integration
- 🖥️ User-friendly GUI interface
- ⚡ Automatic administrator privilege control
- 📊 System compatibility test tool
- 🔄 Status refresh feature

### Technical Features (Initially for Steam)
- Python 3.6+ support
- tkinter-based GUI
- Windows Firewall API integration
- Multiple Steam installation path support
- Thread-safe operations
- Error handling and user feedback

### Supported Client Files (Initially for Steam)
- `steam.exe` (Main Steam application)
- `steamwebhelper.exe` (Web browser component)
<!-- This section can be expanded or moved to a general "Supported Clients" section in newer versions -->

### Supported Client Paths (Initially for Steam)
- `C:\Program Files (x86)\Steam\`
- `C:\Program Files\Steam\`
- `D:\Steam\`
- `E:\Steam\`
<!-- This section can be expanded or moved to a general "Supported Clients" section in newer versions -->

### Security
- Only uses Windows built-in firewall
- Requires no third-party software
- Does not interfere with client files
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
This first stable release included all essential features needed to safely and easily control Steam's internet connection. The program used Windows Firewall rules to manage Steam's internet access and provided a user-friendly interface. (Functionality now expanded to multiple clients).

### Known Limitations (General)
- Only works on Windows operating systems
- Requires administrator privileges
- Supports standard installation paths for detected clients
- Firewall rules can be manually deleted

### Future Releases
Future releases will include more features, better error handling, and potentially support for more gaming platforms.

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
