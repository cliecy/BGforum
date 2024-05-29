export interface Post{
    title: string;
    body: string;
    date: Date;
    uniqueid: string;
}
export interface Reply{

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