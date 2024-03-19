# Web Scraper API 🕸️

The Web Scraper API is a Flask application that provides an endpoint to scrape external links from a given URL.

## Features

- 📡 Accepts POST requests with a URL payload.
- 🕵️‍♂️ Scrapes external links from the provided URL.
- 📋 Returns a JSON response with the extracted links.

## Dependencies

- Python 3.x
- Flask
- requests
- BeautifulSoup

## Usage

1. Install Python and required libraries.
2. Clone/download the project files.
3. Run the Flask application using `python Web-Scraping.py`.
4. Send POST requests to `http://127.0.0.1:5000/Scraping` with a JSON payload containing the URL.
5. You can check this api using Postman 

## Endpoint

- `/Scraping` (POST): Accepts a JSON payload with a URL field and returns external links.

## Contributing

👩‍💻 Contributions welcome! Feel free to open issues or submit pull requests to suggest improvements or report bugs.

