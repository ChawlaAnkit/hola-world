import pandas as pd
import matplotlib.pyplot as plt
a = {"Name":{"0" :"Ankit",
"1" : "Pankaj",
"2" : "Pranjal",
"3" : "Akash"},
"Expertise":{"0" : "Sf",
"1" : "Se"},"data" : {"0" : 50,
"1" : 100}}
b = pd.DataFrame(a)
x = b["data"].mean()
b["data"].fillna(x, inplace= True)

b.fillna("he", inplace = True)
print(b)
b.plot()
plt.show()
