export interface Post {
    ShareId: number | undefined;
    UserId: number;
    Content: string;
    Title: string;
    PostTime: string;
    IsLocked: boolean;
}
export interface Reply{
    Content: string;
    Floor:number;
    PostTime:Date;
    ReplyId:number;
    ReplyTo:number;
    ShareId:number;
    UserId:number;
}

export enum gender{
    male = 'male',
    female = 'female',
}

export enum userclass {
    Admin = 'admin',
    Normal = "Normal"
}
export interface User {
    name: string;
    userid: string;
    userclass: userclass;
    gender: gender;
    lastlogintime: Date;
}

export interface ShareAndReplies{
    share: Post[];
    replies: Reply[];
}