export interface Post{
    ShareId: string;
    UserId:string;
    Content: string;
    Title: string;
    PostTime: string;
    IsLocked: boolean;
}
export interface Reply{
    date: Date;
    content: string;
    shareid: string;
    floor:number;
    authorid:string;
}
export enum gender{
    male = 'male',
    female = 'female',
}

export enum userclass{
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


export function isPost(obj: any): obj is Post {
    return (
      typeof obj.title === 'string' &&
      typeof obj.content === 'string' &&
      obj.date instanceof Date &&
      typeof obj.shareid === 'string' &&
      typeof obj.authorid === 'string'
    );
  }