def TzWccS1PizzaSellerHaveChange(bills):
    count_of_five = bills.count(5) 
    count_other = bills.count(10) + bills.count(20)

    if bills[0] == 5:
        if count_of_five >= count_other // 2:
            return True
        else:
            return False
    else:
        return False
