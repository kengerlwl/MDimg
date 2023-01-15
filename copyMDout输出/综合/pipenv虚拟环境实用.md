# pipenv虚拟环境管理

## 安装
运行以下命令安装：
```
pip install pipenv
```

查看是否安装成功

```
pipenv --help
```

## 进行环境配置

进入项目文件夹下，安装虚拟环境
```
pipenv install
```

进入虚拟环境
```
pipenv shell
```
![](https://raw.githubusercontent.com/kengerlwl/MDimg/master/image/f4c8bb88e70a139f1a1b6fd1fbe46230/0c5e1eed2297e846bea8335613d5262c.png)


推出虚拟环境
```
exit
```


安装库
```
pipenv install flask
```


## 关于配置文件

pipenv 相对于可以做到虚拟环境的隔离，而且用pienv进行的库管理也更加合理。相对于pip freeze  > requirement的的库管理。pipenv更能分清依赖。能够分清哪些是项目用到的库，哪些是库需要的库。

例如一个pipfile
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
flask = "*"
flask-cors = "*"
dbutils = "*"
requests = "*"
ldap3 = "*"
passlib = "*"
requests-toolbelt = "*"
pycryptodome = "*"
xmltodict = "*"
redis = "*"
qrcode = "*"
pillow = "*"
pyzbar = {extras = ["scripts"], version = "*"}
[dev-packages]

[requires]
python_version = "3.7"

```


## 常用的命令

```
pipenv --where                 列出本地工程路径
pipenv --venv                  列出虚拟环境路径
pipenv --py                    列出虚拟环境的Python可执行文件
pipenv install                 创建虚拟环境
pipenv isntall [moduel]        安装包
pipenv install [moduel] --dev  安装包到开发环境
pipenv uninstall[module]       卸载包
pipenv uninstall --all         卸载所有包
pipenv graph                   查看包依赖
pipenv lock                    生成lockfile
pipenv run python [pyfile]     运行py文件
pipenv --rm                    删除虚拟环境,在虚拟环境的目录下运行
```

查看安装的库
```
# 方法一
pipenv run pip list

#方法二
pipenv requirements 
```

卸载
`pipenv uninstall package_name`卸载包



