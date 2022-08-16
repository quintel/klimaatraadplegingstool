'''Represent a full setting as we can send it to the ETM'''

class CombinedSetting:
    def __init__(self, etm_scenario_name, kr_setting, etm_setting, kpi_settings):
        '''
        They are all dicts -
        TODO: please give them a default of being empty!!
        '''
        self.etm_scenario_name = etm_scenario_name
        self.kr_setting = kr_setting
        self.etm_setting = etm_setting
        self.kpis = {key['gquery']: {'key': key['key'], 'value': None} for key in kpi_settings}

    def to_json(self):
        '''Make sure the KPI results are not None!'''

    def as_request(self):
        # This will change as we'll do two requests :)
        return {
            "scenario": {
                "user_values": self.etm_setting
            },
            "gqueries": self.kpis.keys()
        }

    def update_kpis(self, result):
        '''Update the KPI dict'''
        for query, outcome in result.items():
            self.kpis[query]['value'] = outcome['future']

    def add_setting(self, kr_key, kr_value, etm_settings):
        '''Add the settings for one klimaatraadpleging input to all settings'''
        if kr_key in self.kr_setting:
            raise KeyError(f'Settings for {kr_key} are already present')

        self.kr_setting[kr_key] = kr_value
        self.etm_setting.update(etm_settings)
