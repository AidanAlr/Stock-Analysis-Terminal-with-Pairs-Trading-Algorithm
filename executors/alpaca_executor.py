import os
import sys

from utils.formatting_and_logs import blue_bold_print

# Get the directory of the current script
# If the script is not in the root directory, navigate to the root directory
# Append the root directory to sys.path so that modules can be imported
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from trading.alpaca_functions import Alpaca


def live_position_menu(alpaca: Alpaca):
    try:
        blue_bold_print("Current Positions - Live Portfolio")
        alpaca.live_profit_monitor(15)
    except Exception as e:
        print(e)


def manual_trade_menu(alpaca: Alpaca):
    try:
        blue_bold_print("Manual Trade Selected")
        blue_bold_print("To place a trade, please enter the following information:")
        order_type = input("Type (market/limit): ")
        symbol = input("Symbol: ")
        side = input("Side (buy/sell): ")

        while True:
            qty = input("Quantity: ")
            if qty.isnumeric():
                qty = float(qty)
                break

        if order_type == "limit":

            while True:
                limit_price = input("Limit Price: ")
                if limit_price.isnumeric():
                    limit_price = float(limit_price)
                    break

            blue_bold_print("Would you like to add a take profit/stop loss to your order? (y/n)")
            tp_sl_choice = input()
            if tp_sl_choice.lower() == "y":
                blue_bold_print("Please enter the take profit gain (Enter 1.05 for 5% tp) : ")
                tp = input()
                tp_price = limit_price * float(tp)
                blue_bold_print("Please enter the stop loss loss (Enter 0.95 for 5% sl) : ")
                sl = input()
                sl_price = limit_price * float(sl)

                alpaca.send_limit_order(symbol, qty, side, limit_price, stop_loss=sl_price, take_profit=tp_price)
            else:
                alpaca.send_limit_order(symbol, qty, side, limit_price)

        elif order_type == "market":
            alpaca.send_market_order(symbol, qty, side)

    except Exception as e:
        print(e)

