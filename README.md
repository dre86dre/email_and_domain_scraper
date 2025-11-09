# Email & Domain Scraper

A simple, beginner-friendly Python script example that demonstrates how to scrape emails and domains from a webpage and save results to a CSV file. 
**This repository is for learning and testing only** — it uses safe practice targets like [ScrapePark.org](https://scrapepark.org) that are designed for scraping practice.

---

## Features

- Fetches page HTML using `requests`.
- Parses HTML with `BeautifulSoup`.
- Extracts emails and domains using regular expressions.
- Saves results to `CSV`.

---

## Safety

**Important:** Scraping websites without permission can violate terms of service and privacy laws (e.g. GDPR). **Do not** use this script to collect personal data from websites you do not own or have explicit permission to scrape. Use it on:
- your own sites
- official APIs
- or public sandbox sites designed for scraping practice (e.g. [ScrapePark.org](https://scrapepark.org), [scrapethissite.com](https://www.scrapethissite.com)).

---

## Requirements

- Python 3.8+ recommended
- Packages:
  - `requests`
  - `beautifulsoup4`
 
---

## Installation

1. Clone the repo:

```
git clone https://github.com/dre86dre/email_and_domain_scraper.git
cd email_and_domain_scraper
```

2. (Optional) Create and activate a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

---

## Usage

The repository contains a the script, `email_and_domain_scraper.py`. To run it:

```
python email_and_domain_scraper.py
```

for the example, the script targets a safe practice URL:

```
url = "https://scrapepark.org/"
```

If you want to run the script against a different page you own or have permission to scrape, change the `url` variable in the script.

After running, the script will print found emails/domains to the console and write them to `scraped_results.csv`.

---

