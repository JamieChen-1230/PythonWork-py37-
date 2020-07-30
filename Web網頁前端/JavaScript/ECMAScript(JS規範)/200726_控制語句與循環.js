// if語句
/*
let name='jamie';
if (name=='666'){
    console.log('666');
}
else if (name=='sb'){
    console.log('sb');
}
else {
    console.log(name);
}
*/


// switch語句
/*
let day=6;
switch (day) {
    case "m": console.log('星期一'); break;
    case 'r': console.log('星期二'); break;
    case "w": console.log('星期三'); break;
    case "r": console.log('星期四'); break;
    case "f": console.log('星期五'); break;
    case 6: console.log('星期六'); break;
    case 7: console.log('星期日'); break;
    default: console.log('nothing');  // 無匹配走default
}
*/


// for循環
/*
let attr = ['aa', 'bb', 'cc']
// 方法一(推薦)
for (let i=0; i<attr.length; i++){
    console.log(i, attr[i]);
}
// 方法二
for (let i in attr){
    console.log(i, attr[i]);
}
// 方式三(推薦)
// 只可用於可迭代物件(Array、Map、Set、String、TypedArray、arguments等)
for (let i of attr){
    console.log(i);
}
*/


// while循環
/*
let i = 1, sum = 0;
while (i <= 100){
    sum += i;
    i++;
}
console.log(sum);
*/


// do while循環
/*
let i = 1, sum = 0;
do {
  sum += i;
  i++;
}while(i <= 100);
console.log(sum);
*/


// 異常
/*
try{
    // 正常程序
    console.log(123);
    throw Error('define error');  // 拋出異常
}
catch (e) {
    // 發生異常執行的代碼
    console.log(e);
}
finally {
    // 不管有沒有發生異常最後都會執行
    console.log('finally');
}
*/