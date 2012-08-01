import json
import requests


class TemperatureWatch(object):
    thermostat_url = None
    alert_high = 80
    alert_low = 60
    _last_response = None

    def get_info(self):
        r = requests.get(self.thermostat_url + '/tstat')
        self._last_response = json.loads(r.text)
        return r.text

    def check_temp(self):
        if not self._last_response:
            self.get_info()

        if self._last_response['temp'] > self.alert_high:
            print('Temperature max of %s exceeded. Currently %s' % (self.alert_high, self._last_response['temp']))

        if self._last_response['temp'] < self.alert_low:
            print('Temperature min of %s exceeded. Currently %s' % (self.alert_low, self._last_response['temp']))


if __name__ == '__main__':
    tw = TemperatureWatch()
    tw.thermostat_url = 'http://10.0.1.52'
    tw.check_temp()
