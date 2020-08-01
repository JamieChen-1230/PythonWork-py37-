/*
JavaScript跟Python一樣擁有動態類型，味著相同的變量可用作於不同的類型
*/
let x;
console.log(x);  // => undefined
x = 1;
console.log(x);  // => 1
x = 'jamie';
console.log(x);  // => jamie


/*
字符串(String):
    - 常用的轉義字符: \n:換行  \':單引號  \":雙引號  \\:右劃線
    - 可以使用''或""包字串值
*/
let str="\u4f60\u597d\n歡迎來到\"JavaScript世界\"";
console.log(str);  // => 你好
                   //    歡迎來到"JavaScript世界"
console.log(typeof str);  // => String
console.log(str.length);  // => 21
// ----------字符串的方法----------
let str1='hello';
// 編排方法(不常用)
console.log(str1.italics());  //=> <i>hello</i>
console.log(str1.anchor());  //=> <a name="undefined">hello</a>
console.log(str1.bold());  //=> <b>hello</b>
// 大小寫轉換
console.log(str1.toLocaleLowerCase());  //=> hello
console.log(str1.toUpperCase());  //=> HELLO
// 獲取指定字符
let str1_x = str1.charAt(4);
console.log(str1_x);  //=> o
// 查詢索引
let str1_y = str1.indexOf('l');  // 找第一個l
let str1_y2 = str1.lastIndexOf('l');  // 找最後一個l
console.log(str1_y);  //=> 2
console.log(str1_y2);  //=> 3
// 擷取字符串
console.log(str1.substr(1, 3));  //=> ell，從第1個位置抓3個字符
console.log(str1.substring(1, 3));  //=> el，從第1個位置取到第(3-1)個位置
console.log(str1.slice(1, 3));  //=> el，從第1個位置取到第(3-1)個位置
// 替代字符串
console.log(str1.replace('l', 'x'));  //=> hexlo，只替代第一個(根據字符串替代)
console.log(str1.replace(/l/, 'x'));  //=> hexlo，只替代第一個(使用正則)
console.log(str1.replace(/l/g, 'x'));  //=> hexxo，替代所有(使用正則)
// 分割字符串
console.log(str1.split('l'));  //=> (3) ["he", "", "o"]


/*
數字(Number):
    - JS中只有一種數據類型(不區分整型數值和浮點型數值)
    - 16進制數據: 前面加上0x
    - 8進制數據: 前面加上0
    - 指數: <數值>e<次方>
*/
let num1 = 34
let num2 = 34.01
let num8 = 034
let num16 = 0x34
let nume = 34e5
let nume2 = 34e-5
console.log(num1, num2, num8, num16, nume, nume2);  // => 34 34.01 28 52 3400000 0.00034


/*
布林值(Boolean):
    - true或false
    - 0為false
*/
if(0){
    console.log('T');
}else{ console.log('F'); }  // => F


/*
數組(Array):
    - 數組下標是基於零的，所以第一個項目是[0]，第二個是[1]
*/
let cars = new Array();
cars[0] = "Saab";
cars[1] = "Volvo";
cars[2] = "BMW";
let cars2 = ["Saab","Volvo","BMW"];
let cars3 = new Array("Saab","Volvo","BMW");
console.log(cars, cars2, cars3);  // => [ 'Saab', 'Volvo', 'BMW' ] [ 'Saab', 'Volvo', 'BMW' ] [ 'Saab', 'Volvo', 'BMW' ]
// --------------數組方法--------------
var arr1 = [1, 'hello', [11,2]];
var arr2 = new Array(4);  // 加數字的話為創建固定長度數組
var arr3 = new Array([1, 'world', true, [1,2,3]]); // 長度依元素決定
// 連接 join
console.log(arr1.join("***"));  // => 1***hello***11,2
// 拼接 concate
console.log(arr1.concat([4, 5]));  // => [1, "hello", Array(2), 4, 5]
// 轉字符串 tostring
console.log(arr1.toString());  // => 1,hello,11,2
console.log(typeof arr1.toString());  // => string
// 反轉 reverse
let arr4 = [10, 1, 5, 99, 4];
console.log(arr4.reverse()); // => [4, 99, 5, 1, 10]
// 排序 sort
console.log(arr4.sort());  // => [1, 10, 4, 5, 99]，從最高位開始排
function f(a, b) {
    if (a>b){
        return 1;  // 要正數
    }
    else if (a<b){
        return -1;  // 要負數
    }
    else {
        return 0;  // 要0
    }
}
console.log(arr4.sort(f)); // => [1, 4, 5, 10, 99]，自定義正常排序
// 刪除/新增子數組
let arr5 = [1,2,3,4,5,6,7];
arr5.splice(1,2);  // 從第1筆刪除2個值
console.log(arr5); //=> [1, 4, 5, 6, 7]
arr5.splice(1,0,99,98);  // 從第1筆刪除0個值，並加入99和98
console.log(arr5); //=> [1, 99, 98, 4, 5, 6, 7]
// 進出棧操作(先進後出)
let arr6 = [1,2,3];
arr6.push([7,8,0]);  // 做為一個元素加入
console.log(arr6);  //=> [1, 2, 3, [7,8,0]]
arr6.push('jamie',666);  // 分開加入
console.log(arr6);  //=> [1, 2, 3, [7,8,0], "jamie", 666]
console.log(arr6.pop());  //=> 666，取最後一筆
console.log(arr6.length);  //=> 5
// 進出棧操作2
let arr7 = [1,2,3];
arr7.unshift([7,8,0]);
console.log(arr7);  //=> [[7,8,0], 1, 2, 3]
arr7.unshift('jamie',666);  // 分開加入
console.log(arr7);  //=> ["jamie", 666, [7,8,0], 1, 2, 3]
console.log(arr7.shift());  //=> jamie，取第一筆
console.log(arr7.length);  //=> 5


