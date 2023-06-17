# Learning to automate testing in Python
Implemented the first test on pytest. <br>
The tested service is presented here -> https://github.com/touchbit/automatron

### config.py
contains url (Need to change when starting locally) for of service under test:
```commandline
HOST = 'http://localhost:8080'
```

### Building local Allure report
for a local building Allure Report
1. Install Allure
2. Execute
```commandline
pytest --alluredir=%allure directory%
allure serve %allure directory% 
```
