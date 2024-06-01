import {Post, Reply, ShareAndReplies, User, gender, userclass} from "./typeDefinition";
import axios from "axios";
import { FieldType } from "../Pages/Login";
import storageUtils from "./storageUtils";


export async function GetPostPage(shareId: number): Promise<ShareAndReplies> {
    // 发送 GET 请求特定 ID 的帖子
    let share: ShareAndReplies = {share:[], replies:[]};
    const myaxios = axios.create()
    myaxios.defaults.timeout = 10000
    try {
        await myaxios.get(`http://127.0.0.1:8000/shares/${shareId}`).then(function (response) {
            console.log(response);
            share = response.data;
        }).catch(function (error) {
            console.log(error);
        });
    }
    catch {
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
    console.log(share)
    return share
}


export async function GetAllPost(): Promise<Post[]> {
    // 发送 POST 请求
    // 为给定 ID 的 user 创建请求
    let myposts: Post[] = [];
    let myresponse;

    try {
        await axios.get('http://127.0.0.1:8000/shares').then(function (response) {
            console.log(response);
            myresponse = response
            myposts = myresponse.data;
        }).catch(function (error) {
            console.log(error);
        });
    }
    catch {
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
    console.log(myposts)
    return myposts
}

export async function MakePost(post: Post): Promise<void> {
    try {
        await axios.post("http://127.0.0.1:8000/shares", post).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        });
    } catch {
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
}
// export function


interface LoginStatus {
    status: string;
    message: string
}

export async function LoginFunc(values: FieldType): Promise<void> {
    let myresponse: LoginStatus = { status: "", message: "" };
    try {
        await axios.post('http://127.0.0.1:8000/users/login', { UserName: values.userName, password: values.password }).then(function (response) {
            console.log(response);
            myresponse = response.data
        }).catch(function (error) {
            console.log(error);
        });
        if (myresponse.status === "Success") {
            console.log("LOGIN SUCCESS")
            if (values.userName != undefined && values.password != undefined)
                if (values.remember == true) {
                    console.log(values)
                    storageUtils.saveUser({ username: values.userName, password: values.password })
                }
        }
    }
    catch {
        console.log("ERRORS BUT NOT AXIOS ERROR")
    }
    window.location.reload()
}

// export async function RegisterFunc(values:)

export function Logout(): void {
    if (storageUtils.getUser())
        storageUtils.removeUser()
    else {
        console.log("already log out")
    }
    window.location.reload()
}