def Tz1NumberOfTicketsICanBuy(ticketPrice, comboPrice, money):
    max_tick = money // ticketPrice
    total_price = 0
    numb_tick = 0
    remainder = money - total_price

    while total_price < money:    
        numb_tick += 1
        total_price += ticketPrice
        if numb_tick % 2 == 0:
            total_price += comboPrice

    return numb_tick - 1
    