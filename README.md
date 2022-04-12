# Coinbase-Simulator

![](https://i.imgur.com/zADQ7FF.png)

![](https://i.imgur.com/e97gBDM.png)

![](https://i.imgur.com/X16WCbZ.png)

## Build with:
- [Colorama](https://pypi.org/project/colorama/)
- [Matplotlib](https://matplotlib.org/)
- [Requests](https://pypi.org/project/requests/)

Using Coinbase API (https://api.coinbase.com/) app is checking in real time crypto price changes on market. When profit increases over sell price threshold then app stops and creates plot.

To change crypto data values edit **config.json** file
```json
{
    "crypto": "SOL",
    "entryprice": "1000",
    "sellthreshold" : "1001"
}
```
If you want to simulate different crypto change SOL to any other like BTC, LTC etc.

## Install required packages by running this command:
```
pip3 install -r requirements.txt
```
# Contributing
If you have some ideas that you want to suggest please make a [pull requests](https://github.com/yunglean4171/Coinbase-Simulator/pulls) and if you found some bugs please make an [issue](https://github.com/yunglean4171/Coinbase-Simulator/issues). Every contribution will be appreciated.


