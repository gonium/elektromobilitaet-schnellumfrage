import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
alldata = pd.read_csv("data/cleanelectric-20190412.csv",delimiter=',')

#print(alldata.head())

num_answers = alldata['Timestamp'].count()
daheimlader = alldata[alldata['Daheimladen']=="Ja"]
oeffentlichlader = alldata[alldata['Daheimladen']=="Nein"]


print("Anzahl Antworten: {}, davon Daheimlader: {}".format(num_answers,
  len(daheimlader.index)))

n, bins, patches = plt.hist(x=alldata['Fahrleistung'], bins='auto',
    color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Kilometer pro Jahr')
plt.ylabel('Häufigkeit')
plt.title(r'Fahrleistungen ($N={:d}$, $\mu={:d}$ km)'.format(
  int(num_answers),
  int(np.mean(alldata['Fahrleistung']))))
plt.savefig('img/fahrleistung-histogramm.png')

print("Mittlere Fahrleistung insgesamt: {:.0f}, Daheimlader: {:.0f}, \
Oeffentlichlader: {:.0f}".format(
  np.mean(alldata['Fahrleistung']),
  np.mean(daheimlader['Fahrleistung']),
  np.mean(oeffentlichlader['Fahrleistung'])
  )
)

plt.clf()
plt.scatter(daheimlader['Fahrleistung'], daheimlader['Stromverbrauch'],
  color='blue', label="Daheimlader")
plt.axhline(y=np.mean(daheimlader['Stromverbrauch']), color='blue',
    label="Durchschnitt daheim")
plt.scatter(oeffentlichlader['Fahrleistung'], oeffentlichlader['Stromverbrauch'],
  color='red', label="Öffentliche Lader")
plt.axhline(y=np.mean(oeffentlichlader['Stromverbrauch']), color='red',
    label="Durchschnitt öffentlich")
plt.legend(loc="upper left", prop={'size': 10})
plt.xlim([0, 52000])
plt.ylim([0, 21000])
plt.xlabel('Kilometer pro Jahr')
plt.ylabel('Jahresstromverbrauch [kWh]')
plt.title(r'Daheim oder öffentlich Laden')
plt.savefig("img/fahrleistung-stromverbrauch.png")

plt.clf()
plt.scatter(daheimlader['Stromverbrauch'], daheimlader['Stromerzeugung'],
  color='blue', label="Daheimlader")
plt.axhline(y=np.mean(daheimlader['Stromerzeugung']), color='blue',
    label="Durchschnitt daheim")
plt.scatter(oeffentlichlader['Stromverbrauch'],
    oeffentlichlader['Stromerzeugung'],
  color='red', label="Öffentliche Lader")
plt.axhline(y=np.mean(oeffentlichlader['Stromerzeugung']), color='red',
    label="Durchschnitt öffentlich")
plt.legend(loc="upper left", prop={'size': 10})
plt.xlabel('Jahresstromverbrauch [kWh]')
plt.ylabel('Jahresstromerzeugung [kWh]')
plt.xlim([0, 25000])
plt.ylim([0, 25000])
plt.title(r'Stromerzeugung und -verbrauch')
plt.savefig("img/stromverbrauch-stromerzeugung.png")

print("Stromverbrauch Daheimlader: min {:.0f}, avg {:.0f}, \
max {:.0f} kWh".format(
      np.min(daheimlader["Stromverbrauch"]),
      np.mean(daheimlader["Stromverbrauch"]),
      np.max(daheimlader["Stromverbrauch"]),
    )
  )

print("Stromverbrauch Öffentliche Lader: min {:.0f}, avg {:.0f}, \
max {:.0f} kWh".format(
      np.min(oeffentlichlader["Stromverbrauch"]),
      np.mean(oeffentlichlader["Stromverbrauch"]),
      np.max(oeffentlichlader["Stromverbrauch"]),
    )
  )
