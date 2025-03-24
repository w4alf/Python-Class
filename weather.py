
temperature = input("Enter a temperature:\n")
temperature = int(temperature)
forecast = input("Enter the forecast:\n")

if temperature > 90 and not forecast== "rainy":
    print("Stay inside.")
else:
    print("Enjoy the outdoors.")
