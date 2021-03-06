

# 匹配 “ujiuye”
import re

# ret = re.match("ujiuye","ujiuye.com")
# # print(ret)
# if ret:
#     print(ret.group())
# else:
#     print("匹配不成功")


# 匹配单个字符
# # - 1.“.” ：表示匹配任意一个字符，除了\n(换行符)以外
# #案例：看电影，输入电影名称：“速度与激情”时，“激”字符可以任意输入，都算成功
# # ret = re.match("速度与激情","速度与激情") #速度与激情
# # ret = re.match("速度与.情","速度与即情") #速度与即情
# # ret = re.match("速度与.情","速度与#情")  #速度与#情
# # ret = re.match("速度与.情","速度与\n情") #None
# ret = re.match("速度与.情","速度与情情abc12345") #速度与情情
# print(ret)

# [ ] ：匹配“[]”列举的字符
#案例：看电影，输入电影名称：“速度与激情”时，“速度与激情1”-“速度与激情8”都算正确的
# ret = re.match("速度与激情[12345678]","速度与激情1") #速度与激情1
# ret = re.match("速度与激情[12345678]","速度与激情a") #None
# ret = re.match("速度与激情[12345678]","速度与激情10") #速度与激情1
# ret = re.match("速度与激情[1-8]","速度与激情1") #速度与激情1
#“速度与激情6”不匹配
# ret = re.match("速度与激情[1-57-8]","速度与激情6")  #None
# ret = re.match("速度与激情[a-z]","速度与激情a")
# print(ret)

# \d：匹配数字，0-9
# 案例：看电影，输入电影名称：“速度与激情”时，“速度与激情1”-“速度与激情8”都算正确的
# ret = re.match("速度与激情\d","速度与激情6")
# ret = re.match("速度与激情\d","速度与激情#")
# print(ret)

#4.\D：匹配非数字，即不是数字
# ret = re.match("速度与激情\D","速度与激情6")
# ret = re.match("速度与激情\D","速度与激情#")
# print(ret)

# \s：匹配空格，包含空格和tab
# ret = re.match("速度与激情\s","速度与激情#") #None
# ret = re.match("速度与激情\s","速度与激情 ") #"速度与激情 "
# ret = re.match("速度与激情\s","速度与激情") #None

#\S：匹配非空格
# ret = re.match("速度与激情\S","速度与激情8") #速度与激情8
# ret = re.match("速度与激情\S","速度与激情a")  #速度与激情a
# ret = re.match("速度与激情\S","速度与激情#")  #速度与激情#
# ret = re.match("速度与激情\S","速度与激情 ")  #None
# print(ret)

# 7.\w：匹配单词字符：包含(a-z,A-Z,0-9,_)
# ret = re.match("\w","1") #1
# ret = re.match("\w","a") #a
# ret = re.match("\w","_") #_
# ret = re.match("\w","@")  #None
# ret = re.match("\w","张")

#\W:匹配非单词字符
# ret = re.match("\W","1") #1
# ret = re.match("\W","a") #a
# ret = re.match("\W","_") #_
# ret = re.match("\W","@")  #None
# ret = re.match("\W","张")
# print(ret)


# 匹配多个字符
#
# - 1.{m}：匹配前一个字符出现m次
#匹配出合法的手机号
#规则：要求满足11位，且第一位是1
# ret = re.match("\d{11}","12345678901") #12345678901
# ret = re.match("1\d{10}","32345678901") #None
# ret = re.match("1\d{10}","123ab678901") #None
# ret = re.match("1\d{10}","12345678901abc") #12345678901
# print(ret)

# 2.{m,n}：匹配前一个字符出现m到n次
# 案例：验证电话号码的合法性，如：010-1234567，0558-8080255
#规则：区号3-4位数字，电话号是7-8位数字，中间用“-连接”
# ret = re.match("\d{3,4}-\d{7,8}","010-1234567") #010-1234567
# ret = re.match("\d{3,4}-\d{7,8}","0558-8080255") #0558-8080255
# ret = re.match("\d{3,4}-\d{7,8}","0558-8080255a") #0558-8080255
# print(ret)

# ?：前一个字符出现0次或者1次，那么出现1次，那么出现0次
# 案例：验证电话号码的合法性，如：010-1234567，0558-8080255
#规则：区号3-4位数字，电话号是7-8位数字，中间用“-连接”区号和电话号，“-”可有可无
# ret = re.match("\d{3,4}-\d{7,8}","0101234567") #None
# ret = re.match("\d{3,4}-?\d{7,8}","0101234567") #0101234567
# ret = re.match("\d{3,4}-?\d{7,8}","010@1234567") #None
# print(ret)


# *：匹配前一个字符出现0次或多次
#案例：把一个文本内容全部提取出来
# content = "life is short,I use Python！"
# content = "life is short,I use\n Python！"
# ret = re.match(".*",content)
# ret = re.match(".*",content,re.S) #可以匹配多行
# ret = re.match(".*","")
# print(ret)
# print(ret.group())


