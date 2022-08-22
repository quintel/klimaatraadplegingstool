'''Represent a full setting as we can send it to the ETM'''

from klimaatraadpleging.etm_scenario import ETMScenario


class CombinedSetting:
    def __init__(self, etm_scenario_name, kr_setting, etm_setting, kpi_settings):
        '''
        They are all dicts
        '''
        self.kr_setting = kr_setting
        self.etm_scenario = ETMScenario(etm_scenario_name, etm_setting, kpi_settings)

    def as_json(self):
        '''Returns a dict that can be dumped by json'''
        return (
            self.kr_setting |
            self.etm_scenario.as_json()
        )

    def as_request(self, iteration=0):
        if iteration == 0:
            return self.etm_scenario.scenario_object()
        if iteration == 1:
            return self.etm_scenario.installer_queries()
        if iteration == 2:
            return self.etm_scenario.installer_user_values() | self.etm_scenario.kpi_queries()

    def update(self, result, iteration=1):
        if iteration == 1:
            self.etm_scenario.update_installer(result)
        if iteration == 2:
            self.etm_scenario.update_kpis(result)

    def add_setting(self, kr_key, kr_value, etm_settings):
        '''Add the settings for one klimaatraadpleging input to all settings'''
        if kr_key in self.kr_setting:
            raise KeyError(f'Settings for {kr_key} are already present')

        self.kr_setting[kr_key] = kr_value
        self.etm_scenario.update(etm_settings)
