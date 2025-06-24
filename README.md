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

## Step-by-Step Setup

### Clone the repository

```bash
git clone https://github.com/yourusername/html-downloader.git
cd html-downloader
```

### Create and activate virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
```

### Install required dependencies
```bash
pip install -r requirements.txt
```

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/html-downloader.git
cd html-downloader
```

### Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

The HTML Downloader is a command-line tool that processes a CSV file containing URLs and downloads the HTML content of each URL into a specified directory.

### Basic Command

```bash

python html_downloader.py -i urls.csv -o output_directory

```

### Command Line Options

| Option | Description | Required |

|--------|-------------|----------|

| `-i`, `--input` | Input CSV file with URLs (one per line) | Yes |

| `-o`, `--output` | Output directory for HTML files | Yes |

### Example Input File (urls.csv)

Create a CSV file containing the URLs you wish to download. Example:

```csv

https://www.example.com

https://www.wikipedia.org

https://github.com

https://news.ycombinator.com

```

### Output

The tool will create the output directory if it doesn't exist. Each downloaded HTML file will be named based on the sanitized URL. For example:

- `https://www.example.com` → `example_com.html`

- `https://en.wikipedia.org/wiki/Python_(programming_language)` → `en_wikipedia_org_wiki_Python_programming_language.html`

### Sample Run

```

2023-08-15 14:30:22,456 - INFO - Created output directory: /path/to/output_directory

2023-08-15 14:30:22,457 - INFO - Processing 4 URLs from urls.csv

2023-08-15 14:30:25,123 - INFO - [1/4] Saved: example_com.html | Status: 200

2023-08-15 14:30:27,845 - INFO - [2/4] Saved: wikipedia_org.html | Status: 200

2023-08-15 14:30:30,156 - INFO - [3/4] Saved: github_com.html | Status: 200

2023-08-15 14:30:32,478 - INFO - [4/4] Saved: news_ycombinator_com.html | Status: 200

==================================================

PROCESSING SUMMARY:

Total URLs: 4

Successful: 4

Failed: 0

Output directory: /path/to/output_directory

==================================================

```

### Advanced Usage

#### Customizing Filenames

You can modify the `sanitize_filename` function in the code to change how filenames are generated. For example, to keep the TLDs (like .com, .org) in the filename, remove the line that strips them.

#### Adjusting Request Parameters

To customize the HTTP request headers or retry strategy, edit the following sections in the code:

- **Headers**: Look for the `headers` dictionary in the `download_html_from_csv` function.

- **Retry Strategy**: Modify the `create_session` function.




# Feel free to contribute or report issues



