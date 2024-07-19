// 초기 설정(1)
const express = require("express");         //익스프레스 사용할거야!
const app = express();                      // app이라는 이름에 express 담아서 사용할거야!
const nunjuck = require("nunjucks");        // nunjucks도 사용할거야!
const mainRouter = require("./routes/mainRouter") //라우터 기능을 가져올거야!
const sessionRouter = require("./routes/session") // session라우터 기능을 가져올거야!

//세션 세팅
const session = require("express-session");
const fileStore =require("session-file-store")(session);
app.use(session({
    httpOnly : true, // http로 들어온 요청만 처리하겠다.
    resave : false, // 세션을 항상 재 저장하겠다.
    secret : "secret", // 암호화할때 사용하는 키값
    store : new fileStore(), //세션을 저장하기 위한 저장소 셋팅
    saveUninitialized : false //세션에 저장할 내용이 없더라도 저장 여부!
    
}))

// 라우터 설정
app.use("/",mainRouter);
app.use("/session", sessionRouter); // sessionRouter도 추가



// 넌적스 설정(2) -> 나 화면 여기서 보여질거야!
app.set("view engine","html");
nunjuck.configure("views",{
    express : app,
    watch :true
});

// 서버 시작(1)
app.listen(3000)// 나는 서버를 3000포트에서 사용할거야! 


