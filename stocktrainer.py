# Importing libraries needed to use api, date data, saving variable, and pathing.
from alpha_vantage.timeseries import TimeSeries
from datetime import date, timedelta
import pickle
from os import path

# Uses the API Key to request stock data with the stock symbol
key = 'SHBRA075RSEB7YVF'
ts = TimeSeries(str(key))

# Gets today's date to use for current stock info
def get_date():
    n = 3
    return date.today() - timedelta(days=n)

# Prompts user for the stock symbol they would like to invest in.
def ask_for_symbol():
    ask_for_symbol.user_symbol = str(input('What stock symbol? (without $)')).upper()

#Gets the daily open and closing price of that stock.
def get_daily(stock_symbol):
    sym, meta = ts.get_daily(symbol=stock_symbol)
    raw_data = str(sym[str(get_date())])
    get_daily.data = raw_data.split("'")

# Asks user for how many stocks they want to invest,
def start():
    start.input_start = int(input("How many stocks?"))

# Creates variables to hold the open and close price of the selected stock.
def get_openclose():
    get_openclose.stock_open = float(get_daily.data[3])
    get_openclose.stock_close = float(get_daily.data[15])

# Creates variables to hold how much money (stock price * stock volume)
def calc_real_money(stock_volume):
    calc_real_money.portfolio_start = get_openclose.stock_open * stock_volume
    calc_real_money.portfolio_end = get_openclose.stock_close * stock_volume

# Prints the portfolio value and then finds the difference between the start and end.
def print_net_gainz():
    print(calc_real_money.portfolio_start, calc_real_money.portfolio_end)
    print_net_gainz.net_gainz = calc_real_money.portfolio_end - calc_real_money.portfolio_start
    print(print_net_gainz.net_gainz)

# Adds the net to a file.
def net_file():
    f = open("Dayrate.txt", "a")
    f.write("Your net for " + str(get_date()) + " is " + str(print_net_gainz.net_gainz) + "\n")
    f.close()

# Goes through each function above this line
def first_time_run():
    ask_for_symbol()
    get_daily(ask_for_symbol.user_symbol)
    start()
    get_openclose()
    calc_real_money(start.input_start)
    print_net_gainz()
    net_file()

# If statement that tests if the file that is created after first run is there, then it goes through
# different processes depending on the outcome
if path.exists('Dayrate.txt'):
    #Confirms that the path exist, which is only created after you run the program for the first time
    print('IT EXISTS')

    # Opening saved variables from first time run
    pickle_var = open('saved_vars.p', 'rb')
    saved_stock_vol, gainz, saved_symbol = pickle.load(pickle_var)

    # Goes through the normal program again, removing the start function
    get_daily(saved_symbol)
    get_openclose()
    calc_real_money(saved_stock_vol)
    print_net_gainz()
    net_file()
else:
    #Goes through the process of a first time run of the program
    first_time_run()

    #Saving variables that were created
    pickle_var = open('saved_vars.p', 'wb')
    pickle.dump([start.input_start, print_net_gainz.net_gainz, ask_for_symbol.user_symbol], pickle_var)
    pickle_var.close()




