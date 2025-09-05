# 🔑 Log-Track 

**Log-Track** is a **basic keystroke logger** built in Python using the [`pynput`](https://pypi.org/project/pynput/) library.
It records keyboard inputs and saves them into a text file (`klog.txt`).

⚠️ **Disclaimer:**
This project is created **only for educational and research purposes**.

* It is intended to demonstrate how keystroke logging works in a **controlled environment**.
* Do **not** use this on any system without the **explicit consent** of the owner.
* Unauthorized use of keyloggers is **illegal** and may lead to serious legal consequences.
* Designed for **cybersecurity training, research, and demo projects**.
* Only run on your **own machine** or in a **virtual lab environment**.
* Any misuse of this tool is **strictly prohibited**.

## 🛠️ Prerequisites

### 1. Install Python

You need **Python 3.7+** installed.

* [Download Python](https://www.python.org/downloads/)
* Verify installation:

  ```bash
  python --version
  ```

  or

  ```bash
  python3 --version
  ```

### 2. Install pip (if not installed)

Check if pip is installed:

```bash
pip --version
```

If missing, follow this guide: [Install pip](https://pip.pypa.io/en/stable/installation/).

### 3. Install Required Library (`pynput`)

Install with:

```bash
pip install pynput
```

Docs: [pynput Documentation](https://pynput.readthedocs.io/en/latest/)


## 🚀 How to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/Log-Track.git
   cd Log-Track
   ```

2. **Verify script file exists:**
   The main script is named **`monitor.py`**.

3. **Run the program:**

   ```bash
   python monitor.py
   ```

   or (depending on your system):

   ```bash
   python3 monitor.py
   ```

4. **Check the output file:**
   Keystrokes will be saved in **`klog.txt`** (same folder).

   * Linux/macOS:

     ```bash
     cat klog.txt
     ```
   * Windows:

     ```powershell
     notepad klog.txt
     ```


## 🛑 How to Stop the Program

Since the logger keeps running in the background:

* Press **`CTRL + C`** in the terminal where it is running.
* Or manually kill the process from **Task Manager (Windows)** / **Activity Monitor (macOS)** / `kill` command (Linux).


## 📄 Features

* Logs standard keys (letters, numbers, symbols).
* Handles **special keys** (Space, Enter, Tab, Backspace).
* Ignores **modifier keys** (Shift, Ctrl, Alt).
* Saves keystrokes into `klog.txt`.


