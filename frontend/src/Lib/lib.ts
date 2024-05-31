import { Post, Reply, Share, User, gender, isPost, userclass, } from "./typeDefinition";
import axios from "axios";


export async function GetPostPage(shareId: string): Promise<Share> {
    let mygets: Share = {share: [], replies: []};
    try{
        await axios.get(`http://127.0.0.1:8000/shares/${shareId}`).then(function (response){
            console.log(response);
            mygets = response.data;
        }).catch(function (error) {
            console.log(error);
        });
    }
    catch{
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
    console.log(mygets);
    return mygets;
}


export async function GetAllPost(): Promise<Post[]> {
    // 发送 POST 请求
    // 为给定 ID 的 user 创建请求
    let myposts:Post[] = [];
    let myresponse;
    let data ={Title: "ABC", Content: "SSSS", PostTime:"2013-03-24 13:30:20", UserId: 2 ,IsLocked:false}
    try{
        await axios.post("http://127.0.0.1:8000/shares",data).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        });
    }catch{
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
    try{
        await axios.get('http://127.0.0.1:8000/shares').then(function (response) {
            console.log(response);
            myresponse = response
            myposts = myresponse.data;
        }).catch(function (error) {
            console.log(error);
        });
    }
    catch{
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
    console.log(myposts)
    return myposts
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