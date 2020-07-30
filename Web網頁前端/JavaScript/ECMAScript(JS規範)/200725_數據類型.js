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


/*
對象(Object):
    - 對象由花括號分隔
    - 內容為鍵值對
    - 循環中無法直接獲取key, val
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
*/
// 一般寫法
function func1(name, age) {
    let obj = {
        'name': name,
        'age': age
    }

    return obj;
}
let res1 = func1('jamie', 22);
console.log(res1);

// 當作表達式
let square = function(num){ return num*num };
console.log(square(3));


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
console.log(p.name);  // => jamies

class Cooker extends Person{
    // 覆寫
    constructor(name, age) {
        super(name);  // 調用父類建構子
        this.age = age;
    }
    // 覆寫
    sayHi() {
        super.sayHi();
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




