# klimaatraadplegingstool
Tool to generate the ETM results for the kimaatraadpleging database.

Please use pyenv and pipenv for the best experience.

Simple installation of the tool:
```
pipenv install
```

Generate the result in the output folder:
```
pipenv run generate_results
```

## Configuration
You can add multiple basic scenarios and their settings to `basic_scenarios.csv`. The format is the
same as used in the [`scenario-tools`](https://github.com/quintel/scenario-tools).

Settings of supply and efficiencies that should be added to each individual scenario can be
specified in `supply_and_savings.csv`.

In the file `input_mapping` you can specify for each klimaatraadpleging slider for which setting
which ETM sliders should be altered and with what values.

The global `config.yml` contains the ETEngine url to connect to, and the `end_year` and `area_code`
information for creating the basic scenarios. For now also the KPI queries are in this config, but we can change that.

## Results
The result can be found in the output folder in the form of a JSON with all combinations of
klimaatraadplegings sliders. For example:

```
[
  {
    "wevaluate_option_1000": 0,
    "wevaluate_option_1001": 0.25,
    "wevaluate_option_1002": 0,
    "etm_scenario": "high_demand",
    "etm_kpi_one": 300,
    "etm_kpi_two": 123456789
  },
  {
    "wevaluate_option_1000": 0,
    "wevaluate_option_1001": 0.5,
    "wevaluate_option_1002": 0,
    "etm_scenario": "high_demand",
    "etm_kpi_1": 310,
    "etm_kpi_2": 123456999
  }
]
```
