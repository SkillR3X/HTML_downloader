import requests
import csv
import os
import argparse
import re
import hashlib
import time
import random
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def create_session():
    """Create HTTP session with retry strategy"""
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def sanitize_filename(url):
    """
    Convert URL to safe filename
    """
    clean_url = re.sub(r'^https?://', '', url)
    clean_url = re.sub(r'#.*$', '', clean_url)
    clean_url = re.sub(r'^www\.', '', clean_url)
    clean_url = re.sub(r'\?.*$', '', clean_url)
    clean_url = re.sub(r'[\\/*?:"<>|]', '_', clean_url)
    clean_url = clean_url.rstrip('/')
    
    if len(clean_url) > 180:
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        base = clean_url[:80]
        return f"{base}_{url_hash}"
        
    return clean_url

def download_html_from_url(url, output_folder, session, headers, attempt, total):
    """
    Download and save HTML content from a single URL
    
    Args:
        url: Target URL to download
        output_folder: Directory to save HTML file
        session: HTTP session for making requests
        headers: Request headers
        attempt: Current URL position in processing queue
        total: Total URLs to process
    
    Returns:
        tuple: (success: bool, filename: str, status_code: int)
    """
    try:
        # Generate safe filename
        filename = f"{sanitize_filename(url)}.html"
        filepath = os.path.join(output_folder, filename)
        
        # Skip existing files
        if os.path.exists(filepath):
            logger.info(f"[{attempt}/{total}] Skipping existing: {filename}")
            return True, filename, 0
        
        # Fetch content
        response = session.get(
            url,
            headers=headers,
            timeout=15,
            allow_redirects=True
        )
        response.raise_for_status()
        
        # Save content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        return True, filename, response.status_code
        
    except Exception as e:
        logger.error(f"[{attempt}/{total}] Failed: {url} | Error: {str(e)}")
        return False, url, getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0

def download_html_from_csv(csv_file, output_folder):
    """Download HTML content from URLs in CSV file"""
    # Create output directory
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Created output directory: {os.path.abspath(output_folder)}")
    
    # Read URLs from CSV
    with open(csv_file, 'r', encoding='utf-8') as file:
        urls = [row[0].strip() for row in csv.reader(file) if row and row[0].strip()]
    
    if not urls:
        logger.error("No valid URLs found in input file")
        return
        
    logger.info(f"Processing {len(urls)} URLs from {csv_file}")
    
    # Create HTTP session and headers
    session = create_session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    # Process each URL
    success_count = 0
    for i, url in enumerate(urls, 1):
        success, filename, status_code = download_html_from_url(
            url=url,
            output_folder=output_folder,
            session=session,
            headers=headers,
            attempt=i,
            total=len(urls)
        )
            
        if success:
            success_count += 1
            logger.info(f"[{i}/{len(urls)}] Saved: {filename} | Status: {status_code}")
            
            # Polite delay between requests
            time.sleep(random.uniform(0.5, 1.5))
    
    # Generate summary report
    logger.info("\n" + "="*50)
    logger.info(f"PROCESSING SUMMARY:")
    logger.info(f"Total URLs: {len(urls)}")
    logger.info(f"Successful: {success_count}")
    logger.info(f"Failed: {len(urls) - success_count}")
    logger.info(f"Output directory: {os.path.abspath(output_folder)}")
    logger.info("="*50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='HTML Downloader: Fetch and save web content from URLs in CSV file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--input', 
                        required=True, 
                        help='Input CSV file containing URLs (one per line)')
    parser.add_argument('-o', '--output', 
                        required=True, 
                        help='Output directory for HTML files')
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.isfile(args.input):
        logger.error(f"Input file not found: {args.input}")
        exit(1)
    
    download_html_from_csv(args.input, args.output)