# 5.+：匹配前一个字符出现1次或多次，即至少出现1次

# # ret = re.match("a+","aaaa") #aaaa
# ret = re.match("a+","") #None
# print(ret)



# 匹配开头与结尾
#
# - 1."^"：匹配开头的字符串
# ret = re.match("ujiuye","ujiuye.com")
# ret = re.search("ujiuye","www.ujiuye.com")
# ret = re.search("^ujiuye","www.ujiuye.com")
# 注意：^ 用在[]中，表示取反
# ret = re.match("速度与激情[^6]","速度与激情9")
# print(ret)

# 2."$"：匹配以xxx结尾的字符串
#案例：匹配出合法的手机号，规则：11位数字，且第一位是1
# ret = re.match("1\d{10}","12345678901abc") #匹配成功但不符合需求
# ret = re.match("1\d{10}$","12345678901abc") #None
# print(ret)


# 案例1：匹配出合法的变量名
names = ["age1","1age","AGO_","_9age","age_","a9#_2","a#ge"]
#匹配规则：字符由数字，字母，下划线组成，首字符不能是数字
# for name in names:
#     ret = re.match("[a-zA-Z_]\w*$",name)
#     if ret:
#         print("%s变量名合法"%ret.group())
#     else:
#         print("%s变量名不合法" % name)


# 案例2：匹配合法的163邮箱
#每个邮箱以“@163.com”结尾，@之前有4-20个单词字符
# email_list = ["zhangweiqinag@163.com","liu6_@qq.com","zhangwei@163.cn","xuweim@163.com.cn","liang@163ccom"]
# for email in email_list:
#     ret = re.match("\w{4,20}@163\.com$",email)
#     if ret:
#         print("%s邮箱名合法"%ret.group())
#     else:
#         print("%s邮箱名不合法" % email)


# 匹配分组
#
# - 1. |：匹配左右任意一个表达式
# email_list = ["zhangweiqinag@163.com","liu6_@qq.com","zhangwei@163.cn","xuweim@163.com.cn","liang@163ccom"]
# # 匹配出合法的163或者126或者qq邮箱
# for email in email_list:
#     ret = re.match("\w{4,20}@163\.com$|\w{4,20}@126\.com$|\w{4,20}@qq\.com$",email)
#     if ret:
#         print("%s邮箱名合法"%ret.group())
#     else:
#         print("%s邮箱名不合法" % email)

# 2.(ab)：分组
# email_list = ["zhangweiqinag@163.com","liu6_@qq.com","zhangwei@163.cn","xuweim@163.com.cn","liang@163ccom"]
# 匹配出合法的163或者126或者qq邮箱
# email = "liu6_@qq.com"
# ret = re.match("\w{4,20}@qq\.com$",email)
# ret = re.match("(\w{4,20})@qq\.com$",email)
# print(ret.group())
# print(ret.group(1))
# for email in email_list:
#     ret = re.match("\w{4,20}@(163|qq|126)\.com$",email)
#     if ret:
#         print("%s邮箱名合法"%ret.group(0))
#     else:
#         print("%s邮箱名不合法" % email)


# 3.\num 引用分组：引用分组匹配到的字符串
# 案例：检查html网页语法的合法性
#语法规则：标签必须配对
# content = "<h1>hello world</h1>"
# content = "<h1>hello world</h2>"
#不严谨的写法
# ret = re.match("<\w+>.*</\w+>",content)
#严谨的写法
# ret = re.match("<(\w+)>.*</\\1>",content)
# print(ret)


# - 4.给分组给别名 （?P<name>）
# - 5.(?P=name)：引用别名为name的分组匹配到的字符串
# content = "<h1><body>hello world</body></h1>"
# # ret = re.match("<(\w+)><(\w+)>.*</\\2></\\1>",content)
# ret = re.match("<(?P<a>\w+)><(?P<b>\w+)>.*</(?P=b)></(?P=a)>",content)
# print(ret)


# re模块的其他用法 search，findall,sub
#1.search :查看匹配的数据，匹配到立即返回
#语法和match相同
# 案例：匹配阅读次数
# content = "阅读次数88次，下载次数30次"
# ret = re.search("\d+",content)
# print(ret)

#2.findall():查找字符串中所有匹配的数据，返回的是列表
# # 案例：匹配所有的数字
# content = "阅读次数88次，下载次数30次"
# ret = re.findall("\d+",content)
# print(ret)

#3.sub ():替换，返回的是替换后的字符串
# 案例：将所有的字数归0
# content = "阅读次数88次，下载次数30次"
# ret = re.sub("\d+","0",content)
# print(ret)

# 贪婪和非贪婪

# - 1.Python中默认是贪婪，总是尝试尽可能多的匹配字符，非贪婪相反，总是尽可能少的匹配字符

# ret = re.match("\d{2,5}","12345")
# print(ret)

# re.complie(strPattern),将字符串形式的正则表达式编译成pattern对象
pattern = re.compile("\d{2,5}")
ret = pattern.match("12345")
print(ret)
