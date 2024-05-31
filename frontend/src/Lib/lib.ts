import { Post, Reply, User, gender, isPost, userclass, } from "./typeDefinition";
import axios from "axios";
import { FieldType } from "../Pages/Login";
import storageUtils from "./storageUtils";

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


export async function GetAllPost(): Promise<Post[]> {
    // 发送 POST 请求
    // 为给定 ID 的 user 创建请求
    let myposts:Post[] = [];
    let myresponse;

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

export async function MakePost(post:Post):Promise<void>{
    try{
        await axios.post("http://127.0.0.1:8000/shares",post).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        });
    }catch{
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
}
// export function 


interface LoginStatus{
    status:string;
    message:string
}

export async function LoginFunc(values:FieldType): Promise<void>{
    let myresponse:LoginStatus = {status:"",message:""};
    try{
        await axios.post('http://127.0.0.1:8000/users/login',{userName:values.userName,password:values.password}).then(function (response) {
            console.log(response);
            myresponse = response.data
        }).catch(function (error) {
            console.log(error);
        });
        if(myresponse.status==="success"){
            console.log("LOGIN SUCCESS")
            if(values.userName != undefined && values.password!= undefined)
                if(values.remember==true)
                    storageUtils.saveUser({username:values.userName,password:values.password})
        }
    }
    catch{
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }

}

// export async function RegisterFunc(values:)

export function Logout():void{
    if(storageUtils.getUser())
        storageUtils.removeUser()
    else{
        console.log("already log out")
    }
}