# MCP (Model Control Protocol) Tools

This repository contains a collection of Python-based MCP tools that provide various utilities for security scanning, file management, and data retrieval. These tools are built using the FastMCP framework.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nithishkumar2022020/MCP_Claude.git
cd MCP_Claude
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Available Tools

### 1. Web Vulnerability Scanner (`vul_scanner.py`)
A comprehensive web security scanning tool that checks for various vulnerabilities:
- SQL Injection
- Cross-Site Scripting (XSS)
- Sensitive Information Exposure
- Crawls websites up to a specified depth

Usage:
```python
from vul_scanner import scan_url

# Scan a website for vulnerabilities
result = scan_url("https://example.com")
```

### 2. Data Retriever (`data_retriever.py`)
A tool for extracting and querying content from PDF documents, specifically designed for Gen AI related questions.

Usage:
```python
from data_retriever import fetch_context

# Query the PDF content
response = fetch_context("Tell me about LLMs")
```

### 3. File Counter (`file_counter.py`)
A utility to count the number of files on your desktop.

Usage:
```python
from file_counter import count_desktop_files

# Get the count of files on desktop
result = count_desktop_files()
print(result)  # "There are X files on your desktop."
```

### 4. Conversation Saver (`file_saver.py`)
A tool to save chat conversations to text files on your desktop.

Usage:
```python
from file_saver import save_conversation

# Save a conversation
result = save_conversation("Your conversation content here")
print(result)  # "Conversation saved at: /path/to/file"
```

### 5. Greeter (`greeter.py`)
A simple greeting tool that returns a welcome message.

Usage:
```python
from greeter import greet

# Get a welcome message
message = greet()
print(message)  # "Hey nithish, welcome to MCP!"
```

## Running the Tools

Each tool can be run independently. To start a tool, navigate to its directory and run:

```bash
python <tool_name>.py
```

For example:
```bash
python vul_scanner.py
```

## Security Notes

1. The Web Vulnerability Scanner should only be used on websites you have permission to test.
2. Be careful with sensitive information and API keys.
3. Always review the scan results and verify findings manually.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 