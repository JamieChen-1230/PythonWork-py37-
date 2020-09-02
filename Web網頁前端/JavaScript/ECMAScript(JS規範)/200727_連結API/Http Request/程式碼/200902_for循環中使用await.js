let axios = require('axios');



async function sleep(ms = 0) {
    return new Promise(r => setTimeout(r, ms));
};


async function hello(time){
    await sleep(time);
    return "hello" + time;
};

async function run(){
    let time_array = [2000, 4000, 3000];
    // 串行
    for(let t of time_array){
        let res = await hello(t);
        console.log(res);
    }; 

    // 並行
    // axios.all(time_array.map(async (x) => {
    //     return await hello(x) + "XXD";
    // }))
    // .then(axios.spread((...res) => {
    //     console.log(res);
    // }))
};

run()