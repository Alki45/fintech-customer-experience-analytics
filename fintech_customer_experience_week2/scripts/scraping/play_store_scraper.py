from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import logging

# Logging setup
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ✅ Apps listed in the challenge
apps = {
    'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
    'Dashen Bank': 'com.dashen.dashensuperapp',
    'Bank of Abyssinia': 'com.boa.boaMobileBanking',
}

def scrape_reviews(bank_name, app_id):
    logging.info(f"🔄 Fetching reviews for {bank_name}...")

    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=500,
            filter_score_with=None
        )

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"data/raw/{bank_name.replace(' ', '_')}_reviews_{timestamp}.csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
            writer.writeheader()

            for entry in result:
                writer.writerow({
                    'review_text': entry['content'],
                    'rating': entry['score'],
                    'date': entry['at'].strftime('%Y-%m-%d'),
                    'bank_name': bank_name,
                    'source': 'Google Play'
                })

        logging.info(f"✅ Saved {len(result)} reviews to {filename}")
        print(f"✅ {bank_name}: {len(result)} reviews saved to {filename}")

    except Exception as e:
        logging.error(f"❌ Error for {bank_name}: {e}")
        print(f"❌ Error fetching reviews for {bank_name}: {e}")

# Run scraping for all apps
for bank, app_id in apps.items():
    scrape_reviews(bank, app_id)
