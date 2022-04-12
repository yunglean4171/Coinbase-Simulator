from urllib import response
import requests
import json
import matplotlib.pyplot as plt
import os.path

file_path = os.path.abspath(os.path.dirname(__file__))
cfgpath = f"{file_path}/config.json"

class cryptothings:
    def returncrypto():
        with open(cfgpath, "r") as cfg:
            data = json.load(cfg)
        return data["crypto"]

    def returnentrythreshold():
        with open(cfgpath, "r") as cfg:
            data = json.load(cfg)
        return data["entryprice"]

    def returnsellthreshold():
        with open(cfgpath, "r") as cfg:
            data = json.load(cfg)
        return data["sellthreshold"]

    def getprice():           
        response = requests.get(f"https://api.coinbase.com/v2/prices/{cryptothings.returncrypto()}-USD/sell").text
        response_info = json.loads(response)
        return float(response_info["data"]["amount"])

    def getbuyprice():
        response = requests.get(f"https://api.coinbase.com/v2/prices/{cryptothings.returncrypto()}-USD/buy").text
        response_info = json.loads(response)
        cryptoprice = response_info["data"]["amount"]
        return cryptoprice
        

class plotthings:
    def iflogsexists():
        if os.path.exists(file_path + "/price.log"):
            os.remove(file_path + "/price.log")
        if os.path.exists(file_path + "/profit.log"):
            os.remove(file_path + "/profit.log")

    def profitlog(profit, timestamp):
        f = open(f"{file_path}/profit.log", "a")
        f.write(f"{profit} {timestamp}\n")
        f.close()

    def pricelog(price, timestamp):
        f = open(f"{file_path}/price.log", "a")
        f.write(f"{price} {timestamp}\n")
        f.close()     

    def createplot():
        profit = []
        ptime = []
        price = []
        prtime = []

        with open(file_path + "/profit.log") as my_file:
            for line in my_file:
                a,b = line.split(' ', 1)
                profit.append(a)
                ptime.append(b.replace("\n", ""))

        with open(file_path + "/price.log") as my_file:
            for line in my_file:
                a,b = line.split(' ', 1)
                price.append(a)
                prtime.append(b.replace("\n", ""))

        plt.figure(1, figsize=(15, 7))
        plt.subplot(211)
        plt.plot(ptime, profit, color='red', linestyle='-', label='Profit Plot')
        plt.subplot(212)
        plt.plot(prtime, price, color='red', linestyle=':', label='Price Plot')
        plt.gcf().autofmt_xdate()
        plt.gcf().canvas.set_window_title('Profit & Price Plots')
        plt.show()