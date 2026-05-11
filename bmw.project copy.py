#BMW vs porsche sales analysis 
#created by MOHAMMED MUBASHIR AHMED 
#tools used : python, pandas , matplotlib



import pandas as pd

import matplotlib.pyplot as plt

data = {
    "Car": [
        "BMW X5",
        "BMW M4",
        "BMW i8",
        "BMW X3",
        "Porsche 911",
        "Porsche Cayenne",
        "Porsche Taycan"
    ],

    "Sales": [
        120,
        90,
        40,
        150,
        180,
        130,
        95
    ]
}

df = pd.DataFrame(data)

print(df)


print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
plt.bar(df["Car"], df["Sales"],
        color=["blue","black","silver","skyblue",
               "red","gray","green"])
plt.title("BMW vs porsche  Sales Analysis")
plt.xlabel("BMW Cars")
plt.ylabel("Sales")
plt.savefig("/Users/mohammedmubashir/Desktop/bmw_porsche_sales.png")

plt.show()