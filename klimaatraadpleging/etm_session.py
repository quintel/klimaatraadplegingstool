import requests
from klimaatraadpleging.combined_setting import CombinedSetting

from klimaatraadpleging.config import Config

class ETMSession():
    def __init__(self):
        pass

    def calculate(self, setting: CombinedSetting, iteration=0):
        if iteration == 0:
            self._create_scenario(setting)

        url = f'{Config().etengine_url}/scenarios/{setting.etm_scenario.id}'
        self._update_setting(
            setting,
            self._handle_response(requests.put(url, json=setting.as_request(iteration))),
            iteration
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

    def _update_setting(self, setting: CombinedSetting, result, iteration=1):
        setting.update(result['gqueries'], iteration)


class ETMConnectionError(Exception):
    pass
