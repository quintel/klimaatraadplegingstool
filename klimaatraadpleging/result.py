import json

class Result():
    def __init__(self, combiner, etm_session):
        self.result = []
        self.combiner = combiner
        self.etm_session = etm_session

    def calculate(self):
        for setting in self.combiner.generate_settings():
            self.etm_session.calculate_kpis(setting)
            self.result.append(setting.as_json())

    def write_to(self, path):
        f = open(path, "w")
        f.write(json.dumps(self.result))
        f.close()
