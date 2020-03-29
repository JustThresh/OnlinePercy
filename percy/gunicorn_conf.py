import multiprocessing

# 绑定端口号
bind = '127.0.0.1:8000'  # 负载均衡需要改为本机ip

# 工作进程数
workers = multiprocessing.cpu_count() * 2 + 1

# 每个进程数线程数
# threads = multiprocessing.cpu_count() * 2 + 1

timeout = 30
daemon = False

# 日志级别
loglevel = 'debug'  # 错误日志级别
# access_log_format = '%(t)s %(p)s %(h)s %({X-Forwarded-For}i)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = '/local/logs/gunicorn.acc.log'
errorlog = '/local/logs/gunicorn.err.log'  # '-' 输出到屏幕方式
capture_output = True  # 把标准输出和标准错误重定向到日志文件中

pidfile = '/tmp/gunicorn.pid'
