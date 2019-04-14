import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
alldata = pd.read_csv("data/cleanelectric-20190412.csv",delimiter=',')

print(alldata.head())

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
median {:.0f}, max {:.0f} kWh".format(
      np.min(daheimlader["Stromverbrauch"]),
      np.mean(daheimlader["Stromverbrauch"]),
      np.median(daheimlader["Stromverbrauch"]),
      np.max(daheimlader["Stromverbrauch"]),
    )
  )

print("Stromerzeugung Daheimlader: min {:.0f}, avg {:.0f}, \
median {:.0f}, max {:.0f} kWh".format(
      np.min(daheimlader["Stromerzeugung"]),
      np.mean(daheimlader["Stromerzeugung"]),
      np.median(daheimlader["Stromerzeugung"]),
      np.max(daheimlader["Stromerzeugung"]),
    )
  )

print(u"Stromverbrauch oeffentliche Lader: min {:.0f}, avg {:.0f}, \
median {:.0f}, max {:.0f} kWh".format(
      np.min(oeffentlichlader["Stromverbrauch"]),
      np.mean(oeffentlichlader["Stromverbrauch"]),
      np.median(oeffentlichlader["Stromverbrauch"]),
      np.max(oeffentlichlader["Stromverbrauch"])
    )
  )

print(u"Stromerzeugung oeffentliche Lader: min {:.0f}, avg {:.0f}, \
median {:.0f}, max {:.0f} kWh".format(
      np.min(oeffentlichlader["Stromerzeugung"]),
      np.mean(oeffentlichlader["Stromerzeugung"]),
      np.median(oeffentlichlader["Stromerzeugung"]),
      np.max(oeffentlichlader["Stromerzeugung"])
    )
  )



pflichteinbau = daheimlader[daheimlader["Stromverbrauch"] >= 6000]
sowiesopflichteinbau = pflichteinbau[
    (pflichteinbau["Elektrisch_Heizen"] == "Ja") |
    (pflichteinbau["Elektrisch_Wasser"] == "Ja") |
    (pflichteinbau["Stromerzeugung"] > 0)
  ]
optionaleinbau = daheimlader[
    (daheimlader["Stromverbrauch"] < 6000) &
    (daheimlader["Stromverbrauch"] >= 2000)
    ]

print("Anzahl Pflichteinbaufaelle intelligentes Messsystem: {:d}/{:d}".format(
    len(pflichteinbau.index), len(daheimlader.index)
  ))
print("... davon Haushalte, die sowieso Pflichteinbaufaelle sind: {:d}".format(
    len(sowiesopflichteinbau.index)
  ))
print("... demnach Anzahl Haushalte, die durch Elektroauto ein IMS \
bekommen: {:d}".format(
    len(pflichteinbau.index) - len(sowiesopflichteinbau.index)
    ))

print("Anzahl optionale Einbaufaelle intelligentes Messsystem: {:d}".format(
  len(optionaleinbau.index)
  ))

plt.clf()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Wegen PV etc.', 'durch EV', 'Optional'
sizes = [
    len(sowiesopflichteinbau.index), 
    len(pflichteinbau.index) - len(sowiesopflichteinbau.index), 
    len(optionaleinbau.index)
    ]
explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title(r'Daheimlader: Warum bekommt man ein intelligentes Messsystem?')
plt.savefig("img/einbaufaelle.png", bbox='tight')
