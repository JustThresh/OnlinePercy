import multiprocessing

# �󶨶˿ں�
bind = '127.0.0.1:8000'  # ���ؾ�����Ҫ��Ϊ����ip

# ����������
workers = multiprocessing.cpu_count() * 2 + 1

# ÿ���������߳���
# threads = multiprocessing.cpu_count() * 2 + 1

timeout = 30
daemon = False

# ��־����
loglevel = 'debug'  # ������־����
# access_log_format = '%(t)s %(p)s %(h)s %({X-Forwarded-For}i)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = '/local/logs/gunicorn.acc.log'
errorlog = '/local/logs/gunicorn.err.log'  # '-' �������Ļ��ʽ
capture_output = True  # �ѱ�׼����ͱ�׼�����ض�����־�ļ���

pidfile = '/tmp/gunicorn.pid'
