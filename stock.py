import numpy as np
import yfinance as yf

class Stock:
    def __init__(self, stockName):
        self.name = stockName
        self.data = yf.Ticker(self.name).history(period="1y")
    def fetchData(self):
        close = np.array(self.data['Close'])
        dividends =  np.array(self.data['Dividends'])
        yearlyReturn = (((close[-1] - close[0])+ np.sum(dividends))/close[0])*100
        dailyReturn = np.array((np.diff(close)+dividends[:-1])/close[:-1])
        volatility  = np.std(dailyReturn)
        avgDailyReturn = np.mean(dailyReturn)
        maxDailyReturn = np.max(dailyReturn)
        minDailyReturn = np.min(dailyReturn)
        totalDividends = np.sum(dividends)
        dailyReturn = np.round(dailyReturn*100, 2)

        fullData = {"close":close, "dividends":totalDividends, "yearlyReturn": yearlyReturn, "dailyReturn": dailyReturn,
                     "volatility" : volatility,  "avgDailyReturn": avgDailyReturn*100, "maxDailyReturn": maxDailyReturn*100
                      , "minDailyReturn": minDailyReturn*100 }
        return fullData
def displayMenu():
    print("\nMenu:")
    print("1. Show Yearly Return")
    print("2. Show Daily Returns")
    print("3. Show Average Daily Return")
    print("4. Show Total Dividends")
    print("5. Show Max Daily Return")
    print("6. Show Min Daily Return")
    print("7. Show Volatility")
    print("8. Change stock")
    print("9. show summary report")
    print("10. Exit")


print("Welcome to the Stock Analysis Program!")
ticker =input("Enter ticker symbol (or press Enter for AAPL)  use .ns at the end for indian stocks: ") or "AAPL"

choice = 1
stock = Stock(ticker.upper())
stockData = stock.fetchData()

while choice != 9:
    displayMenu()
    choice = int(input("enter your choice [1-9]: "))
    if choice == 1:
        print(f"yearly returns are {stockData["yearlyReturn"]:.2f}%")
    elif choice == 2:
        print(f"daily returns are {stockData["dailyReturn"]}")
    elif choice == 3:
        print(f"Average daily returns are {stockData["avgDailyReturn"]:.2f}%")
    elif  choice == 4:
        print(f"total dividends are {stockData["dividends"]}")
    elif choice == 5:
        print(f"Max daily return is {stockData['maxDailyReturn']:.2f}%")
    elif choice == 6:
        print(f"Min daily return is {stockData['minDailyReturn']:.2f}%")
    elif choice == 7:
        print(f"Volatility: {np.round(stockData['volatility']*100, 2)}%")
    elif choice == 8:
        ticker = input("Enter new ticker symbol (or press Enter for AAPL): ") or "AAPL"
        stock = Stock(ticker.upper())
        stockData = stock.fetchData()
        print("Stock data updated.")
    elif choice == 9:
        print("Summary Report:")
        print(f"Ticker: {ticker.upper()}")
        print(f"Yearly Return: {stockData['yearlyReturn']:.2f}%")
        print(f"Total Dividends: ${stockData['dividends']:.2f}")
        print(f"Average Daily Return: {stockData['avgDailyReturn']:.2f}%")
        print(f"Max Daily Return: {stockData['maxDailyReturn']:.2f}%")
        print(f"Min Daily Return: {stockData['minDailyReturn']:.2f}%")
        print(f"Volatility: {np.round(stockData['volatility']*100, 2)}%")
    elif choice == 10:
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")
        

