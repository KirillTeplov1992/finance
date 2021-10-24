from moduls import*
import pandas as pd
import matplotlib.pyplot as plt 
import okama as ok


data_about_stocks = [{"Акция": "Сбербанк","Цена": get_price_of_stock("SBER"), "Количество": 150, "Стоимость": 0, "Доля": 0},
					 {"Акция": "ВТБ", "Цена": get_price_of_stock("VTBR"), "Количество": 900000, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Магнит", "Цена": get_price_of_stock("MGNT"), "Количество": 10, "Стоимость": 0, "Доля": 0},
					 {"Акция": "МТС", "Цена": get_price_of_stock("MTSS"), "Количество": 180, "Стоимость": 0, "Доля": 0},
					 {"Акция": "FXCN", "Цена": get_price_of_etf("FXCN"), "Количество": 14, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Россети", "Цена": get_price_of_stock("RSTI"), "Количество": 5000, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Россети-п", "Цена": ok.Asset("RSTIP.MOEX").price, "Количество": 4000, "Стоимость": 0, "Доля": 0},
					 {"Акция": "РосГидро", "Цена": get_price_of_stock("HYDR"), "Количество": 35000, "Стоимость": 0, "Доля": 0},
					 {"Акция": "FXIT", "Цена": get_price_of_etf("FXIT"), "Количество": 6, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Московская биржа", "Цена": get_price_of_stock("MOEX"), "Количество": 60, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Газпром", "Цена": get_price_of_stock("GAZP"), "Количество": 180, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Башнефть-п", "Цена": ok.Asset("BANEP.MOEX").price, "Количество": 57, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Сбербанк-п", "Цена": ok.Asset("SBERP.MOEX").price, "Количество": 50, "Стоимость": 0, "Доля": 0},
					 {"Акция": "ОГК-2", "Цена": get_price_of_stock("OGKB"), "Количество": 22000, "Стоимость": 0, "Доля": 0},
					 {"Акция": "НЛМК", "Цена": get_price_of_stock("NLMK"), "Количество": 70, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Северсталь", "Цена": get_price_of_stock("CHMF"), "Количество": 16, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Татнефть", "Цена": ok.Asset("TATNP.MOEX").price, "Количество": 110, "Стоимость": 0, "Доля": 0},
					 {"Акция": "АФК-Система", "Цена": get_price_of_stock("AFKS"), "Количество": 1400, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Немецкие акции", "Цена": get_price_of_etf("FXDE"), "Количество": 1500, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Аэрофлот", "Цена": get_price_of_stock("AFLT"), "Количество": 150, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Carnival", "Цена": get_price_of_fstock("CCL")*get_currency("USDRUB"), "Количество": 37, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Bank of America", "Цена": get_price_of_fstock("BAC")*get_currency("USDRUB"), "Количество": 22, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Veon", "Цена": get_price_of_fstock("VEON")*get_currency("USDRUB"), "Количество": 224, "Стоимость": 0, "Доля": 0},
					 {"Акция": "TCS Group", "Цена": get_price_of_stock("TCS"), "Количество": 24, "Стоимость": 0, "Доля": 0},
					 {"Акция": "MTS PJSC", "Цена": get_price_of_fstock("MBT")*get_currency("USDRUB"), "Количество": 1, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Американские акции", "Цена": get_price_of_etf("VTBA"), "Количество": 260, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Акции развивающихся стран", "Цена": get_price_of_etf("VTBE"), "Количество": 330, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Евро облигации", "Цена": get_price_of_etf("VTBU"), "Количество": 560, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Американские облигации", "Цена": get_price_of_etf("VTBH"), "Количество": 470, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Российские акции", "Цена": get_price_of_etf("VTBX"), "Количество": 1, "Стоимость": 0, "Доля": 0},
					 {"Акция": "Российские облигации", "Цена": get_price_of_etf("VTBB"), "Количество": 3, "Стоимость": 0, "Доля": 0}]

amount = [{"Стоимость": data_about_stocks[i]["Количество"]*data_about_stocks[i]["Цена"]} for i in range(len(data_about_stocks))]

capital=0
for x in amount:
	capital+=x["Стоимость"]

for i in range(len(data_about_stocks)):
	data_about_stocks[i]["Стоимость"]=amount[i]["Стоимость"]
	data_about_stocks[i]["Доля"]=round((data_about_stocks[i]["Стоимость"]/capital)*100, 2)	

labels = []
value = []
for i in data_about_stocks:
	labels.append(i["Акция"])
	value.append(i["Доля"])
	
main_frame = pd.DataFrame(data_about_stocks)

print(main_frame)
print("Совокупная стоимость: "+ str(round(capital,2))+" р")

fig = plt.figure()
ax = fig.add_subplot()

ax.pie(value, labels = labels, autopct = "%.2f")
ax.grid()
plt.show()