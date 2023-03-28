## 简介

fofatools 是一个用python 编写的FOFA批量查询脚本，利用强大的互联网搜索引擎FoFa，能进行批量查询，让网络安全专业人士更容易在目标网站上寻找漏洞。

## 使用说明

本工具基于 FoFa 的 API 进行封装，使用时需要高级会员或者普通会员的 API key，使用注册用户的 API key 会提示账户需要充值F币。

点击 https://github.com/cail0906/fofatools 下载

- pip install pandas==1.5.3,requests==2.28.2
- 将查询语句写入fofa_queries.txt
- python fofa.py
- 查看新生成的csv文件



**FOFA会员说明链接!!!!!**

贵宾说明：https://fofa.info/static_pages/vip



## 问答

1. 为什么查询显示结果超过了10000条，但是导出的数据不到10000条？
   由于fofa api的限制，每个查询条件最多获取10000条数据，所以超过10000条以后的数据将无法导出，可尝试通过关键字和限制查询时间来获取数据。`after``before`

2. 为什么挂了梯子无法执行脚本？

   由于外网无法直接访问api
