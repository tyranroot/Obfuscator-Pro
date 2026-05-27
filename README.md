![Alt text](https://github.com/tyranroot/Obfuscator-Pro/blob/main/Encoder/logo.png?raw=true)

### ⚡ MILITARY-GRADE PYTHON CODE PROTECTION SYSTEM ⚡

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Versions" />
  </a>
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-darkgreen?style=for-the-badge" alt="Platforms" />
  <img src="https://img.shields.io/badge/Security-Obfuscated%20%26%20Packed-red?style=for-the-badge&logo=spyderide" alt="Security" />
  <a href="#license">
    <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge" alt="License" />
  </a>
</p>

</div>

---

# 🚀 ENCODER

**Encoder** is a professional, lightweight, and high-performance **Python Code Obfuscator, Compressor, and Packager**. It is explicitly designed for developers, security researchers, and software publishers to protect sensitive intellectual property, proprietary script files, and key assets from decompilation, simple reverse engineering, and code tampering.

By leveraging a dynamic, multi-layered security pipeline combining **System-Native Marshal Serializations**, **High-Ratio Zlib Compressions**, and **Base64 Payload Encoding**, **Encoder** renders your `.py` scripts entirely unreadable while preserving standard interpreter speed and performance.

---

## 🔥 Key Features

* **🌀 System-Native Marshal Packing:** Compiles and serializes the script's AST directly into raw Python bytecode via the native `marshal` module, severely disrupting standard decompilation attempts (e.g. `uncompyle6`, `decompyle++`).
* **📦 High-Ratio Zlib Compression:** Compresses compiled binary structures using deep level-9 recursive `zlib` dictionaries, minimizing the protected script block file size while scrambling original source sequences.
* **🛡️ Base64 Encoding Armor:** Safely encapsulates intermediate compressed byte representations using robust, platform-neutral `base64` character arrays to prevent text corruption across diverse systems.
* **🛑 Anti-Tamper Checksums:** Optionally injects embedded digital hash validations. If an encoded file is edited by even a single byte or executed under a standard attached debugger, it instantly alerts of violation and terminates execution.
* **⚡ Zero-Overlay Execution:** Designed to unpack and load all bytecode structures directly into standard internal server memory, maintaining zero performance lag or file-system reads during launches.
* **🌐 Universal OS Compatibility:** Compiled packages require nothing but a standard Python interpreter to execute flawlessly across Windows, Linux, and macOS.

---


---

## ⚙️ Quick Installation

### Prerequisites
* **Python 3.8 or higher** is recommended.
* Standard system modules (`base64`, `zlib`, `marshal`) are pre-built into Python.

### Step-by-Step Installation
Clone the repository and jump right into the workspace directory:

```bash

git clone https://github.com/tyranroot/Obfuscator-Pro.git

cd Obfuscator-Pro

```

---

## 📖 Complete Usage Guide

Running `Encoder` is incredibly straightforward. Simply invoke the script with python and supply the relative or absolute path of your target Python code.

### Standard Usage

```bash
python3 obfuscator.py /file path.py
```

For paths containing spaces or specialized directories:

```bash
python3 obfuscator.py /home/your user/your script file.py
```

---

## 🛠️ Advanced Integration (Command Options)

Extend the packing engine configurations by passing additional command-line parameters to customize the obfuscation depth:

| Flag | Argument | Description | Default |
|:---|:---|:---|:---|
| `-o`, `--output` | `[FILENAME]` | Manually declare the output file destination. | `[original]_encoded.py` |
| `-i`, `--iterations`| `[INT]` | Run multiple passes of the obfuscation array (1-5 layers). | `2` |
| `--no-compress` | *None* | Disables the internal zlib compression layer. | `False` |
| `--no-tamper` | *None* | Disables the integrity checksum and anti-analysis shield. | `False` |

### Premium CLI Custom Commands
```bash
# Force 4-passes of serializations and output to a custom location
python3 obfuscator.py /home/your user/file name.
```

---

## 🧩 Architectural Flow (How it Works)

The logic structure of the encoding and decapsulation cycle represents standard modern cybersecurity designs:

```text
┌─────────────────────────┐
│     Source Code (.py)   │  <-- Standard readable code
└────────────┬────────────┘
             │
             ▼  [Stage 1: AST Pre-processing]
┌─────────────────────────┐
│ Clean AST Parsing       │  <-- Stripping out developer comments & docstrings
└────────────┬────────────┘
             │
             ▼  [Stage 2: Bytecode Packing]
┌─────────────────────────┐
│ `marshal` Serializer    │  <-- Serializes AST to native Python binary structures
└────────────┬────────────┘
             │
             ▼  [Stage 3: Data Scrambling]
┌─────────────────────────┐
│ `zlib` Level-9 Compress │  <-- High-density recursive dictionary compression
└────────────┬────────────┘
             │
             ▼  [Stage 4: Binary Armor]
┌─────────────────────────┐
│ `base64` Encoder        │  <-- Formats binary bits into safe ASCII string characters
└────────────┬────────────┘
             │
             ▼  [Stage 5: Self-Loading Assembly]
┌─────────────────────────┐
│ Loader Guard Wrapper    │  <-- Generates dynamically decoding __exec__ block
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Encoded Source (.py)   │  <-- Final distributed secure file
└─────────────────────────┘
```

---

## ❓ Frequently Asked Questions

#### Q1: Does the encoded code require dependencies to execute?
**No.** The resulting encoded script handles all decryption, unpacks, compiles, and loads variables fully in-memory utilizing only standard built-in Python core libraries: `base64`, `zlib`, and `marshal`. No external pip modules are required!

#### Q2: Can the encoded file be executed normally?
**Yes!** You run the final encoded file exactly the same way as your original script using standard Python commands (e.g., `python3 script_encoded.py`).

#### Q3: Is it possible to recover the original code after compilation?
**No.** Obfuscation, bytecode marshalling via `marshal`, multi-pass `zlib` compression, and final base64 parsing strip all readable metadata comments and structural mappings. This makes simple decompilation back into high-fidelity source code practically impossible. Always key backup copies of your source scripts in a private, secure repository!

#### Q4: Does Encoder support Windows path syntax?
**Yes.** Standard Windows escape character formats, single quotes, double quotes, and complex file directions are fully resolved by our robust path parser layer.

---

## 🛡️ License

Distributed under the **MIT License**. See `LICENSE` inside the repository for full license declarations.

---


---
## 👨‍💻 Author
* **Name:** Maruf x ZeroTrace 
* 🐙 GitHub: [@tyranroot](https://github.com/tyranroot/)
* 💬 Telegram: [@marufxzerotrace](https://t.me/marufxzerotrace)
* 📘 Facebook: [Maruf x ZeroTrace](https://www.facebook.com/share/1CDxaGN6p3/)

---

