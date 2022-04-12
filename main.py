from datetime import datetime
from functions import *
from colorama import Fore


def main():
    logo = """
 _____       _       _                         
/  __ \     (_)     | |                        
| /  \/ ___  _ _ __ | |__   __ _ ___  ___      
| |    / _ \| | '_ \| '_ \ / _` / __|/ _ \     
| \__/| (_) | | | | | |_) | (_| \__ |  __/     
 \____/\___/|_|_| |_|_.__/ \__,_|___/\___|                                                   
 _____ _                 _       _             
/  ___(_)               | |     | |            
\ `--. _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
 `--. | | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
/\__/ | | | | | | | |_| | | (_| | || (_) | |   
\____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|                                                           
"""

    print(logo)

    plotthings.iflogsexists()

    # Initialize current and previous prices
    current_price = cryptothings.getprice()
    a = cryptothings.returnentrythreshold()
    b = cryptothings.getbuyprice()
    coinsamount = float(a)/float(b)
    last_price = current_price

    print(Fore.CYAN + f"╔ {cryptothings.returncrypto()} price: ${current_price} [0%]")
    print(f"║ {coinsamount} {cryptothings.returncrypto()} has been bought for ${cryptothings.returnentrythreshold()}")
    print(f"╚ Sell price threshold: ${cryptothings.returnsellthreshold()}")
    #print(f"↳ {cryptothings.buytokens()} {cryptothings.returncrypto()} has been bought for ${cryptothings.returnentrythreshold()}")
    baseprice = last_price

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        percent = percentage(current_price, baseprice)
        worthnow = nowworth(percent)
        actualprofit = profit(worthnow)

        if current_price > last_price:
                print(Fore.GREEN + f"\n⬆️  {cryptothings.returncrypto()} price has increased: ${current_price} [{percent}%] - {current_time}")
                print(Fore.WHITE + f"💸 Now worth: ${worthnow}")
                print(f"📈 Profit: ${actualprofit}")
                plotthings.profitlog(actualprofit, current_time)
                plotthings.pricelog(current_price, current_time)

        elif current_price < last_price:
                print(Fore.RED + f"\n⬇️  {cryptothings.returncrypto()} price has decreased: ${current_price} [{percent}%] - {current_time}")
                print(Fore.WHITE + f"💸 Now worth: ${worthnow}")
                print(f"📈 Profit: ${actualprofit}")
                plotthings.profitlog(actualprofit, current_time)
                plotthings.pricelog(current_price, current_time)

        if float(actualprofit) + float(cryptothings.returnentrythreshold()) >= float(cryptothings.returnsellthreshold()):
                print(Fore.GREEN + "\n✅ Actual profit has increased over sell price threshold!")
                print(f"➡️ {round(coinsamount, 9)} tokens sold for: ${round(coinsamount * current_price, 2)}")
                plotthings.createplot()
                break

        # Set last_price to current_price, then update current_price
        last_price = current_price
        current_price = cryptothings.getprice()


def delpositive(percent):
    if "+" in str(percent):
        percent = percent.replace("+", "")
    return percent


def profit(wn):
    profit = wn - int(cryptothings.returnentrythreshold())
    return round(profit, 2)


def nowworth(prct):
    if type(prct) == float:
        nowworth = ((prct + 100) * int(cryptothings.returnentrythreshold())) / 100
    else:
        nowworth = ((float(prct.replace("+", "")) + 100) * 1000) / 100
    return nowworth


def percentage(price, bprice):
    formula = ((price * 100) / bprice) - 100
    percentage = round(formula, 2)
    if percentage > 0:
        percentage = f"+{percentage}"
    return percentage


if __name__ == "__main__":
    main()