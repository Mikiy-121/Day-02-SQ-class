customers = [
    ("Almaz" , 1500),
    ("Dawit" , 700),
    ("Tigist" , 200),
]

for name, balance in customers:
    if balance >=1000:
        tier = "premium"
    elif balance >=500:
        tier = "standard"
    else:
        tier = "basic"
    print(f"{name}  {tier} ({balance}ETB.)")
