# Wuzzuf Jobs Deep Scraper 🚀

### Project Overview
A sophisticated **Python-based** web scraping tool designed to extract detailed job information from **Wuzzuf**. Unlike basic scrapers, this tool performs **Deep Scraping** by navigating into each individual job listing to capture comprehensive data that isn't available on the search results page.

### Key Features
*   **Deep Extraction:** Automatically visits each job URL to fetch detailed specifications.
*   **Salary Insights:** Specifically designed to target and extract salary data (where disclosed).
*   **Structured Data:** Exports all scraped information into organized **CSV** or **Excel** formats for immediate analysis.
*   **Pagination Logic:** Seamlessly navigates through multiple result pages to gather large datasets.

### Tech Stack
*   **Python 3.x**
*   **BeautifulSoup4 / Selenium** (for dynamic content handling)
*   **Requests** (for HTTP networking)
*   **Pandas** (for data manipulation and export)

### How It Works
1. **Clone the repository:** `git clone [Your-Repo-Link]`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the scraper:** `python main.py`
4. **View results:** Check the generated `.csv` file for the extracted data.

### Disclaimer
This project was developed for educational purposes. Please ensure compliance with the website's `robots.txt` policy and terms of service before use.
