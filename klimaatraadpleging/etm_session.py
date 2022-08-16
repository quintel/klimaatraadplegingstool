import requests

from klimaatraadpleging.config import Config

class ETMSession():
    def __init__(self):
        pass

    def calculate_kpis(self, setting):
        data = setting.as_request()
        url = Config().etengine_url + '/scenarios/'

        if setting.etm_scenario_id:
            url += setting.etm_scenario_id
        else:
            data['scenario']['end_year'] = Config().basic_scenario['end_year']
            data['scenario']['area_code'] = Config().basic_scenario['area_code']

        self._update_kpis(setting, self._handle_response(requests.put(url, json=data)))

    def _update_kpis(self, setting, new_content):
        '''Updates the scenario ID and the KPI's'''
        setting.etm_scenario_id = new_content['scenario']['id']
        setting.update_kpis(new_content['gqueries'])

    def _handle_response(self, response):
        if response.ok:
            return response.json()

        raise ETMConnectionError(response.content)

class ETMConnectionError(Exception):
    pass
