# 一.web框架模式
## a. django模式：MVT/MTV（models/templates/views）
	M（模型） -- 模型层--定义业务模型和数据库（管理数据），一个模型对应数据库中的一个数据表
	V（视图） -- 业务逻辑层 -- 负责业务逻辑并适当调用Model和Template  （相当于MVC中的controller）
	T（模板） -- 表现层 -- 模板，渲染HTML页面或者返回数据展现给用户（空的document模型）

    过程 ： 用户输入请求 -- >  服务器URL控制器接收匹配URL --> 交给不同的view视图 -- > 视图去model读取数据 (model读取数据库数据返给视图)-- > 视图将数据给模板Templates -- > 模板将页面返给用户
## b. 传统模式：MVC(models/views/controller)
	M（模型） -- 模型层 -- 定义业务模型和数据库，一个模型对应一个数据表
	V（视图）-- 表现层 -- 渲染HTML页面或者返回数据给客户
	C（控制器） -- 收集用户输入、请求，进行逻辑判断 、数据的处理（crud）

    过程 ： 用户输入请求 --> controller控制器接收处理请求 --> 通过数据库访问数据返回给控制器 -- > 把数据给views视图，展现给用户
    优点： 降低各功能模块之间的耦合性，方便变更，更容易 构建代码，最大程度上实现代码的重用

# 二.创建django框架项目

### django开发流程：
		启动mysql服务 --> 
		搭建python虚拟环境 --> 
		创建django工程 --> 
		创建应用项目 -->  
		配置setting.py（数据库，应用，）--> 
		配置数据库（__init__.py中导入mysql）--> 
		在models.py文件中创建模型 --> 
		生成、迁移模型数据表 --> 
		创建模板（templates）--> 
		在setting.py中配置模板 --> 
		编写项目（模型、视图、模板）


**python主要的web框架：Django、Flask、Tornado**
## a.给项目搭建python虚拟环境：
### 1）第一步 -- 安装virtualenv工具：在cmd终端中输入 -- pip install virtualenv
（pycharm终端输入也可以，最好在创建之前在某一地址创建venv和workspacel两个文件夹，一个存放项目虚拟环境，一个存放代码）
### 2）第二步 -- 给项目创建python3.7版本虚拟环境：
    virtualenv --no-site-packages -p C:\python37\python.exe django_project_files

以上命令表示：不导入系统自带库，创建纯净的虚拟环境，选择python3.7版本环境创建名为django\_project_files的项目文件
### 3）第三步 -- 输入cd django_project_files,再输入cd Scripts，再输入activate（苹果电脑用source  activate）激活虚拟环境
### 4）第四步 -- pip install django，pip install pymysql(安装最新的django和pymysql版本，安装之前可以通过pip list命令查看第二步安装的库)
### 5）第五步 -- deactivate命令退出虚拟环境
## b.创建django项目
### 1)第一步--django-admin startproject 项目名称 
#### 项目下有一个manage.py文件和一个工程文件夹：
	1） 项目名称目录下有是个文件：
	__init__.py -- 告诉python这个所在的文件夹看成是python包（空文件）
	settings.py -- 项目的配置文件
	urls.py -- 项目的url声明
	wsgi.py -- 项目与WSGI兼容的Web服务器入口


	2） manage.py -- 一个命令行工具。可以使我们用多种方式对Django项目进行交互
### 2)第二步 -- 给项目配置虚拟文件
        启动pycharm，点击左上方file下的open，打开建立的项目文件（wordspace下面的项目django\_project_files）
        再点击file下面的settings下的project:django\_project_files下的Project Interpreter配置虚拟环境
### 3）第三步 -- 配置驱动（配置右上角的三角运行按钮）






			###2）第二步 -- python manage.py runserver 启动Django框架服务器 (django自带的纯python写的轻量级的web服务器，只在开发测试阶段使用)
			修改启动端口 ： python manage.py runserver ip:端口
			修改启动端口：  python manage.py runserver 端口
			port端口参数默认为80端口，可以不用写
			ip参数如果为0.0.0.0表示可以通过公网访问



## c.数据库连接配置（Django默认SQLite数据库）：
### 1)第一步：setting.py配置（DATABASES参数配置）
        将SQLite改为mysql
		USER：用户名
		PASSWORD参数：密码
		HOST：ip
		POST:端口 
		NAME：数据库名字
### 2）第二步：pip installl pymysql -- 安装pymysql(python3没有mysqldb驱动器，python2不用安装)
### 3)第三步 ：在__init__.py文件中导入pymysql模块并调用：pymysql.install\_as_MySQLdb()
## c.创建应用
**一个python程序中可以创建多个应用，每个应用进行一个业务处理**
### 第一步：创建应用
    python manage.py startapp 应用名 -- 创建应用生成叫应用名的包
### 第二步：激活应用
    在settings.py中，将创建的引用名加入到INSTALL_APPS选项中
### 第二步：数据库表的迁移 
	1）第一次迁移：python manage.py migrate--将Django自带的数据表迁移到数据库中（用户表，日志表等等）
    

	2）在models.py中写表的模型：
	class Student(models.Model):
	    s_name = models.CharField(max_length=10, unique=True)
	    s_age = models.IntegerField(default=20)
	    s_gender = models.BooleanField(default=0)
	    # auto_now_add:创建时，默认字段赋值为最新事件
	    create_time = models.DateTimeField(auto_now_add=True)
	    # auto_now :
	    update_time = models.DateTimeField(auto_now_add=True)
	
	    class Meta:
	        db_table = 'student'


	3）生成迁移文件：（除开第一次） python manage.py makemigrations
	4）执行迁移文件 （将数据存入数据库）：python manage.py migrate
