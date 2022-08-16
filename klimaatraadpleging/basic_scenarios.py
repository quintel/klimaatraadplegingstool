class BasicScenarios():
    def  __init__(self, basic_settings, supply_and_savings):
        '''Both are dataframes'''
        #  I'm sorry dataframes, but you are nasty. We do it old fashioned with some dicts

        scenarios = basic_settings.to_dict()
        extra_settings = supply_and_savings['value'].to_dict()
        for scenario in scenarios:
            scenarios[scenario].update(extra_settings)
        self.scenarios = scenarios

    def generate_scenarios(self):
        '''Generate the different scenarios'''
        for scenario, settings in self.scenarios.items():
            yield (scenario, settings)
