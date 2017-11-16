# 说明
 - **环境准备**
       1. 安装 Python 2.7.X 

       2. 安装 Pip 工具

          - 从 https://bootstrap.pypa.io/get-pip.py 下载.py 文件
          - 在命令行运行

          ```
          python get-pip.py
          ```

       3.  安装 logconfig 模块

           ```

           ```
          pip install logconfig
           ```
        
          参考： https://pypi.python.org/pypi/logconfig

    ​      

- **日志loggin**

    - **格式字段介绍**

    > filename: 指定日志文件名
    > filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
    > format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
    > %(levelno)s: 打印日志级别的数值
    > %(levelname)s: 打印日志级别名称
    > %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    > %(filename)s: 打印当前执行程序名
    > %(funcName)s: 打印日志的当前函数
    > %(lineno)d: 打印日志的当前行号
    > %(asctime)s: 打印日志的时间
    > %(thread)d: 打印线程ID
    > %(threadName)s: 打印线程名称
    > %(process)d: 打印进程ID
    > %(message)s: 打印日志信息
    > datefmt: 指定时间格式，同time.strftime()
    > level: 设置日志级别，默认为logging.WARNING
    > stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略   
    >
    > ​
    >

    - **各种Handler** 

    > logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
    > logging.FileHandler: 日志输出到文件
    >
    > 日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
    > logging.handlers.BaseRotatingHandler
    > logging.handlers.RotatingFileHandler
    > logging.handlers.TimedRotatingFileHandler
    >
    > logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
    > logging.handlers.DatagramHandler: 远程输出日志到UDP sockets
    > logging.handlers.SMTPHandler: 远程输出日志到邮件地址
    > logging.handlers.SysLogHandler: 日志输出到syslog 
    > logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志 
    > logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
    > logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器
    >
    > 由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中， 上述其它处理方式的使用请参见python2.5手册！
    >



 - 例子介绍

   -  [main.py](main.py) 利用dict 类型和 .ini 文件两种定义形式进行配置

     - dict : `logging.config.dictConfig(another_config)`

     - .ini 文件： `logging.config.fileConfig('logging.ini', disable_existing_loggers=False)`

       ​

   - [yaml_logging_main.py](yaml_logging_main.py)  利用Yaml 形式进行配置

   - ​