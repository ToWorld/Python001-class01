# 文件功能说明
## python_jobs.py
  用于爬取北京、上海、广州、深圳前100的python待遇，最终将每一个职位写到job_info.csv文件中。 地区级别顺序挖掘，特定地区使用多线程爬取。
## agg.py
  按照地区对数据进行汇总，求平均值，并生成新文件agg.json。
## show.py
  使用matplotlib对csv文件进行画图展示.
