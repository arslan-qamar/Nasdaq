# Nasdaq Listings Web Crawler and Notifier

This project is a web crawler that scrapes Nasdaq-listed company data from the [Market Index](https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true) website. It periodically fetches new listings and stores them in a database. If new listings are found, a notification is sent to a Telegram bot chat.

## Features

- Scrapes Nasdaq-listed companies from the Market Index website.
- Stores fetched data in a MongoDB database.
- Periodically checks for newly listed companies.
- Sends notifications via a Telegram bot when a new listing is detected.
- Automated execution using GitHub Actions.

## Technologies Used

- **Python** (Primary programming language)
- **Requests** (For HTTP requests)
- **MongoDB** (For storing Nasdaq listings data)
- **Python-Telegram-Bot** (For sending notifications via Telegram)
- **GitHub Actions** (For automating data fetching and notifications)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arslan-qamar/Nasdaq
   cd Nasdaq
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   export bot_token="your_telegram_bot_token"
   export bot_chatid="your_telegram_chat_id"
   export Nasdaq_db="your_mongodb_connection_string"
   ```
4. Run the fetcher script:
   ```bash
   python start_fetcher.py
   ```
5. Run the notifier script:
   ```bash
   python start_notifier.py
   ```

## Project Structure
```
.
├── Ingestion/
│   ├── start_fetcher.py  # Fetches Nasdaq listings and updates DB
│   ├── requirements.txt  # Dependencies for ingestion
├── Notifier/
│   ├── start_notifier.py  # Checks for new listings and notifies Telegram
│   ├── requirements.txt  # Dependencies for notifier
├── storage/
│   ├── storagemanager.py  # Handles MongoDB interactions
├── .github/workflows/
│   ├── fetcher.yml  # GitHub Action for fetching listings
│   ├── notifier.yml  # GitHub Action for notifying Telegram
├── README.md  # Project documentation
└── requirements.txt
```

## GitHub Actions Workflow

### Fetcher Pipeline
- Runs every 4 hours to fetch Nasdaq listings.
- Updates the MongoDB database.

```yaml
on:
  schedule:
    - cron: "0 */4 * * *"
```

### Notifier Pipeline
- Runs every 5 hours to check for new listings.
- Sends notifications to the Telegram bot if a new listing is found.

```yaml
on:
  schedule:
    - cron: "0 */5 * * *"
```

## License
This project is licensed under the MIT License.

## Author
Arslan Qamar - [Nasdaq Listings Web Crawler and Notifier](https://github.com/arslan-qamar/Nasdaq)

---

Feel free to modify and expand the project as needed!


