"""
整理：
    - 元(特殊)字符：
            .：代表一個任意字符(除了\n等符號)
            ^：代表匹配字串須為字符串的開頭
            $：代表字符串須為字符串的結尾
            *：重複符號(代表0到無窮次)
            +：重複符號(代表1到無窮次)
            ?：重複符號(代表0或1次)
            {x,y}：重複符號(範圍自訂)，不給參數代表無窮，且參數間不可有空格
            [ ]：字符集，裡面不能有元(特殊)字符，只能有 -到、^not、\轉義
            \ ：轉義符，能讓有意義變沒意義，能讓沒意義變有意義
                    \d：代表[0-9]
                    \D：代表[^0-9] => 非0-9
                    \s：代表[空格\t\n\r\f\v] (空白符)
                    \S：代表[^\t\n\r\f\v]  => 非 空格\t\n\r\f\v
                    \w：代表[a-z0-9A-Z_]
                    \W：代表[^a-z0-9A-Z_]  => 非 a-z0-9A-Z_
            |：代表或(or)，找多個值
            ( )：代表分組
                    (?:)：只識別，不取值
                    (?P<name>[a-z]+)：分組命名
    - 方法：
            findall：匹配所有並返回一個陣列
            search：找第一個符合字符串並返回一個對象
            match：只匹配字符串開頭並返回一個對象
            split：分割並返回一個陣列
            sub：替代並返回一個字串
            subn：替代並返回一個元組(字符串和替換個數)
            finditer：匹配所有並返回一個跌代器對象
"""

# 正則表達式，只對字符串進行處理
# 元(特殊)字符 .^$*+?{}[]|()\
import re
# . 一個任意字符(除了\n等)
# print(re.findall("s..b", "fffsd\nblkfks\kbsaab"))  # => ['s\\kb', 'saab']

# ^ 匹配字符串須為字符串的開頭
# print(re.findall("^s..b", "fffsddblkfksdkb"))  # => []
# print(re.findall("^s..b", "sddblkfksdkb"))  # => ['sddb']

# $ 匹配字符串須為字符串的結尾
# print(re.findall("s..b$", "fffsddblkfksdkbb"))  # => []
# print(re.findall("s..b$", "fffsddblkfksdkb"))  # => ['sdkb']

# * 重複符號(0到無窮次)
# print(re.findall("d*", "asdddddddasda"))  # => ['', '', 'ddddddd', '', '', 'd', '', '']
# print(re.findall("jami*e", "ddjamiiiiieee"))  # => ['jamiiiiie']，i可以有0到無窮個
# print(re.findall("jami*e", "ddjameee"))  # => ['jame']

# + 重複符號(1到無窮次)
# print(re.findall("d+", "asdddddddasda"))  # => ['ddddddd', 'd']
# print(re.findall("jami+e", "ddjamiiiiieee"))  # => ['jamiiiiie']，i可以有1到無窮個
# print(re.findall("jami+e", "ddjameee"))  # => []

# ? 重複符號(0到1次)
# print(re.findall("jami?e", "ddjamiiiiieee"))  # => []
# print(re.findall("jami?e", "ddjameee"))  # => ['jame']
# print(re.findall("jamie?", "ddjamieee"))  # => ['jamie']

# {} 重複符號(範圍自訂)，不給參數代表無窮，且參數間不可有空格
# print(re.findall("jami{1,8}e", "ddjamiiiiieee"))  # => ['jamiiiiie']，i可以出現1到8次

# [] 字符集，裡面不能有元字符，只有 -到 ^not \轉義
# print(re.findall("w[b,nb]", "wsbxhzhxf"))  # => []，裡面沒有wb w, wn wb
# print(re.findall("x[yz]", "xzdasadxy"))  # => ['xz', 'xy']，y或z都可以
# print(re.findall("q[a-z]", "qwqfsfsfkqoqfkl"))  # => ['qw', 'qf', 'qo', 'qf']，字符集a到z都可，字符集內的-代表到
# print(re.findall("q[a-z]*", "qwqfsfsfkqoqfkl"))  # => ['qwqfsfsfkqoqfkl']
# print(re.findall("q[^a-z]", "qwqfsfsfkqoqfkl"))  # => []，字符集內的^代表not
# print(re.findall("q[^a-z]", "q44wqfsfsfkqoqfkl"))  # => ['q4']
# print(re.findall("q[^ab]", "qaqbqkldjglq^"))  # => ['qk', 'q^']
# print(re.findall("q[\^ab]", "qaqbqkldjglq^"))  # => ['qa', 'qb', 'q^']，\有意義的^變沒意義

