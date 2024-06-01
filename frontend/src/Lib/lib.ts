import { Post, Reply, Share, User, gender, isPost, userclass, } from "./typeDefinition";
import axios from "axios";
import { FieldType } from "../Pages/Login";
import storageUtils from "./storageUtils";
import { RegisterFieldType } from "../Pages/Register";


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

export function formatDate(time: string | number) {
    if (time === null) {
      return ''
    } else {
      const date = new Date(time)
      const y = date.getFullYear()
      let m: string | number = date.getMonth() + 1
      m = m < 10 ? `0${String(m)}` : m
      let d: string | number = date.getDate()
      d = d < 10 ? `0${String(d)}` : d
      let h: string | number = date.getHours()
      h = h < 10 ? `0${String(h)}` : h
      let minute: string | number = date.getMinutes()
      minute = minute < 10 ? `0${String(minute)}` : minute
      let second: string | number = date.getSeconds()
      second = second < 10 ? `0${String(second)}` : second
      return `${String(y)}-${String(m)}-${String(d)}   ${String(h)}:${String(
        minute
      )}:${String(second)}`
    }
  }

  function formatDatefordate(date: Date): string {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');

    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}



export async function RegisterFunc(values:RegisterFieldType):Promise<void>{
    let myresponse: LoginStatus = { status: "", message: "" };
    const now = new Date();
    try {
        await axios.post('http://127.0.0.1:8000/users', { UserName: values.userName,motto:"LEO is really excellent",LastLogintime:formatDatefordate(now)
        ,gender:"Male", password: values.password,numofShares:0}).then(function (response) {
            console.log(response);
            myresponse = response.data
        }).catch(function (error) {
            console.log(error);
        });
        if (myresponse.status === "Success") {
            console.log("Register and Login SUCCESS")
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
    // window.location.reload()
}

