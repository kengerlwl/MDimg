# 介绍

GitHub Actions是GitHub 官方出品的持续集成工具，非常优秀的 CI/CD 工具。

在软件工程中，CI/CD或CICD通常指的是持续集成和持续交付或持续部署的组合实践。

### **简单来说**

就是一个自动化来对提交的代码进行打包，集成，运维部署，测试，同步等操作。



### 优点

支持平台很多

Github支持自建容器

支持基于事件触发：push / issue 创建 / PR 提交都可以触发，完全可以基于此完成一套自动化维护项目的流程。



### 概念/术语

1. Workflow：GitHub 是对一次 CI/CD 的过程定义为 Workflow，中间可能经历过代码拉取，编译，测试，打包，发布，通知等多个过程。
2. Action： 一个独立的运行任务，多个 Action 组成 steps 来创建一个 Job。一组 Action（Actions） 逻辑相同就可以被复用，可以发布到 Actions Marketplace 供他人使用。
3. Steps：一个多个 Actions 形成的步骤。一个 step 可以只是一个命令，也可以是一个 Action。
4. Job：Steps 中的 Action 一个一个走完就完成了一个 Job。Job 下的所有 step 是运行在同一个容器中的，所以可以共享文件系统。
5. Workflow File：Workflow 的配置文件，yaml 格式。GitHub 规定需要存放在 `{$REPO_HOME}/.github/workflow/`。





# demo讲解

### action与step结构

- step会一个接着一个依次执行
- step可以直接引入其他开发者的开源插件
- step也可以是一段命令

```yaml
name: github pages # 工作流的名称

# 触发工作流的事件 Event 下面设置的是当 push 到 source 分支后触发
# 其他的事件还有：pull_request/page_build/release
# 可参考：https://help.github.com/en/actions/reference/events-that-trigger-workflows
on:	
  push:
    branches:
    - source

# jobs 即工作流中的执行任务
jobs:
  build-deploy: # job-id
    runs-on: ubuntu-18.04 # 容器环境
    # needs: other-job 如果有依赖其他的 job 可以如此配置
    
    # 任务步骤集合
    steps:
    - name: Checkout	# 步骤名称
      uses: actions/checkout@v2	# 引用可重用的 actions，比如这个就是 GitHub 官方的用于拉取代码的actions `@` 后面可以跟指定的分支或者 release 的版本或者特定的commit
      with:	# 当前 actions 的一些配置
        submodules: true # 如果项目有依赖 Git 子项目时可以设为 true，拉取的时候会一并拉取下来

    - name: Setup Hugo
      uses: peaceiris/actions-hugo@v2	# 这也是一个开源的 actions 用于安装 Hugo
      with:
        hugo-version: 'latest'
        # extended: true

		# 单运行命令
    - name: Build
      run: hugo --minify # 一个 step 也可以直接用 run 执行命令。如果有多个命令可以如下使用
      #run: |
    		#npm ci
    		#npm run build

    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3 # 开源 actions 用于部署
      with:
        github_token: ${{ secrets.GITHUB_TOKEN}} # GitHub 读写仓库的权限token，自动生成无需关心
        publish_branch: master
```





### 1. github每个yml文件对应一个action

```
. .github目录
└── workflows
    ├── action.yml
    └── action2.yml

```

- 每个文件对应一个action
- 支持同时运行多个action

![image-20230226162215015](/Users/lwl/Library/Application Support/typora-user-images/image-20230226162215015.png)



### 2. 事件触发器

- 可以通过指定事件来触发工作流程

```
on:
  push:
    branches: # 指定以master 分支或名称 以 releases/ 开头的分支 
    - master  
    - 'releases/**'
    paths: # 仅仅docs目录下面的改变才会触发
    - 'docs/**'
  pull_request: # 指定新的pull request
    branches:
    - master
    - 'releases/**'
```

### 3.矩阵参数组合执行

很多时候对于一些复杂环境，例如我这里有一个服务器。然后里面有许多参数组合不同，我想要组合执行一遍。

那么可以用这个方案

```
name: CI

on: [push]

jobs:    
  build:
    runs-on: ubuntu-latest

    strategy:    
      matrix:
        cc: [gcc, clang]
        curl: [openssl, gnutls, nss]
        kerberos: [libkrb5, heimdal]

    steps:
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y ${{ matrix.cc }} \
                                libcurl4-${{ matrix.curl }}-dev \
                                ${{ matrix.kerberos }}-dev
    - name: Display Configuration
      run: |
        echo "C Compiler:"
        ${CC} --version
        echo ""
        echo "Curl configuration:"
        curl-config --ssl-backends --version
        echo ""
        echo "Kerberos configuration:"
        krb5-config --all
      env:
        CC: ${{ matrix.cc }}

    - name: Checkout
      uses: actions/checkout@v1

    - name: Build
      run: ./configure && make test
```

结果，执行的时候会自动替换成相应的变量

![image](https://user-images.githubusercontent.com/3297411/77169169-07952200-6af4-11ea-8770-f381ddfaa7eb.png)



### 4.平台指定

以下面的代码为例，就指定了多个平台分别作为一个job，执行代码检查任务

```
# test
name: CI

on: [push]

jobs: #可以有多个job
  linux:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v1
    - name: Build
      run: make

  windows:
    runs-on: windows-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v1
    - name: Build
      run: make

  macos:
    runs-on: macos-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v1
    - name: Build
      run: make
      
```

### 5. run命令，同时运行多行

run可以执行命令，支持同时运行多行

```
name: CI

on: [push]

jobs: #可以有多个job
  linux:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v1
      - name: Build
        run: make
        run: |  #同时运行多行
          npm ci
          npm run build
          npm test
```



**注意！！！**

**注意，如果在一个 step 中 cd 到某个目录下，那么后续的 step 是不受影响的，还是在原来的目录中。**



### 6.Github密码

##### 6.1 可以自己设置一些变量

![image-20230226193445352](/Users/lwl/Library/Application Support/typora-user-images/image-20230226193445352.png)

要使用该密码，你可以在工作流中使用上下文 `secrets` 来引用它。如果你有一个密码的名字 `SECRET_KEY`，你可以将其称为 `$`。

```yaml
name: Publish Documentation


on:
  push:
    branches:
    - master


jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - run: |
          VERSION=$(date +%s)
          docker login -u ethomson -p ${{ secrets.SECRET_KEY }}
          docker build . --file Dockerfile --tag ethomson/app:${VERSION}
          docker push ethomson/app:${VERSION}
```

 



#####  **`GITHUB_TOKEN`**

GitHub Actions会为每次运行的工作流**自动在存储库中设置一个密码 `GITHUB_TOKEN`。该令牌使你可以与存储库进行交互，而无需自己创建新令牌或设置密码。**

该令牌为你提供了对存储库本身，issue和[GitHub Packages](https://www.edwardthomson.com/blog/github_actions_9_deploy_to_github_packages.html)进行读写的有限访问权限。但是它不能完全访问所有内容──你无法与组织中的其他存储库一起使用，也无法发布到GitHub Pages──因此，对于某些工作流，你可能仍需要设置令牌。



# ref

[使用 GitHub Action 持续集成你的博客](https://blog.xiaohei.im/posts/github-action-guide/)

[GitHub Actions 第11天：密码（Secrets）](https://qiwihui.com/qiwihui-blog-94/)

[请在该页面检索action](https://qiwihui.com/archives/)