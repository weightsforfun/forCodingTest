import seaborn as sns
import matplotlib.pyplot  as plt



tips = sns.load_dataset("tips")
sns.boxplot(x="size", y="total_bill", hue="day", data=tips)
plt.show()