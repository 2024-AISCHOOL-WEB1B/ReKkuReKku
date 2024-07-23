const express = require("express");
const routes = express.Router();

routes.get("/",(req,res)=>{
    res.render("main")
})

// 사용자가 회원가입 요청할 때 ->> view에 있는 join페이지로 이동
Router.get("/join",(req,res)=>{
    res.render("join")
})

// 사용자가 로그인 요청할 때
router.get("/login",(req,res)=>{
    res.render("login")
})

module.exports = routes;