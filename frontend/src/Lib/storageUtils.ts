// ! 本模块主要是进行local数据存储

export interface LoginUser{
    username:string;
    password:string;
}


export default {
    // 保存用户
    saveUser(user:LoginUser) {
        localStorage.setItem("username",user.username);
        localStorage.setItem("password",user.password)
    },

    // 读取用户
    getUser():boolean {
        const result = localStorage.getItem("username")
        if(result!=null){
            return true
        }else{
            return false
        }
    },

    // 删除用户
    removeUser():void {
        localStorage.setItem("username","")
        localStorage.setItem("password","")
    }
}
