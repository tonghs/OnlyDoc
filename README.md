# 这是一个文档管理工具

## 安装说明

1. 配置服务器
    * MySQL
		* 安装 MySQL 开发库

			```
			# 如果是 Ubuntu，执行：
			sudo apt-get install libmysqlclient-dev

			# 如果是 CentOS，执行：
			sudo yum install -y  mysql-devel
			```
    * Python 2.7
    * pip
    * nginx
    * supervisor

2. clone 代码
	
	```
    git clone https://github.com/tonghuashuai/sth.git YOUR-DIR
	```
	
	此时你的 server 目录为 YOUR-DIR/xinhua，将所有配置中的 YOUR-PATH 替换为该值

3. 进入代码目录，安装网站运行依赖

	```
    sudo chmod +x apt.sh
    sudo ./apt.sh
    sudo pip install -r requirements.txt
	```

4. 配置网站信息
	
	```
    cp config.sample.py config.py
	```
	
	然后根据具体情况修改 config.py ，文件内容及说明:

    ```
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	DEBUG = True  # 调试模式，上线后请改为 False
	APP = 'StoryBoard'  # 网站名称，即网站左上角显示的名字
	PORT = 8888
	STATIC_HOST = 'http://192.168.1.123:8889'  # 静态资源文件（js、css、img、favicon）地址及端口（静态文件可单独部署，不过这个规模的网站没必要了）
	HOST = 'http://192.168.1.123'  # 网站 IP 或域名
	COOKIE_SECRET = '0532ba8942499cdef558f8da355093ce'  # 可以自己生成一个或就用现有的这个


	#  MySQL 数据库配置
	class MYSQL:
		HOST = 'localhost'  # 数据库地址
		USER = 'root'  # 数据库用户名
		PWD = 'pwd'  # 数据库密码
		DB = 'db_name'  # 数据库名
    ```

5. 新建数据库

	```
	CREATE DATABASE `db_name` CHARACTER SET utf8 COLLATE utf8_general_ci;
	```

6. 初始化数据库

	```
	python test/models.py
	```

7. 配置 supervisor
	* 根据需要修改 misc/conf/supervisor.conf 中的内容
	* 添加配置文件

		``` 
		cd /etc/supervisor/conf.d
		ln -s YOUR-PATH/misc/conf/supervisor.conf xinhua.conf
		 ```
	* reload config file 或 重启 supervisor 服务

8. 配置 nginx 反代
	* 根据需要修改 misc/conf/nginx.conf 中的内容（端口、域名、路径）
	* 添加配置文件

		``` 
		cd /etc/nginx/conf.d
		ln -s YOUR-PATH/misc/conf/nginx.conf xinhua.conf
		nginx -s reload
		```

至此配置完成，可以根据配置的域名或 IP 访问了。
