# Network Reconnaissance Tool

A powerful, multi-threaded port scanner with banner grabbing for security professionals. Detects open ports, identifies services, and grabs banners to help you understand what's running on target systems.

**Works on: Windows, macOS, Linux (Ubuntu, Kali, Debian, etc.)**

---

## 🚀 Quick Start (For Beginners)

Choose your operating system and follow the steps:

### 🪟 Windows

#### Step 1: Install Python

1. Go to [python.org/downloads](https://python.org/downloads)
2. Click **Download Python** (latest version)
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" at the bottom
5. Click **Install Now**

Verify installation:
```cmd
python --version
```

#### Step 2: Download the Tool

**Option A: Using Git**
```cmd
# Install Git from https://git-scm.com/download/win
# Then open Command Prompt or PowerShell and run:

git clone https://github.com/Omkar409/network-recon-tool.git
cd network-recon-tool
```

**Option B: Manual Download (No Git)**
1. Go to: https://github.com/Omkar409/network-recon-tool
2. Click green **Code** button → **Download ZIP**
3. Extract the ZIP to your Desktop
4. Open Command Prompt in the extracted folder

#### Step 3: Run the Tool

```cmd
# Make script executable (if needed)
# Then run the scanner
python network_recon.py

# Or scan a specific target
python network_recon.py --target 192.168.1.1

# Scan specific ports
python network_recon.py --target 192.168.1.1 --ports 80,443,8080
```

---

### 🍎 macOS

#### Step 1: Install Python

```bash
# Check if Python is installed
python3 --version

# If not installed, install via Homebrew:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
```

#### Step 2: Download the Tool

```bash
# Install git if needed
brew install git

# Clone the repository
git clone https://github.com/Omkar409/network-recon-tool.git
cd network-recon-tool
```

Or manually download the ZIP from GitHub and extract it.

#### Step 3: Run the Tool

```bash
# Make executable
chmod +x network_recon.py
chmod +x setup.sh

# Run setup (if needed)
./setup.sh

# Run the scanner
python3 network_recon.py

# Or scan a specific target
python3 network_recon.py --target 192.168.1.1

# Scan specific ports
python3 network_recon.py --target 192.168.1.1 --ports 80,443,8080
```

---

### 🐧 Linux (Ubuntu, Kali, Debian, etc.)

#### Step 1: Install Python

```bash
# Check if Python is installed
python3 --version

# If not installed:
sudo apt update
sudo apt install python3 python3-pip -y
```

#### Step 2: Download the Tool

```bash
# Install git if needed
sudo apt install git -y

# Clone the repository
git clone https://github.com/Omkar409/network-recon-tool.git
cd network-recon-tool
```

Or manually download the ZIP from GitHub and extract it.

#### Step 3: Run the Tool

```bash
# Make executable
chmod +x network_recon.py
chmod +x setup.sh

# Run setup (if needed)
./setup.sh

# Run the scanner
python3 network_recon.py

# Or scan a specific target
python3 network_recon.py --target 192.168.1.1

# Scan specific ports
python3 network_recon.py --target 192.168.1.1 --ports 80,443,8080

# Full port range scan
python3 network_recon.py --target 192.168.1.1 --ports 1-65535
```

---

## 📋 What You'll See

When you run the tool, you'll get output like this:

```
╔══════════════════════════════════════════════════════════════╗
║         NETWORK RECONNAISSANCE TOOL v1.0                     ║
║              Cross-Platform Security Tool                    ║
╚══════════════════════════════════════════════════════════════╝

[+] Target: 192.168.1.1
[+] Scanning ports: 1-1000
[+] Threads: 100
[+] Started at: 14:30:25

┌─ Scan Results ─────────────────────────────────────────┐
│ Port     Status    Service      Banner               │
├────────────────────────────────────────────────────────┤
│ 22/tcp   OPEN      SSH          OpenSSH 8.2p1       │
│ 80/tcp   OPEN      HTTP          Apache/2.4.41       │
│ 443/tcp  OPEN      HTTPS         Apache/2.4.41       │
│ 3306/tcp OPEN      MySQL         MySQL 8.0.25        │
│ 8080/tcp OPEN      HTTP-proxy    nginx/1.18.0        │
└────────────────────────────────────────────────────────┘

[+] Scan completed in 12.45 seconds
[+] Open ports found: 5
[+] Report saved to: scan_192.168.1.1_20240101.txt
```

---

## 📖 How to Use (Command Line Options)

| Option | What It Does | Example |
|---------|-----------|---------|
| `--target` | IP address to scan | `--target 192.168.1.1` |
| `--ports` | Port range to scan | `--ports 80,443` or `--ports 1-1000` |
| `--threads` | Number of threads | `--threads 50` |
| `--timeout` | Connection timeout | `--timeout 3` |
| `--banner` | Enable banner grabbing | `--banner` |
| `--output` | Save results to file | `--output results.txt` |
| `--help` | Show all options | `--help` |

---

## 🎓 Understanding the Results

### Port Status

| Status | Meaning | Action |
|--------|---------|--------|
| **OPEN** | Port is accepting connections | Investigate the service |
| **CLOSED** | Port is not accepting connections | Normal, no action needed |
| **FILTERED** | Port is blocked by firewall | May need different scan type |

### Common Ports to Check

| Port | Service | Risk Level |
|------|---------|------------|
| 21 | FTP | Medium |
| 22 | SSH | Low (if secured) |
| 23 | Telnet | **High** (unencrypted) |
| 25 | SMTP | Medium |
| 53 | DNS | Low |
| 80 | HTTP | Medium |
| 110 | POP3 | Medium |
| 143 | IMAP | Medium |
| 443 | HTTPS | Low |
| 3306 | MySQL | **High** (if exposed) |
| 3389 | RDP | **High** (if exposed) |
| 8080 | HTTP Proxy | Medium |

---

## 🛠️ Advanced Setup (Optional)

### Create Virtual Environment (Recommended for Developers)

**Windows:**
```cmd
cd network-recon-tool
python -m venv venv
venv\Scriptsctivate
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
cd network-recon-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Deactivate when done:**
```bash
deactivate
```

---

## 🐛 Troubleshooting

### Windows: `python is not recognized`

**Fix:** Reinstall Python and check "Add Python to PATH" during installation.

### macOS/Linux: `python3: command not found`

**Fix:**
```bash
# macOS
brew install python3

# Linux (Ubuntu/Debian/Kali)
sudo apt update
sudo apt install python3 -y
```

### `Permission denied` (macOS/Linux)

**Fix:**
```bash
chmod +x network_recon.py
chmod +x setup.sh
```

### `Connection refused` or timeout errors

**Fix:**
- Check if target is online: `ping 192.168.1.1`
- Try increasing timeout: `--timeout 5`
- Check your firewall settings
- Some networks block port scanning (use responsibly!)

### Colors look weird or don't show

**Fix:** The tool auto-detects color support. If colors don't work, the tool still functions normally.

For Windows, install colorama:
```bash
pip install colorama
```

### `ModuleNotFoundError: No module named 'threading'`

**Fix:** This is a built-in module. If this error occurs, your Python installation is corrupted. Reinstall Python.

---

## ⚠️ Legal Disclaimer

**This tool is for educational and authorized testing purposes only.**

- Only scan networks you **own** or have **explicit permission** to test
- Unauthorized port scanning may be illegal in your jurisdiction
- The authors are not responsible for misuse of this tool
- Always follow responsible disclosure practices

---

## 🤝 Contributing

Found a bug or want to add a feature?

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Push and create a Pull Request

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 🙋 Need Help?

- **Open an Issue**: https://github.com/Omkar409/network-recon-tool/issues
- **Star this repo** if you found it useful! ⭐

**Happy Hacking! 🛡️**
