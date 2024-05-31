import { Post, Reply, User, gender, userclass, } from "./typeDefinition";
import axios from "axios";


  
  

export function GetPostPage(): Reply[] {
    var shareid = 0;

    return [{
        date: new Date(),
        content: "ssss",
        shareid: "123",
        floor: 2323,
        authorid: "sdadas"
    }]
}


export function GetAllPost(): Post[] {
    // 发送 POST 请求
// 为给定 ID 的 user 创建请求
axios.get('/api/shares').then(function (response) {
    console.log(response);
  }).catch(function (error) {
    console.log(error);
  });
  
  

    return [{ title: "BCD", content: "SSSS", date: new Date("2013/03/24"), shareid: "000", authorid: "3" }, {
        title: "EFG",
        content: "SSSS",
        date: new Date("2013/03/24"),
        shareid: "1",
        authorid: "3"
    }]
}

export function GetUserInfo(): User {
    return {
        name: "cliecy",
        userid: "1",
        userclass: userclass.Admin,
        gender: gender.female,
        lastlogintime: new Date()
    }
}