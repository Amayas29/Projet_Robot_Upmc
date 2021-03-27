import configparser
config = configparser.ConfigParser()
# ecriture
config['Mode'] = {'mode_simu': 'true'}
config['Strat'] = {'strat1': 'avancer, reculer, tourne',
                   'strat2': 'avancer, recule'}
config['Chiffre'] = {'first': '1'}
with open('config.cfg', 'w') as configfile:
    config.write(configfile)
print("ok")
# lecture
config.read('config.cfg')
etat = str(config['Strat']['strat1'])
print(etat)
mode = config['Mode'].getboolean('mode_simu')
if (mode):
    print("Simu on")
else:
    print("simu off")
chiffre = int(config['Chiffre']['first'])
print(f"{chiffre}")