# \ 轉意符，能讓有意義變沒意義，能讓沒意義變有意義
# # print(re.findall("(", "j(h9h"))  # => error
# print(re.findall("\(", "j(h9h"))  # => ['(']，讓(變沒意義
# print(re.findall("\d", "ff454f54f"))  # => ['4', '5', '4', '5', '4']，\d變為[0-9]
# print(re.findall("\D", "ff454f54f"))  # => ['f', 'f', 'f', 'f']，\D變為[^0-9]
# print(re.findall("\s", "ff45\t4f 54f\n"))  # => ['\t', ' ', '\n']，\s變為[空格\t\n\r\f\v] (空白符)
# print(re.findall("\S", "ff45\t4f 54f\n"))  # => ['f', 'f', '4', '5', '4', 'f', '5', '4', 'f']，\S變為[^\t\n\r\f\v]
# print(re.findall("\w", "\t4f_54f\n"))  # => ['4', 'f', '_', '5', '4', 'f']，\w變為[a-z0-9A-Z_]
# print(re.findall("\W", "\t4f_54f\n"))  # => ['\t', '\n']，\W變為[^a-z0-9A-Z_]
#
# print(re.findall("I", "Hello I am LIST"))  # => ['I', 'I']
# # \b代表一個特殊字符(空白, #, @, &等)
# print(re.findall("I\b", "Hello I am LIST"))  # => []，但因為\b本身在python解釋器中就有意義，所以無法被re調用
# print(re.findall("I\\b", "Hello I am LIST"))  # => ['I']，python解釋器中\\代表"\"，這樣就變成了"\b"
# print(re.findall(r"I\b", "Hello I am LIST"))  # => ['I']，字符串前加r代表原生字符串，表示字符串內的內容都只是文字，不賦予轉意

# | 或，找多個值
# print(re.findall(r"ka|b", "asdkalblb"))  # => ['ka', 'b', 'b']，找ka和b

# () 分組
# print(re.findall(r"abc+", "abccccc"))  # => ['abccccc']
# print(re.findall(r"(abc)+", "abccccc"))  # => ['abc']
# (?:) 只識別，不取值
# print(re.findall("(?:abc)+", "abcabcabc"))  # => ['abcabcabc']，使用?:去掉分組的優先權
# print(re.findall("(?:a)(bc)", "abcabcbbc"))  # => ['bc', 'bc']
# 有命名的分組
# print(re.search("(?P<name>[a-z]+)\d+", "jamie123sb123").group())  # => jamie123，?P<name>用來命名
# print(re.search("(?P<name>[a-z]+)\d+", "jamie123sb123").group("name"))  # => jamie，只取出name的值
# # print(re.findall("(?P<name>[a-z]+)\d+", "jamie123sb123").group("name"))  # => error，list沒有group屬性
# print(re.search("(?P<name>[a-z]+)(?P<age>\d+)", "jamie123sb123").group("age"))  # => 123，只取出age的值

# search 找第一個符合字符串並返回一個對象
# print(re.search("\d+", "fasf5fafas5f46af5"))  # => <_sre.SRE_Match object; span=(4, 5), match='5'>，匹配成功返回一個對象
# print(re.search("\d+", "fasf5fafas5f46af5").group())  # => 5，.group()返回值

# match 只匹配字符串開頭
# print(re.match("\d+", "fasf5fafas5f46af5"))  # => None
# print(re.match("\d+", "11fasf5fafas5f46af5"))  # => <_sre.SRE_Match object; span=(0, 2), match='11'>

# split 分割
# print(re.split(" ", "I am Jamie"))  # => ['I', 'am', 'Jamie']
# print(re.split("[ |]", "I am|Jamie"))  # => ['I', 'am', 'Jamie']
# print(re.split("[ab]", "asdabcd"))  # => ['', 'sd', '', 'cd']

# sub 替代
# print(re.sub("\d+", "數字", "a123b4c"))  # => a數字b數字c
# print(re.sub("\d+", "數字", "a123b4c", 1))  # => a數字b4c，只替換第一個

# subn 回傳替代後字符串和替換個數
# print(re.subn("\d+", "數字", "a123b4c"))  # => ('a數字b數字c', 2)

# compile 編譯
# d = re.compile("\d+")
# print(d.findall("a123b4c"))  # => ['123', '4']，不用加條件了

# finditer 返回的是一個跌代器對象
# res = re.finditer("\d", "a123b12c")
# print(res)  # => <callable_iterator object at 0x000001FC521D2E48>
# print(res.__next__().group())  # => 1

# ()優先問題
# ---findall有優先級問題---
# 範例一
# https://www.crifan.com/python_re_search_vs_re_findall/
# print(re.findall("www\.(mail|edu)\.tw", "11www.mail.tw55"))  # => ['mail']，只會顯示分組內的東西，因為他默認優先權較高
# print(re.findall("(www\.(mail|edu)\.tw)", "11www.mail.tw55"))  # => [('www.mail.tw', 'mail')]
# print(re.findall("www\.(?:mail|edu)\.tw", "11www.mail.tw55"))  # => ['www.mail.tw']，使用?:去掉分組的優先權
# 範例二
# print(re.findall("(abc)+", "abcabcabc"))  # => ['abc']
# print(re.findall("(?:abc)+", "abcabcabc"))  # => ['abcabcabc']
# print(re.findall("(abc)+", "abcabcabc123abc"))  # => ['abc', 'abc']
# print(re.findall("(?:abc)+", "abcabcabc123abc"))  # => ['abcabcabc', 'abc']
# ---search沒有優先級問題---
# print(re.search("www\.(mail|edu)\.tw", "11www.mail.tw55").group())  # => www.mail.tw，search沒有優先級問題
# ---finditer沒有優先級問題---
# res = re.finditer("www\.(mail|edu)\.tw", "11www.mail.tw55")
# print(next(res).group())  # => www.mail.tw，finditer沒有優先級問題

