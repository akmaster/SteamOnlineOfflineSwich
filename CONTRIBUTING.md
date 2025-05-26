# Contributing Guide

Thank you for wanting to contribute to the Game Client Connection Controller project! 🎉

## 📋 Table of Contents
- [Types of Contributions](#types-of-contributions)
- [Development Environment](#development-environment)
- [Code Standards](#code-standards)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Community Guidelines](#community-guidelines)

## 🤝 Types of Contributions

### 🐛 Bug Reports
- Report bugs you encounter using the [bug report template](/.github/ISSUE_TEMPLATE/bug_report.md)
- Describe the steps to reproduce the bug in detail
- Include your system information

### ✨ Feature Suggestions
- Share your new feature ideas using the [feature request template](/.github/ISSUE_TEMPLATE/feature_request.md)
- Explain why this feature is needed
- Include mockups or design examples if possible

### 📝 Documentation
- Improve the README file
- Enhance code comments
- Expand the user guide

### 💻 Code Contributions
- Bug fixes
- New features
- Performance improvements
- Code refactoring

## 🛠️ Development Environment

### Requirements
- Windows 10/11
- Python 3.6+
- Git
- Administrator privileges (for testing)

### Setup
1. Fork the repository
2. Clone to your local machine:
   ```bash
   git clone https://github.com/akmaster/SteamOnlineOfflineSwich.git <!-- TODO: Update repo URL if changed -->
   cd SteamOnlineOfflineSwich <!-- TODO: Update directory name if changed -->
   ```
3. Run the test program:
   ```bash
   python test_program.py
   ```

### Development Branches
- `main`: Stable version
- `develop`: Development branch
- `feature/feature-name`: New features
- `bugfix/bug-name`: Bug fixes

## 📏 Code Standards

### Python Code Style
- Follow PEP 8 standards
- Function and variable names can be in English
- Write docstrings in English

### Example Code Format
```python
def block_client_connection(self, client_name):
    """Block the selected game client's internet connection.
    
    Args:
        client_name (str): The name of the client (e.g., "Steam", "Ubisoft").

    Returns:
        bool: True if operation successful, False otherwise
    """
    try:
        # Code here to block connection for the given client_name
        print(f"Blocking connection for {client_name}...")
        return True
    except Exception as e:
        print(f"Error blocking {client_name}: {e}")
        return False
```

### Commit Messages
Use English commit messages:
- `feat: add new feature`
- `fix: fix bug`
- `docs: update documentation`
- `style: fix code formatting`
- `refactor: refactor code`
- `test: add tests`

## 🔄 Pull Request Process

### 1. Preparation
- Create an issue or choose an existing one
- Create a feature branch:
  ```bash
  git checkout -b feature/new-feature
  ```

### 2. Development
- Make your changes
- Follow code standards
- Test your changes

### 3. Testing
- Test the program in different scenarios
- Run system tests with `test_program.py`
- Ensure existing features still work

### 4. Commit and Push
```bash
git add .
git commit -m "feat: new feature description"
git push origin feature/new-feature
```

### 5. Pull Request
- Create a PR on GitHub
- Fill out the [PR template](/.github/pull_request_template.md)
- Wait for reviewers

## 🐛 Issue Reporting

### Bug Reports
1. Check existing issues first
2. Make sure you can reproduce the bug
3. Fill out the template completely
4. Include screenshots

### Feature Requests
1. Explain the necessity of the feature
2. Define use cases
3. Include technical details

## 👥 Community Guidelines

### Code of Conduct
- Be respectful and constructive
- Communicate in English
- Be open to collaboration
- Accept criticism constructively

### Communication Channels
- GitHub Issues: Bug reports and feature requests
- GitHub Discussions: General discussions
- Pull Request comments: Code reviews

## 🏷️ Labels

### Issue Labels
- `bug`: Bug reports
- `enhancement`: Feature requests
- `question`: Questions and support
- `documentation`: Documentation
- `good first issue`: Good for beginners
- `help wanted`: Help needed topics

### Priority Labels
- `priority: low`: Low priority
- `priority: medium`: Medium priority
- `priority: high`: High priority
- `priority: critical`: Critical

## 🎯 Development Goals

### Short Term
- [ ] Support for more client installation paths for all supported clients
- [ ] Enhanced error handling for multi-client scenarios
- [ ] UI improvements for better client selection and status display

### Long Term
- [ ] Support for other gaming platforms (e.g., Epic Games Store, GOG Galaxy)
- [ ] Timer feature (automatic on/off at specific times for selected clients)
- [ ] Profile system (different setting sets, possibly per client)

## 📞 Help

For questions:
1. Use the [Support template](/.github/ISSUE_TEMPLATE/support_request.md)
2. Check existing documentation
3. Use GitHub Discussions

---

**Thank you!** 🙏
Your contributions make this project better.
