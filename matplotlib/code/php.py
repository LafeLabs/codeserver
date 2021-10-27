############### GET INPUT FILE ###############
infile = open("data.txt","r")
textin = infile.read()
infile.close()
##############################################
import numpy as np
import matplotlib.pyplot as plt
import json
jsondata = json.loads(textin)
t = []
v = []
for i in range(len(jsondata)):
    v.append(jsondata[i]['voltage'])
    t.append(jsondata[i]['timestamp'])

#t = np.arange(0,100)
#v0 = 100
#v1 = 100
#tau = 30.0
#v = v1 + v0*np.exp(-t/tau)
#noise = np.random.normal(0,3,100)
#v += noise

fig, ax = plt.subplots()
ax.plot(t, v)

ax.set(xlabel='time [s]', ylabel='voltage [V]',
       title='voltage vs. time')
ax.grid()

fig.savefig("plot.png")
#plt.show()


######### SAVE OUTPUT FILE  ###### 
file = open("textout.txt", "w")
file.write(textin)
file.close()

