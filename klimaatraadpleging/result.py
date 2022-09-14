import json

class Result():
    def __init__(self, combiner, etm_session):
        self.result = []
        self.combiner = combiner
        self.etm_session = etm_session

    def calculate(self):
        counter = 0

        for setting in self.combiner.generate_settings():
            # We have three iterations of requests to ETE:
            # 1. create scenario
            # 2. queries for demand_installer
            # 3. update user values with installed demand + get KPI's
            for i in range(3):
                self.etm_session.calculate(setting, iteration=i)

            self.result.append(setting.as_json())

            counter += 1
            if counter % 1000 == 0: print(counter)

    def write_to(self, path):
        f = open(path, "w")
        f.write(json.dumps(self.result))
        f.close()
