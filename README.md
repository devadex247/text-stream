
# text_stream cli 📊✨

A high-speed CLI text pipeline that ingests raw input, calculates structural text metrics, and streams sanitized data directly back to your Windows or macOS system clipboard.

## Features
- **Instant Metrics:** Tracks word count, sentence count, absolute characters, and reading times.
- **Smart Formatting:** Normalizes extra tabs, duplicate spaces, and messy line breaks into a clean, uniform single-line string.
- **Auto-Clipboard Sync:** Modifies your clipboard instantly with the cleaned text using native OS pipelines (`clip` on Windows / `pbcopy` on macOS).
- **Zero Dependencies:** Built entirely with native Python core modules. No `pip install` required.

## Installation & Setup

1. Clone this repository to your local workspace:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/text_stream-cli.git](https://github.com/YOUR_USERNAME/text_stream-cli.git)
   cd "text_stream cli"
How to Use
Run the utility script using Python in your terminal or PowerShell window:

PowerShell
python text_utility.py
Paste your messy multi-line text directly into the terminal window.

Press Enter to advance to a fresh line.

Send the execution signal to run the analysis:

Windows: Press Ctrl + Z and then hit Enter

Mac / Linux: Press Ctrl + D

Example Output
Plaintext
========================================
 📊 TEXT ANALYSIS RESULTS
========================================
🔹 Words:             42
🔹 Sentences:         3
🔹 Characters (all):  258
🔹 Characters (none): 214
🔹 Est. Reading Time: 13 seconds
----------------------------------------
✨ CLEANED TEXT (Single line, normalized spaces):
   "Your cleanly formatted text preview will appear right here..."
----------------------------------------
📋 Success: Cleaned text has been copied to your clipboard!
========================================



### 🚀 Ready to Commit and Push?

Since you are already inside the folder in PowerShell, you can link this up to GitHub right now by running these four sequential commands:

```powershell
git init
git add .
git commit -m "Initial commit: Added text streaming script and Windows optimised README
