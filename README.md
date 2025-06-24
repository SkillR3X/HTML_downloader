# HTML Downloader

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A robust command-line tool for downloading and archiving HTML content from multiple URLs listed in a CSV file. Designed for web scraping, content archiving, and SEO analysis workflows.

## Key Features

- 🚀 **Batch Processing** - Download hundreds of web pages in a single run
- 🔁 **Smart Retry Logic** - Automatic retries for failed requests with exponential backoff
- 📁 **Intelligent Filenames** - URL-based naming with sanitization for filesystem safety
- 📊 **Detailed Logging** - Comprehensive progress tracking with success/failure reporting
- ⏱️ **Rate Limiting** - Polite delays between requests to avoid overwhelming servers
- ✅ **Resume Capability** - Skips already downloaded files for efficient re-runs

## Use cases

- SEO Analysis - Archive competitor websites for content analysis

- Web Archiving - Preserve historical versions of important web pages

- Research Projects - Collect data for academic studies

- Content Migration - Download pages before site redesigns

- Monitoring - Regularly capture snapshots of key pages

## Usage

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/html-downloader.git
cd html-downloader

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

### Feel free to contribute or report issues

```

