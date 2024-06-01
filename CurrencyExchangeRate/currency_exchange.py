import requests
import matplotlib.pyplot as plt
import datetime

def get_current_exchange_rate(currency_code):
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][0]['mid']
        return rate
    else:
        return f"Error fetching data: {response.status_code}"


def get_historical_exchange_rate(currency_code, days):
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/{start_date}/{end_date}/?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = [rate['mid'] for rate in data['rates']]
        dates = [rate['effectiveDate'] for rate in data['rates']]
        return dates, rates
    else:
        return [], []


def plot_exchange_rate(dates, rates, currency_code):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o')
    plt.title(f"Exchange Rate of {currency_code} to PLN over Time")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate (PLN)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("\nOptions:")
        print("1. Get current exchange rate")
        print("2. Get historical exchange rate")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            currency_code = input("Enter the currency code (e.g., USD, EUR): ").upper()
            rate = get_current_exchange_rate(currency_code)
            if isinstance(rate, float):
                print(f"The current exchange rate for {currency_code} to PLN is {rate:.2f} PLN")
            else:
                print(rate)

        elif choice == '2':
            currency_code = input("Enter the currency code (e.g., USD, EUR): ").upper()
            days = int(input("Enter the number of days for historical data: "))
            dates, rates = get_historical_exchange_rate(currency_code, days)
            if dates and rates:
                plot_exchange_rate(dates, rates, currency_code)
            else:
                print("Error fetching historical data.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()