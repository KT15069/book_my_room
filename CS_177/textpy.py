#Matplotlib charts
import matplotlib.pyplot as plt

#line chart
y1=[12,45,34,9,8,13,15,20,22,25,26]
y2=[21,24,25,15,11,9,5,10,12,15,20]
x=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
plt.plot(x,y1,linewidth=1,color="m",marker="o",mec="k",linestyle="-")

plt.plot(x,y2,linewidth=1,color="c",marker="^",mec="k",linestyle="--")
plt.title("Price Trend from 2k00-2k10",fontdict={'family':"Times New Roman",'color':"r"})
plt.xlabel("Years")
plt.ylabel("Price")
plt.grid(alpha=0.3)

y1=[99,100,200,120]
x=[2021,2022,2023,2024]
plt.show()
plt.close()
plt.pie(y1,labels=x,autopct="%1.2f%%",pctdistance=1.5,wedgeprops={'edgecolor':'y','linewidth':5})
plt.legend(x,loc='center left')
plt.show()
plt.close()
