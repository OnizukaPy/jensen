def beräkning(priset, mom_perc):
    mom = float(mom_perc[:-1])/100

    return priset * (1+mom)

print(beräkning(100, "2%"))