/*
ES6之後，較推薦使用let和const
var: 不推薦使用，因為有可能造成區域變數覆蓋全域變數的情況發生
const: 一般使用在識別值(identifier)或常數，不能被重新定義
    - const在宣告變數時就會進行初始化，無法等到之後再賦予值，因此必定要在一開始就給予值作宣告，否則將會報錯
let: 一般使用在變數(variable)，可以被重新指定值
    - 在同一個block中，不可重複使用let宣告同一個變量
*/

const PI = 3.14;
// PI = 3.15;  // => 報錯


let l = 1;
function change_l_with_let(){
    let l = 2;  // 若有用let宣告，則會將l當作區域變數。
    console.log('in change_l_with_let:', l);
};
function change_l_not_let(){
    l = 3;  // 抓到的是全域的l
    function inner(){
        // 若未使用let宣告，則會使用外層之變數，並且會跟改值。(有點類似於python中的global關鍵字)
        l = 40;  // 抓到的是change_l_not_let的l，也相當於全域的l
        console.log('in change_l_not_let_inner:', l);
    };
    inner();
    console.log('in change_l_not_let:', l);
};
console.log('out function_1:', l);
change_l_with_let();
change_l_not_let();
console.log('out function_2:', l);


