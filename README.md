# Reddit Top Posts Scraper
This project involves scraping the top 100 posts from user-specified subreddits using the Scrapy framework in Python.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements
To install and run this project, you'll require Python<=3.x installed, and also the Scrapy Python library:
- `Scrapy`
- `pandas` (if you're using it for data manipulation)

## Installation
1. Clone this repository: 

```bash
git clone https://github.com/your_username/reddit_scraping_project.git
```

2. Change directory to the project folder:

```bash
cd reddit_scraping_project
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

The requirements.txt file should contain a list of Python libraries that your script and project depend on, and it should be placed in the root directory.

## Usage
After the installation, to start the scraping process, you can run the following command in your terminal:

```bash
scrapy crawl reddit
```
