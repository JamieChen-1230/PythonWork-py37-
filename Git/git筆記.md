# Git筆記

[![hackmd-github-sync-badge](https://hackmd.io/EQdno6aHSdSrCOnFk2IGwg/badge)](https://hackmd.io/EQdno6aHSdSrCOnFk2IGwg)


## 基礎使用

### 版本控制重要性：
1. 可以備份代碼
2. 可以保護彼此的代碼不會被覆蓋後找不回來
3. 可以透過指令輕易比較出文件的修改
4. 可以輕易的切換回舊版本
5. 團隊開發時能保持代碼的一致性

### Git原理：
- HASH(哈希、雜湊)算法：
    - 分為Hash Function(雜湊函數)和Hash Table(雜湊表)
        - 雜湊函數：
            - 是一種將輸入值映射到另一個值域的技術。
            - 不管多長的明文透過雜湊函數後，得出的密文長度皆一致。
            - 這種轉換有一個很重要的特性就是「單向」。(不可藉由HASH輸出值推導回原值)
        - 雜湊表：
            - 儲存(Key,Value)這種對應關係的資料結構。
            - key為原始輸入，value為經過雜湊函數的輸出值。
            - 衝突(Collision)： 當不同的原始輸入，經過雜湊函數後，卻得到相同輸出值，這時就會產生衝突。
    - Git底層的雜湊函數是採用SHA-1。
    
- 保持資料完整性：
    - 先將原始文件經過SHA-1，轉為一個密文。
    - 網路傳輸(上傳或下載等)
    - 把上傳的資料經過SHA-1轉為另一個密文，兩個密文互相比較，有不同則表示數據有丟失。

- 保存版本機制：
    - 快照：
        - 快照並不是整個項目文件夾的副本，快照僅僅是一個記錄文件結構的文檔。
        - 就像是版本資訊對象，每個對象都會有一個編號，透過這個編號我們可以進行git reset等操作。
    - 物件：
        - 用來保存版本庫中所有檔案與版本紀錄。
        - 物件是一個「特別的檔案」，將檔案的內容中取出，透過內容產生一組SHA1雜湊值，然後依照這個SHA1雜湊值命名的一個檔案。
        - 物件又分為「目錄資訊」與「檔案內容」，我們稱為 tree 物件與 blob 物件：
            blob 物件：就是SHA1雜湊值為名稱的檔案。
            tree 物件：儲存特定資料夾下包含哪些檔案，以及該檔案對應的 blob 物件的檔名為何。(簡單的說就是資料夾的概念)
        - 每一個快照(版本對象)中可以包含多個tree和blob物件。
    - 索引：
        - 則是用來保存當下要進版本庫之前的目錄狀態。
        - 「索引」是一個經常異動的暫存檔，這個檔案通常位於 .git目錄下的一位名為 index 的檔案。
        - 用來紀錄有哪些檔案即將要被提交到下一個 commit 版本中。
        - 索引流程：
            1. 要使用 Git 版本控管，必須透過git init先建立「版本庫」。
            2. 在「工作目錄區」進行開發(建立目錄、建立檔案、修改檔案、刪除檔案等操作)。
            3. git add, git mv等操作會將「物件」的索引從工作區添加到暫存區(或是索引區)裡。
            4. git status依據「索引」當下的狀態，顯示哪些變更的檔案在暫存區或工作區裡。
            5. git commit 會提交變更，把版本資訊寫入到「版本庫」當中，並把分支指針指向此快照(版本對象)。
- 管理分支機制：
    - 每個分支都是一個「指針」(包含master等)，他會指向版本對象。
    - 創建一個分支，只是相當於新建了一個指針，並指向一個版本對象，而並非是創造所有文件的副本。
    - HEAD是一個特殊的指針，他是會指向當前使用的分支，這樣就能控制哪個分支要進行修改。


### Git和Github的區別：
- Git：
    是一個分佈式版本控制系統。
    (簡單的說就是一個軟件，用於記錄文件變化，以便來查閱特定版本修訂情況。)
- Github：
    是一個為用戶提供Git服務的網站。
    (簡單說就是一個可以放代碼的地方。Github除了提供管理Git的web界面外，還提供了訂閱、關注、討論組在線編輯器等豐富的功能。)

### Git本地操作的三個區域：
- 工作區：我們平時存放和操作代碼的目錄位置。
- 暫存區：暫時存取我們要從工作區傳到倉庫的文件。
- (本地)倉庫區：最後決定要真正要保存到倉庫的文件，並成為一個新的版本。
    - 倉(版本)庫可理解為一個目錄，裡面的文件記錄著各種信息，而每個文件的修改Git都會進行追蹤並記錄，以便之後的追踪或還原。
        - 版本庫創建： git init => 創建了一個隱藏的.git目錄當作版本庫

&emsp;
## 本地操作

### (全局配置)登入Git，讓大家知道這是誰傳的更新：
    ※ 建議寫GitHub的郵箱和用戶名
    git config --global user.email as124122323@gmail.com
    git config --global user.name silencejammie

### 查詢目前郵箱和用戶名：
    git config --global user.name
    git config --global user.email

### Git倉庫的初始化(即讓Git知道需要他來管理這個目錄)：
    git init  =>  創建了一個隱藏的.git目錄當作版本庫

### 查看當前倉庫的操作狀態：
    git status  =>  查看目前所有文件狀態

### 添加文件到暫存區：
    git add readme.txt readme2.txt  =>  告訴Git我想要把此文件添加到暫存區
    git add .  =>  告訴Git我想要把「當前目錄的所有文件」添加到暫存區

### 提交暫存區中的文件至版本庫：
    ※ 註釋要寫的精簡且易懂。
    git commit -m "這邊寫註釋"  =>  告訴Git把此文件提交到(本地)版本庫

### 查看版本日誌：
    git log  =>  顯示每一次commit的信息(id, author, date)，便於我們找出要回滾的版本
    git log --pretty=oneline  => 【推薦】顯示每一次commit的信息(只有id)
### 查看包括所有的提交與回滾紀錄的版本日誌：
    git reflog  =>  若後悔回滾的話的補救方法

### 回滾(撤回、退回)：
#### 指令：
- git reset --hard HEAD   =>  回復到最新提交版本
- git reset --hard HEAD^  =>  回滾到上一個版本
- git reset --hard HEAD~3  =>  回滾到往前推第三個版本
- git reset --hard fc25e782315b0a3f1674c78dabc081f2e29052cc  
    =>  回滾到此id(輸入前7碼即可)的版本，只要有id就能回滾，相當於 git reset --hard fc25e78
#### reset參數：
- --hard：
    - 跳到指定的 commit，檔案狀態：取消所有變更(※ 表示工作目錄中修改的檔案不會保留，直接刪除修改部分)
    - 在本地倉庫移動HEAD指針，且重置暫存區和工作區
- --mixed：
    - 跳到指定的 commit，檔案狀態：保留所有變更，變更不會幫你add(※ 表示工作目錄中修改的檔案還在，但不會幫你先add起來)
    - 在本地倉庫移動HEAD指針，且重置暫存區
- --soft：
    - 跳到指定的 commit，檔案狀態：保留所有變更，變更會自動幫你add(※ 表示工作目錄中修改的檔案還在，且會幫你先add起來)
    - 僅僅在本地倉庫移動HEAD指針

### 文件比較：
※ 若還沒被添加到倉庫的文件不會被比較
#### 目前工作區和暫存區的比較
    git diff
#### 目前工作區和倉庫HEAD的比較
    git diff HEAD
#### 暫存區和倉庫HEAD的比較
    git diff --cached
#### 兩個版本間的文件比較
    git diff <舊的版本> <新的版本>
    範例：
        git diff HEAD^ HEAD
        git diff HEAD^..HEAD  => 可以用..分開，更容易識別
        git diff 8008a9d..HEAD

### 小結：
- 工作資料夾 --add--> 暫存區 --commit--> 本地倉庫。
- 要想回到過去必須要有commit_id(透過git log查看)，並使用 git reset --hard commit_id 來回到過去。
- 要想回到未來，必須透過 git reflog 查看已被回滾的commit_id，再來使用 git reset --hard commit_id 來回到未來。
- commit_id 至少輸入前7碼會比較穩。

&emsp;
## 遠程操作：
#### 遠端版本庫地址別名：
- 檢視遠端版本庫的地址「別名」：
    - ※ 如果你clone了一個遠端版本庫，你至少看得到一個「origin」(它是Git的預設簡稱，用來代表被克隆的來源)。
    - git remote -v
-  新增遠端版本庫地址別名：
    - git remote add <別名> <網址>
        - git remote add origin https://github.com/JamieChen-1230/PythonWork-py37-.git
- 檢視遠端別名：
    - git remote show <別名>
        - git remote show origin
- 刪除別名：
    - git remote remove <別名>

#### 拉取並更新本地代碼：
- pull 相當於 fetch + merge
- 拉取遠程代碼：
    - git fetch <遠端主機名> <遠端分支名>
        - git fetch origin master
    - git fetch通常用來檢視其他人的程序，因為它取回的程式碼對本地代碼不會有影響
    - 欲查看所取回的代碼，需要checkout到本地的<遠端主機名/分支名>的分支查看
        - git checkout origin/master
- 合併拉取的遠程代碼：
    - 先切換到想要合併更新的分支上
        - git checkout master
    - git merge <遠端主機名/分支名>
        - git merge origin/master
- 拉取並合併遠程代碼：
    - 通常如果更改的不多，可以就直接用pull就好；但如果更改的較多且複雜，可以先用fetch評估是否要合併。
    - git pull <遠端主機名> <遠端分支名>:<本地分支名>
        - 抓取遠端的next分支，並合併到本地的master分支
            - git pull origin next:master
        

#### 推到遠程倉庫：
- 完整使用：
    - git push <遠程主機名> <本地分支名>:<遠程分支名>
        - 將本地的某分支推到遠程主機的某分支
    - git push origin HEAD:master
        - 將當前分支推到遠程的master分支
- 不完整使用(容易搞混)：
    - git push origin master
        - 代表的是將本地的master分支推到遠程的master分支
        - 而不是將本地的目前所在分支推到遠程的master分支
    - git push origin HEAD
        - 將本地的當前分支推到遠程的同名分支
    - git push origin :master
        - 推送一個空的本地分支到遠程master分支
        - 所以等同於刪除了遠程master分支
- 默認使用：
    - git push -u origin master
        - 使用-u，建立默認推送關係
        - 所以以後使用git push，就相當於git push origin master
- 其他使用：
    - git push --all origin
        - 不管是否存在對應的遠程分支，將所有本地分支都推送到origin主機
    - git push --force origin
        - 正常情況下，如果遠程主機的版本比本地版本更新，推送時Git會報錯，要求先在本地做git pull合並差異，然後再推送到遠程主機
        - 但如果要無視版本直接推送的話，就要使用force
        - 很危險，不建議使用

&emsp;
## 使用遠程倉庫(以 Github 為例)
### 兩種常規使用方式：
#### 一、基於https協議：
- (1) 先到要存放目錄的位置(cd D:\Programming\WorkPlace\PythonWork(py37)\Git)。
- (2) clone遠程倉庫到本地(後面的網址為遠程倉庫的地址)：
    - git clone https://github.com/silencejamie/git_demo.git
        => 會產生了一個跟遠程倉庫相同命名的資料夾            (D:\Programming\WorkPlace\PythonWork(py37)\Git\git_demo)，
       裡面帶著所有代碼和.git版本庫。
- (3) 之後這個資料夾就會變成所謂的工作區(工作目錄)，裡面可以做任何的本地git操作。
- (4) 本地操作完後，提交到遠程倉庫：
    - 1. 如果是首次提交，首先應獲取權限(否則會出現403的錯誤)。
        - 獲取權限(修改.git/config文件中的url字段)：
            - 舊的：https://github.com/silencejamie/git_demo.git
                在github.com前面加上「用戶名:密碼@」
            - 新的：https://username:password@github.com/silencejamie/git_demo.git
    - 2. 先更新本地端代碼(因為有可能別人已先在遠程倉庫中新增了新的代碼)：
        - ※ 如果git pull時，工作目錄中有一些修改未提交到版本庫，此時禁止git pull，
        - ※ 需要先在工作區和版本庫中做一些一致性調整(要麼將工作目錄的修改提交到版本庫，要麼捨棄工作目錄的修改)。
        - git pull
    - 3. 提交本地倉庫至遠程倉庫(但通常要push前最好先git pull，才不會造成遠程倉庫版本混亂)：
        - git push <遠程主機名> <本地分支名>:<遠程分支名>
        - EX: git push -u origin master:master
            - -u表示他會記住我們現在傳遞的倉庫分支，這樣之後執行單git push就能達到同樣效果

#### 二、基於ssh協議(要額外使用生成公私鑰的套件)：
- 影片教學：https://www.bilibili.com/video/BV1sJ411D7xN?p=12
- 具體實現在 https://blog.csdn.net/jiahuan_/article/details/105933423

&emsp;
## 分支操作(本地)
### 分支的優點：
    - 可同時並行進行多個功能開法，提高效率。
    - 在開發過程中，若分支開發失敗，也不會影響到主分支和其他分支。(分支彼此是獨立的)

### 查看分支(*代表當前分支)：
    - git branch
    - git branch -v   =>   會顯示更多信息

### 創建分支(在哪個分支上創建分支，就會以該分支為基礎創建)：
    ※ 創造分支的當下主分支和子分支的內容是相同的
    git branch <分支名>
### 刪除分支(要被刪的分支不能處於使用中)：
    git branch -d <分支名>

### 切換分支：
    git checkout <分支名>
    git checkout -b <分支名>  =>  創建並切換分支

### 合併分支：
#### ※ 不同分支之間是互不影響的。
    EX：在新的分支裡添加完並commit到本地倉庫後，再切回master分支，會發現工作目錄下剛剛在分支更改的東西消失了。
        => 所以才需要合併分支。
#### ※ 要先切換到欲合併其他分支的主分支下。
    git checkout xxx
    git merge <分支名>
#### 參數：
    --no-ff：這會為merge操作新創建一個commit，而不是只是指向被合併分支最後的commit
    範例：git merge <分支名> --no-ff
#### 分支類型(通常會這樣分)：
- Master主分支： 
    - 只負責管理發布的狀態，當準備好發佈指定版本(EX: Version1, Version2等)時，最後的提交會給予一個發布版本標籤。
- Develop主分支： 
    - 針對日常開發的分支，所有新功能開發最終都會合併到這裡。
- Feature(Topic)分支：
    - 這個分支是新功能的開發或修復錯誤的時候從 develop 分支分開出來的。
    - Feature分支的操作基本上不需要共享，所以不需要在遠端數據庫建立分支，當完成開發後，合併回 develop 分支後發布。
- Release分支：
    - 一般開發是在develop分支上進行，到了快要發布時候才會建立release分支，release分支主要是做發布前最後錯誤修復所建立的分支。
    - 通常這種分支的名稱最前面會加上"release-"。
- Hot fix分支： 
    - 分支是在發布的產品需要緊急修改時，從 master 分支建立的分支。(通常會在分支名稱的最前面會加上"hotfix-")

&emsp;
## git bush的vim編輯器
    按Esc：
        退出輸入模式，並進入到命令行模式(也是系統默認模式)。
    o, i, a：
        都可以從命令行模式進入到輸入模式。
    :wq：
        在命令模式下輸入 :wq，代表保存修改並且退出vim編輯器。
    :w：
        如果只想保存文件，則輸入 :w。回車後底行會提示寫入操作結果，並保持停留在命令行模式。
    :q!：
        在命令模式下輸入 :q!，代表放棄所有修改並退出。
    :e!：
        放棄所有修改，但不退出，回車後回到命令模式。


&emsp;
## 衝突的產生與解決
### 案件一：同事在更改了遠端倉庫，但我在操作本地倉庫前沒有使用git pull先更新本地代碼(且更改的是相同文件)。
- 衝突原因：
    - 在本地與遠端倉庫不一致的情況下直接更改本地內容(且更改的是相同文件)。
- 在git push遇到的錯誤：
    - error: failed to push some refs to 'https://silencejamie:jamie851230@github.com/silencejamie/git_demo.git'
- 解決方法：
    - (1) 先git pull。
        - 這時還沒有成功，打開衝突文件後會發現他會把衝突的地方標記出來，並標註是誰(commit_id)改的。
        - ※ 會顯示在哪裡起了衝突  =>  CONFLICT (content): Merge conflict in readme.txt
    - (2) 去詢問這是誰改的，並討論該留哪些代碼。
    - (3) 把改好的文件再重新提交到本地倉庫，最後push到遠端即可。


### 案件二：同案例一(但是更改的為不同的文件)。
- 衝突原因：
    - 在本地與遠端倉庫不一致的情況下直接更改本地內容(但更改的是不同的文件)。
- 在git push遇到的錯誤(同案件一)：
    - error: failed to push some refs to 'https://silencejamie:jamie851230@github.com/silencejamie/git_demo.git'
- 解決方法：
    - (1) 先git pull。
        - 這時會自動進入vim編輯器，要我們編寫本次merge的文檔。
    - (2) 編輯完文檔後，Git會自動幫我們merge起來。
    - (3) 最後再push即可。

### 案件三：若自己在本地端遇到master分支和子分支同時修改了同一個檔案並都提交到本地倉庫中，接下來要merge兩個分支會遇到衝突。
- 衝突原因：
    - 兩個分支下同時修改同個文件的內容
- 解決方法：
    - (1) Git會提示我哪個文件發生衝突了，並在衝突文件中顯示衝突點
    - (2) 修改那個文件，保留自己想要的
    - (3) 添加到本地倉庫(add和commit)

&emsp;
## 忽略文件
#### 在上傳時忽略掉某些文件(讓一些文件不上傳到遠程倉庫)：
- (1) 在工作目錄中建立 .gitignore 文件：
    - touch .gitignore
- (2) 編寫 .gitignore 文件。
    - 常用規則如下：
        1. 過濾整個資料夾      /mtk/
        2. 過濾所有.zip文件    *.zip
        3. 過濾某个具體文件    /mtk/a.txt
        4. 不過濾具體某个文件  !index.php

&emsp;
## 觀念釐清
### 觀念一： git init 和 git init --bare 的區別
#### git init：
- 創建了一個「Git普通庫」
- 目錄下有一個.git隱藏目錄，裏面包含各種信息，除了.git目錄之外，還可以看到庫中所包含的所有源文件，相當於擁有一個可以進行瀏覽和修改（添加，提交，刪除等）的本地庫(有工作目錄)
- 比較不適合作為遠端公共倉庫，因為當我們從本地git push到遠端普通庫時，可能會遇到遠端普通庫這正在用此分支，導致push不成功
#### git init --bare：
- 創建了一個「Git裸庫」
- 目錄下只有一個.git目錄，而沒有本地庫那樣的文件結構可以直接進行瀏覽和修改(沒有工作目錄)
- 主要應用場景是作為公共倉庫、遠端備份
- 慣用的命名方式是在庫名後加上.git
    - 範例：
        mkdir example.git 
        cd example.git 
        git init --bare

### 觀念二： 團隊開發中使用Git的基本流程
#### 文字敘述：
1. 克隆遠程版本庫
2. 基於遠程的develop分支建立本地的develop分支
3. 基於develop的分支建立本地特性分支feature
4. 在feature分支中編寫程序
5. 要提交前，先切換到develop分支，合併feature的修改
6. 把本地的develop分支的修改推到遠程的develop
#### 範例：
1. 克隆遠程版本庫
    - 在master分支
        - git clone git@github.com:christian-tl/git-demo.git
2. 基於遠程的develop分支建立本地的develop分支
    - 在master分支
        - cd git-demo
        - git checkout -b develop origin/develop
3. 基於develop的分支建立本地特性分支feature
    - 在develop分支
        -  git checkout -b feature develop
4. 在feature分支中編寫程序
    - 在feature分支
        - vim a.txt
        - git add a.txt
        - git commit -m "add a.txt"
5. 要提交前，先切換到develop分支，合併feature的修改
    - 在feature分支
        - git checkout develop
    - 在develop分支
        - git pull
        - git merge feature
6. 把本地的develop分支的修改推到遠程的develop
    - 在develop分支
        - git push



###### tags `GIT`