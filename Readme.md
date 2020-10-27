# 目录结构说明
```
Hogwarts_Pytest_AllureReport
|--- core
|--- tests

core 源代码
tests 测试代码 
```

# 作业说明

完善Calc的用例，增加更多用例（浮点数相乘bug）
- 提交的github测试文件地址
- 把allure的首页截图到回帖中

# 执行命令
```
pytest --alluredir=./results test_Calc.py

allure serve ./results

```