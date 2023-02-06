

# 监控哪些人在服务器卷小脚步

```
#coding=gbk
import os, re
import requests
import time

# 要留下就返回true
def is_none(s):
    if s:
        return True
    else:
        return False


# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def send_msg(msg):
    # url = 'http://110.40.204.239:5700/send_group_msg?group_id={}&message={}'.format(
    #     '590020444',
    #     msg
    # )

    url = 'http://110.40.204.239:5700/send_private_msg?user_id={}&message={}'.format(
        '2892211452',
        msg
    )
    print(msg)
    requests.get(url)
    pass



if __name__ == '__main__':
    listen_username = 'lwl'
    cmd = "w | grep {}".format(listen_username)
    online_users = {}
    while True:

        result = execCmd(cmd)
        print(result)
        result = result.split('\n')
        online_tty = {}
        all_msgs = ""
        for i in result:

            try:
                # 字符串划分
                i = list(filter(is_none, i.split(' ')))
                print(i)
                username = i[0]
                id = i[1]
                online_tty[id] = 1
                date = i[3]

                # 不在，通知并且添加到在线用户
                if id not in online_users:
                    online_users[id] = {
                        "username":username,
                        "date":date
                    }
                    all_msgs = all_msgs + "{} 于 {} 登录了服务器\n".format(username, date)
                else: # 如果id一样，但是用户不一样了，代表也是有新用户登录了
                    if username != online_users[id]['username']:
                        online_users[id] = {
                            "username": username,
                            "date": date
                        }
                        all_msgs = all_msgs + "{} 于 {} 登录了服务器\n".format(username, date)
            except Exception as e:
                print(e)

        if all_msgs:
            send_msg(all_msgs)


        # 清理掉不在线的终端
        del_key = []
        for key in online_users:
            if key not in online_tty:
                print("{} 终端已经下线".format(online_users[key]))
                del_key.append(key)
        for key in del_key:
            online_users.__delitem__(key)
        print(online_users)
        time.sleep(5)
```



## 防卷v2

```
#coding=utf-8
#coding=gbk
import os, re
import requests
import time

# 要留下就返回true
def is_none(s):
    if s:
        return True
    else:
        return False


# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def send_msg(msg):
    # url = 'http://110.40.204.239:5700/send_group_msg?group_id={}&message={}'.format(
    #     '590020444',
    #     msg
    # )

    url = 'http://110.40.204.239:5700/send_private_msg?user_id={}&message={}'.format(
        '2892211452',
        msg
    )
    rsp = requests.get(url)
    print("发送消息结果" + rsp.text)



if __name__ == '__main__':
    all_listen_username = {"lwl"}
    online_users = {}
    while True:

        # 针对每一个用户都进行检测
        for listen_username in all_listen_username:
            cmd = "w | grep {}".format(listen_username)
            result = execCmd(cmd)
            # print(result)
            result = result.split('\n')
            online_tty = {} # 当前在线终端
            all_msgs = ""
            for i in result:

                try:
                    # 字符串划分
                    i = list(filter(is_none, i.split(' ')))
                    # print(i)
                    username = i[0]
                    id = i[1]
                    
                    date = i[3]

                    # 用人和时间做key值
                    key = date + " " + username

                    online_tty[key] = 1
                    
                    # 剔除掉非目标用户
                    if username != listen_username:
                        continue

                    # 不在，通知并且添加到在线用户
                    if key not in online_users:
                        online_users[key] = {
                            "username":username,
                            "date":date
                        }
                        all_msgs = all_msgs + "{} 于 {} 登录了服务器\n".format(username, date)
    
                except Exception as e:
                    print(e)

            if all_msgs:
                send_msg(all_msgs)


            # 清理掉不在线的终端
            del_key = []
            for user_key in online_users:
                if user_key not in online_tty:
                    print("{} 终端已经下线".format(online_users[user_key]))
                    del_key.append(user_key)
            for user_key in del_key:
                online_users.__delitem__(user_key)
                del_msg = "{} 用户已经下线".format(user_key)
                send_msg(del_msg)
        # print(online_users)
        time.sleep(5)
```





# 自动下线小脚本

自动下线指定用户的终端，**一经发现，直接下线**

```
username=M1ld
while(true)
do
	sleep(500);
	who | grep $username | awk -F ' ' '{print $2}' | xargs  pkill -kill -t 
done;
```

