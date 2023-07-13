import numpy as np

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/mac/Downloads/tub.xls')
man = df.set_index('Unnamed: 0').loc[['Мужчины', 'Женщины']].reset_index().set_index('год')
wom = df.set_index('Unnamed: 0').loc['Женщины'].set_index('год', drop=True)
m = df.set_index('Unnamed: 0').loc['Мужчины'].set_index('год', drop=True)
all = df.set_index('Unnamed: 0').loc['Всего'].set_index('год', drop=True)

man = man.reset_index()
man = man.rename(columns={"Unnamed: 0": "пол"})
man = man[man['год'] < 2020]
first_age = man[['год', 'пол', '0-17 лет']]
sec_age = man[['год', 'пол', '18 лет и старше']]


fig, axes = plt.subplots(2, 1, figsize=(7, 5), sharey=True)
plt.rc('legend', fontsize=7)

gr1 = sns.barplot(
    data=first_age,
    x='год',
    y='0-17 лет',
    hue='пол',
    ax=axes[0],
)
gr1.set(title='Туберкулез в РФ')

sns.barplot(
    data=sec_age,
    x='год',
    y='18 лет и старше',
    hue='пол',
    ax=axes[1]
)

plt.subplots_adjust(hspace=0.5)




plt.show()