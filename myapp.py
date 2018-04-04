# coding: utf-8
#8.while文

# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# else:
#     print("end")

#9.for文

# for i in range(0,10):
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("end")

#10.関数

# def say_hi(name,age=100):
#     print("hi {0} ({1})".format(name,age))
#
# say_hi("nakamoto",19)
# say_hi("asfasf")
# say_hi(age = 18, name = "rick")

# 11.返り値

# def say_hi():
#     return "hi"
# msg=say_hi()
# print(msg)

# def say_hi():
#     pass
# msg=say_hi()
# print(msg)

# 12.変数のスコープ
# msg="hello" #グローバル変数
# def say_hi():
#     msg = "hi" #ローカル変数
#     print(msg)
# say_hi() #hi
# print(msg) #hello

# グローバル変数は関数の中から参照はできる
# msg="hello"
# def say_hi():
#     print(msg)
# say_hi() #hello
# print(msg) #hello

# グローバル変数は関数の中から書き換えはできない
# msg="hello"
# def say_hi():
#     msg="hello global"
#     print(msg)
# say_hi() #hello global
# print(msg) #hello

# #書き換えたい場合は global msgとかいてあげる
# msg="hello"
# def say_hi():
#     global msg
#     msg="hello global"
#     print(msg)
# say_hi() #hello global
# print(msg) #hello global に書き換えられている

#13 クラス

# user_name = "nakamoto"
# user_score = 10

# class User:
#     pass
#
# tom = User() #インスタンス
# tom.name = "tom"
# tom.score = 20
#
# bob = User() #インスタンス
# bob.name = "bob"
# bob.level = 5
#
# print(tom.name)
# print(bob.name)

# 14.コンストラクタ、インスタンス変数
# class User:
#     def __init__(self, name):
#         #selfはこのクラスから作られるインスタンス、nameは下で値が渡される変数
#         #インスタンス変数
#         self.name = name
#
# tom = User("tom")
# bob = User("bob")
#
# print(tom.name)
# print(bob.name)

# 15.クラス変数

# class User:
#     #クラス変数
#     count = 0
#     def __init__(self, name):
#         #クラス変数にアクセスは、「クラス名.変数名」
#         #インスタンスを作るたびに1増える
#         User.count += 1
#         #インスタンス変数
#         self.name = name
#
# print(User.count) #0
# tom = User("tom")
# bob = User("bob")
# print(User.count)#2
# #クラス変数をインスタンスからよんだ場合、同盟のインスタンス変数がない場合クラス変数が呼び出される
# print(tom.count) #2

# 16.メソッド(クラスに定義した関数)

# class User:
#     count= 0
#     def __init__(self,name):
#         User.count +=1
#         self.name = name
#     #インスタンスメソッド（インスタンス化してから使える）
#     def say_hi(self):
#         print("hi {0}".format(self.name))
#     #クラスメソッド（インスタンス化せずに使える）
#     @classmethod
#     def show_info(cls):
#         print("{0} instances".format(a.count))
#
# User.show_info() #0 instances
#
# tom = User("tom")
# bob = User("bob")
#
# User.show_info() #2 instances
# tom.say_hi()
# bob.say_hi()

# 17.アクセス制限
    # name属性を外部からアクセスして欲しくない場合、以下のように＿を1つまたは2つつけるのが慣習
# class User:
#     count= 0
#     def __init__(self,name):
#         User.count +=1
#         self.__name = name
#     def say_hi(self):
#         print("hi {0}".format(self.__name))

# 18.クラスの継承（既存のクラスを元に新しいクラスを作る仕組み）
# 親クラスUser -> 子クラスAdminUser
#
# class User:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("hi {0}".format(self.name))
#
# #継承するにはかっこの中に親クラスを入れる
# class AdminUser(User):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def say_hello(self):
#         print("hello {0}({1})".format(self.name, self.age))
#     #override 親クラスのメソッドを上書き
#     def say_hi(self):
#         print("[admin]hi {0}".format(self.name))
#
# bob = AdminUser("bob", 23)
# print(bob.name)
# bob.say_hi()
# bob.say_hello()

# 19.クラスの多重継承
# A, B ->C
# class A:
#     def say_a(self):
#         print("A!")
#     def say_hi(self):
#         print("hi! from A")
# class B:
#     def say_b(self):
#         print("B!")
#     def say_hi(self):
#         print("hi from B")
# class C(A,B):
#     pass
# c = C()
# c.say_a() #A!
# c.say_b() #B!
# c.say_hi() #hi! from A
#
# class D(B,A):
#     pass
# d = D()
# d.say_a() #A!
# d.say_b() #B!
# d.say_hi() #hi! from B

#20.モジュールでファイルを分割
#モジュールは別ファイルに書いたコード

# import user
#
# bob = user.AdminUser("bob", 13)
# print(bob.name)
# bob.say_hi()
# bob.say_hello()

#モジュールから指定した関数やクラスだけ使いたい時
# from user import AdminUser,User
# bob = AdminUser("bob", 13)#この場合user.はいらない
# print(bob.name)
# bob.say_hi()
# bob.say_hello()

