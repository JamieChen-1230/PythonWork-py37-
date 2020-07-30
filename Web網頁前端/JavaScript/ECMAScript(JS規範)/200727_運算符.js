// 復合運算子
/*
名稱	        簡化的運算子	意義
賦值  	    x = y	    x = y
加法賦值	    x += y	    x = x + y
減法賦值	    x -= y	    x = x - y
乘法賦值	    x *= y	    x = x * y
除法賦值	    x /= y	    x = x / y
餘數賦值	    x %= y	    x = x % y
指數賦值	    x **= y	    x = x ** y
左移賦值	    x <<= y	    x = x << y
右移賦值	    x >>= y	    x = x >> y
位元AND賦值	x &= y	    x = x & y
位元XOR賦值	x ^= y	    x = x ^ y
位元OR賦值	x |= y	    x = x | y
*/
let y = 3;  // 00011
y <<= 2;  // 01100
console.log(y);


// 比較運算子
/*
等於(==): 假如運算元等價就回傳True
不等於(!=): 假如運算元等價就回傳True
嚴格等於(===): 假如運算元具有相同型態且等價則回傳True
嚴格不等於(!==): 假如運算元具有相同型態但不等價，或是具有不同型態，回傳True
大於(>):	假如左方運算元大於右方運算元，回傳True
大於或等於(>=): 假如左方運算元大於或等於右方運算元，回傳True
小於(<): 假如左方運算元小於右方運算元，回傳True
小於或等於(<=): 假如左方運算元小於或等於右方運算元，回傳True
*/
console.log(3=='3');  // => true
console.log(3==='3');  // => false
console.log(3!='3');  // => false
console.log(3!=='3');  // => true


// 算術運算子
/*
取餘數(%): 二元運算子，回傳兩個運算元相除後的餘數
增加(++): 一元運算子，將運算元增加1
減少(--): 一元運算子，將運算元減少1
減號(-): 一元運算子，回傳運算元的負數
加號(+)： 一元運算子，嘗試將運算元轉換成數字，假如它還不是數字的話
指數運算子(**): 二元運算子
*/
// i++(++i)相當於i=i+1，i--(--i)相當於i=i-1
let i = 10;
// i++是先輸出在加(i--同理)
console.log(i++);  // => 10
i = 10;
// ++i是先輸出在加(--i同理)
console.log(++i);  // => 11

console.log(+'3');  // => 3
console.log(-'3');  // => -3


// 位元運算子
/*
位元AND:   a & b	 回傳兩個運算元對於每個bit做AND的結果。
位元OR:    a | b	 回傳兩個運算元對於每個bit做OR的結果。
位元XOR:   a ^ b	 回傳兩個運算元對於每個bit做XOR的結果。
位元NOT:   ~a	     將運算元中的每個bit反轉(1->0,0->1)。
*/
let q = 5;  // 0101
let q2 = 6  // 0110
console.log(q & q2);  // => 4，0100


// 邏輯運算子
/*
邏輯AND: 運算式1 && 運算式2
邏輯OR:  運算式1 || 運算式2
邏輯NOT: !運算式
*/
console.log('1' && true && 1);  // => 1
console.log('1' && false && 1);  // => false


// 關係運算子(in)
let list = ['x', 'y', 'z'];
console.log(0 in list);  // => true
console.log(3 in list);  // => false
console.log('x' in list);  // => false，因為比對的是下標，而不是值
let obj = {
    'a': 10,
    'b': 100,
    'c': 1000
};
console.log('a' in obj);  // => true
console.log(100 in obj);  // => false，因為比對的是key，而不是value


// 三元運算子
let age = 20;
// true為前面的值(成人)，false則反
let status = (age >= 18) ? '成人' : '小孩';
console.log(status);  // => 成人