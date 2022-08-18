import requests
from klimaatraadpleging.combined_setting import CombinedSetting

from klimaatraadpleging.config import Config

class ETMSession():
    def __init__(self):
        pass

    def calculate_kpis(self, setting: CombinedSetting):
        url = Config().etengine_url + '/scenarios/'

        if not setting.etm_scenario.id:
            self._create_scenario(setting)

        url = f'{url}{setting.etm_scenario.id}'
        self._update_kpis(
            setting,
            self._handle_response(requests.put(url, json=setting.as_request(with_queries=True)))
        )

    def _handle_response(self, response):
        if response.ok:
            return response.json()

        try:
            raise ETMConnectionError(response.json())
        except:
            raise ETMConnectionError(response.content)

    def _create_scenario(self, setting: CombinedSetting):
        '''Create a new scenario for the CombinedSetting'''
        data = setting.as_request()
        data['scenario']['end_year'] = Config().basic_scenario['end_year']
        data['scenario']['area_code'] = Config().basic_scenario['area_code']

        self._update_scenario_id(
            setting,
            self._handle_response(requests.post(Config().etengine_url + '/scenarios/', json=data))
        )

    def _update_scenario_id(self, setting: CombinedSetting, data: dict):
        setting.etm_scenario.id = data['id']

    def _update_kpis(self, setting, new_content):
        '''Updates the scenario ID and the KPI's'''
        setting.update_kpis(new_content['gqueries'])


class ETMConnectionError(Exception):
    pass
