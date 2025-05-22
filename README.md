# Socket String Sender Tool

A simple TCP socket-based sender script that continuously sends custom string payloads to a target IP and port. Useful for load testing, debugging socket servers, or experimentation.

## ⚙️ Features

- Repeated string payload construction and sending
- Auto-growing payload size
- Wizard (interactive) mode
- Command-line argument support via `optparse`

---

## 🚀 Usage

### 📦 Run with Command-Line Arguments

```bash
python socket_sender.py -i <repeat_count> -s <start_string> -t <repeat_string> -a <ip_address> -p <port>
