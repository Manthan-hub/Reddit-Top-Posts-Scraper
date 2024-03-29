# Reddit Top Posts Scraper
This project involves scraping the top 100 posts from user-specified subreddits using the Scrapy framework in Python.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements
To install and run this project, you'll require Python<=3.x installed, and also the Scrapy Python library:
- `Scrapy`
- `Python 3.x` 

## Installation
1. Clone this repository: 

```bash
git clone https://github.com/Manthan-hub/Reddit-Top-Posts-Scraper.git
```

2. Change directory to the project folder:

```bash
cd reddit_scraper
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## Usage
After the installation, to start the scraping process, you can run the following command in your terminal:

For JSON Output:

```bash
scrapy crawl reddit -o reddit.json
```

For CSV Output:

```bash
scrapy crawl reddit -o reddit.csv
```
