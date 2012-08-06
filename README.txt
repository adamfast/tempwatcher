This project is a simple solution to get your own temperature alerts from a 3m Filtrete or RadioThermostat thermometer. You can subscribe to their service for $25/yr, but if you already run a computer all the time why not do it yourself?

Tested with the Filtrete 3M-50 model, will work on others that have the same API.

watch.py will need to know the IP address of your thermostat. If you want the alerts to go anywhere but stdout, subclass TemperatureWatch and change the alert method to do what you want with the message.

Cron up the script, and you're set!
