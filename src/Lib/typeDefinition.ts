export interface Post{
    title: string;
    content: string;
    date: Date;
    shareid: string;
    authorid:string;
}
export interface Reply{
    date: Date;
    content: string;
    shareid: string;
    floor:number;
    authorid:string;
}
enum gender{
    male = 'male',
    female = 'female',
}

enum userclass{
    Admin = 'admin',
    Normal="Normal"
}
export interface User{
    name: string;
    userid: string;
    userclass: userclass;
    gender: gender;
    lastlogintime: Date;
}