# 21.パッケージでモジュールを管理
# import mypackage.user
# bob = mypackage.user.AdminUser("bob",23)
# import mypackage.user as mymodule
# bob = mymodule.AdminUser("bob",23)
# from mypackage.user import AdminUser
# bob = AdminUser("bob", 23)
#
# print(bob.name)
# bob.say_hi()
# bob.say_hello()

# 22.例外処理

# def div(a,b):
#     print(a/b)
# div(10,0) #ZeroDivisionError

# def div(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("not by 0!!")
#     else: #例外が発生しなかった場合
#         print("no exception")
#     finally: #例外があるかないいか関わらず
#         print("end")
# div(3,2)
# div(10,0) #not by 0!!

#独自の例外を作りたい場合

# class MyException(Exception):
#     pass
#
# def div(a,b):
#     try:
#         if (b < 0):
#             raise MyException("not minus")
#         print(a/b)
#     except MyException as e:
#         print(e)
# div(3,-2) #not minus

# 23.リスト型
# scores = [40,50]
# print(scores[0])
# scores[0]=45
# print(len(scores)) #2
# scores.append(100)
# print(scores)

# for score in scores:
#     print(score)

#何番目も知りたい場合enumerateが使える
# i:何番目か score:内容
# for i, score in enumerate(scores):
#     print("{0}:{1}".format(i,score))

# 24.タプル
#順序の値だが、値の変更はできない
# items = (50, "apple", 32.5)
# print(items[1])
# items[1] = "pen" #書き換えはできないからエラー

# タプルとリストは変換可能
# print(list((1,2,3)))
# print(tuple([2,3,4]))

# 25.スライス
# scores = [40,50,70,90,60]
# print(scores[1:4]) #１−３番目 50,70,90
# print(scores[:2]) #0-1番目
# print(scores[3:]) #3-最後
# print(scores[-3:]) #末尾から3番目のところから最後まで #70 90 60

##文字列でもスライス可能
# s="hello"
# print(s[1:4]) #ell

# # 26.セット（集合型）
# # 順番なし、重複ダメ
#
# # a = set([5,4,8,5])
# a = {5,4,3,5} #最後の5は重複してるので無視される
# print(a) #{3,4,5}
# # ある要素が含まれているかどうか調べる
# print(5 in a ) #True
# # 要素の追加・削除
# a.add(2)
# a.remove(3)
# print(a)
# #要素の数
# print(len(a))
#
# #集合演算もできる
# a = {1,3,5,8}
# b = {3,5,8,9}
# print(a | b) #和集合
# print(a & b) #積集合
# print(a - b) #差集合

# # 27.辞書型
#
# sales = {"nakamoto": 200, "tanaka":400}
# # print(sales["nakamoto"])
# # sales["nakamoto"]=500
# # # 要素の追加
# # sales["tom"] = 540
# # #要素の削除
# # del(sales["tanaka"])
# # print(sales)
#
# # items()メソッドでキーと値両方とり出せる
# for key, value in sales.items():
#     print("{0}:{1}".format(key, value))

# 28,イテレータ（次の要素を返してくれるデータの集合） iter next
# scores = [1,2,3,4,5,6,7,8]
# it = iter(scores)
# print(next(it)) #1
# print(next(it)) #2
# print("hi")
# print(next(it)) #3

#listからでなく0からでもイテレータ作れる！
#以下のようなイテレータを作る関数をジェネレータという
# def get_infinite():
#     i = 0
#     while True:
#         yield i*2
#         i += 1
# g = get_infinite()
# print(next(g)) #0
# print(next(g)) #2
# print(next(g)) #4
# print(next(g)) #6

# 29.mapとlambda
# map(関数,イテレータ)
# def triple(n):
#     return n*3
#
# print(list(map(triple, [1,2,3]))) #[3,6,9]

#lambda 引数: 処理
# print(list(map(lambda n: n*3, [1,2,3]))) #[3,6,9] tripleいらない

# 30.filter()
# filter(関数,イテレータ)

# def is_even(n):
#     return n % 2 == 0
#
# print(list(filter(is_even, range(10)))) #[0, 2, 4, 6, 8]
#
# #lambda使う場合
# print(list(filter(lambda n : n % 2 == 0, range(10)))) #[0, 2, 4, 6, 8]

# 31.内包表記
# リストやジェネレータを生成、加工するときに書く記法

# mapより簡潔に書ける！
#0-9
print([i for i in range(10)]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#後ろから読んで行く。range(10)から1ずつ要素を取り出してiに入れて、をれをそのままiとして取り出す
print([i*3 for i in range(10)]) #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# filterみたいにも使える！
print([i*3 for i in range(10) if i % 2 == 0]) #[0, 6, 12, 18, 24]

# ジェネレータや集合型にもできる
print((i*3 for i in range(10) if i % 2 == 0)) #ジェネレータ
print({i*3 for i in range(10) if i % 2 == 0})#集合型