/*
對象(Object):
    - 對象由花括號分隔
    - 循環中無法直接獲取key, val
    - 內容為鍵值對
*/
let obj1 = {
    'name': 'jamie',
    'age': 18,
    'hobby': new Array('play game', 'sleep')
};
console.log(obj1, obj1.name, obj1['name']);  // => { name: 'jamie', age: 18, hobby: [ 'play game', 'sleep' ] } jamie jamie
// 無法直接獲取key, val
for(let key in obj1){
    console.log(key, obj1[key]);
}


/*
映射(Map):
    - Object的鍵均為Strings類型，在Map裡鍵可以是任意類型
    - Object的尺寸需自行計算，但Map的尺寸可直接獲得
    - 循環中可以輕易的獲取key, val
    - 不能使用m.name, m['name']
*/
let m = new Map();
m.set('name', 'jamie');
m.set('age', 18);
m.set('hobby', new Array('play game', 'sleep'));
console.log(m, m.name, m['name']);
// => Map {
//  'name' => 'jamie',
//  'age' => 18,
//  'hobby' => [ 'play game', 'sleep' ]
// } undefined undefined
console.log(m.size);  // => 3
// 可以輕易的獲取key, val
for(let [key, val] of m){
    console.log(key, val);
}


/*
集合(Set):
    - 值不重複
*/
let mySet = new Set();
mySet.add(1);
mySet.add("some text");
mySet.add("foo");
mySet.add("foo");
console.log(mySet);
console.log(mySet.size);  // => 3


/*
Undefined 和 Null:
    - Undefined: 表示變量不含有值
    - Null: 變量通常會賦予null來當作空，而不是用Undefined
*/
let n = null;
let n2 = undefined;  // 不太好，不符合規範
let n3;  // 未賦值為Undefined
console.log(n, n2, n3);  // => null undefined undefined


/*
函數(function)
    - ...args: 其餘參數
*/
// 一般寫法
// ※ ...args: 其餘參數
function func1(name, age, ...args) {
    let obj = {
        'name': name,
        'age': age
    }
    console.log(args);  // => [ 'aa', 'bb', 3 ]

    return obj;
}
let res1 = func1('jamie', 22, 'aa', 'bb', 3);
console.log(res1);

// 表達式寫法
let square = function(num){ return num*num };
console.log(square(3));  // => 9

// 匿名函數
// (function anonymous(num){ return num*num })(<參數>)
console.log((function anonymous(num){ return num*num })(5));  // => 25


/*
類(Class):
    - extends: 繼承
*/
class Person {
    // 建構子
    constructor(name) {
        this.name = name;
    }
    // 一般類方法
    sayHi() {
        console.log('Hi', this.name);
    }
};
p = new Person('jamie');
p.sayHi();
console.log(p);  // => Person { name: 'jamie' }
console.log(p.name);  // => jamie

class Cooker extends Person{
    // 覆寫
    constructor(name, age) {
        super(name);  // 調用父類建構子
        this.age = age;
    }
    // 覆寫
    sayHi() {
        super.sayHi();  // 調用父類sayHi()方法
        console.log('Hi, too', this.name);
    }

    cook(thing) {
        console.log(this.name, 'is cooking', thing);
    }
}
c = new Cooker('jamie', 22);
c.cook('fried rice');
c.sayHi();
console.log(c);  // => Cooker { name: 'jamie', age: 22 }




