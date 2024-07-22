const conn = require("./db");


// 모든 사용자 정보 조회
const user = {
    getAll: (callback) =>{
    conn.query("SELECT * FROM user", callback);},
    // 쿼리 실행 후, callback 함수를 실행하여 sql문 결과를 불러옴


};


module.exports = user;