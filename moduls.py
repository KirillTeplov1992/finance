import investpy

# Для пары доллар-рубль USDRUB
def get_currency(pair):
	search_result = investpy.search_quotes(text = pair,
                                        products = ['currencies'],
                                        countries = ['RUSSIA'],
                                        n_results = 1)

	information = search_result.retrieve_information()	

	return information["prevClose"]

def get_price_of_stock(ticker):
	search_result = investpy.search_quotes(text = ticker,
                                        products = ['stocks'],
                                        countries = ['russia'],
                                        n_results = 1)

	information = search_result.retrieve_information()	

	return information["prevClose"]


def get_price_of_etf(ticker):
	search_result = investpy.search_quotes(text = ticker,
                                        products = ['etfs'],
                                        countries = ['russia'],
                                        n_results = 1)

	information = search_result.retrieve_information()	

	return information["prevClose"]

def get_price_of_fstock(ticker):
	search_result = investpy.search_quotes(text = ticker,
                                        products = ['stocks'],
                                        countries = ['united states'],
                                        n_results = 1)

	information = search_result.retrieve_information()	

	return information["prevClose"]