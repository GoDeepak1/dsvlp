import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
data = np.random.randn(1000) 
sns.set_theme(style="whitegrid",font='yellow') 
sns.histplot(data, kde=True) 
plt.title('Customized Seaborn Plot - Deepak USN: 1BI21CS179') 
plt.xlabel('Value') 
plt.ylabel('Frequency') 
plt.show()
