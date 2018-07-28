from tkinter import *


def cali_tax(netProfit):
    if netProfit < 7850:
        return netProfit * 0.99
    elif netProfit < 18610:
        return (netProfit - 7850) * 0.98 + 7850 * 0.99
    elif netProfit < 29372:
        return (netProfit - 18610) * 0.96 + (18610 - 7850) - 0.98 + 7850 * 0.99
    elif netProfit < 40773:
        return (netProfit - 29372) * 0.94 + (29372 - 18610) * 0.96 + (18610 - 7850) - 0.98 + 7850 * 0.99
    elif netProfit < 51530:
        return (netProfit - 40773) * 0.92 + (40773 - 29372) * 0.94 + (29372 - 18610) * 0.96 + (
                18610 - 7850) - 0.98 + 7850 * 0.99
    elif netProfit < 263222:
        return (netProfit - 51530) * (1 - .093) + (51530 - 40773) * 0.92 + (40773 - 29372) * 0.94 + (
                29372 - 18610) * 0.96 + (18610 - 7850) - 0.98 + 7850 * 0.99
    elif netProfit < 315866:
        return (netProfit - 263222) * (1 - 0.103) + (263222 - 51530) * (1 - .093) + (51530 - 40773) * 0.92 + (
                40773 - 29372) * 0.94 + (29372 - 18610) * 0.96 + (18610 - 7850) - 0.98 + 7850 * 0.99
    elif netProfit < 526443:
        return (netProfit - 315866) * (1 - 0.113) + (315866 - 263222) * (1 - 0.103) + (263222 - 51530) * (1 - .093) + (
                51530 - 40773) * 0.92 + (40773 - 29372) * 0.94 + (29372 - 18610) * 0.96 + (
                       18610 - 7850) - 0.98 + 7850 * 0.99
    elif netProfit >= 526443 and netProfit >= 1000000:
        return (netProfit - 526443) * (1 - 0.133) + (526443 - 315866) * (1 - 0.113) + (315866 - 263222) * (
                1 - 0.103) + (263222 - 51530) * (1 - .093) + (51530 - 40773) * 0.92 + (40773 - 29372) * 0.94 + (
                       29372 - 18610) * 0.96 + (18610 - 7850) - 0.98 + 7850 * 0.99


def print_info(income,after_taxes):
    amt_fed_taxed = income - after_taxes
    print("You pay ${} in taxes".format(round(amt_fed_taxed)))
    after_cali = cali_tax(income)
    cali_loss = income - after_cali
    final_income = after_taxes - cali_loss
    print("California will tax ${} on top of that".format(round(cali_loss)))
    print("After Fed Income Tax: ${}".format(round(after_taxes)))
    print("After Cali income tax: ${}".format(round(final_income)))
    percent_Fed_Taxed = round((amt_fed_taxed / income) * 100, 1)
    print("Considering only federal income tax, you lost {}% of your income".format(percent_Fed_Taxed))
    percent_cali_taxed = round(((amt_fed_taxed + cali_loss) / income) * 100, 1)
    print("Considering Cali Tax as well, you lost {}% of your income,".format(percent_cali_taxed))
    print("Total Percent of Cali tax is {}%".format(round(percent_cali_taxed-percent_Fed_Taxed,1)))


while True:
    income = float(input("Enter income:"))

    if str(int(income)) == "0":
        break
    elif 9525 > income:
        after_taxes = income * 0.9
        print_info(income,after_taxes)
    elif income < 38700:
        after_taxes = (income - 9525) * 0.88 + 9525.0 * 0.9
        print_info(income,after_taxes)
    elif income < 82500:
        after_taxes = (income - 38700) * 0.78 + (38700 - 9525) * 0.88 + 9525 * 0.9
        print_info(income,after_taxes)
    elif income < 157500:
        after_taxes = (income - 82500) * 0.76 + (82500 - 38700) * 0.78 + (38700 - 9525) * 0.88 + 9525 * 0.9
        print_info(income,after_taxes)
    else:
        after_taxes = (income - 157500) * 0.72 + (157500 - 82500) * 0.76 + (82500 - 38700) * 0.78 + (
                38700 - 9525) * 0.88 + 9525 * 0.9
        print_info(income,after_taxes)

    print("")

