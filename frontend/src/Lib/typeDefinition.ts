export interface Post {
    ShareId: number | undefined;
    UserId: number;
    Content: string;
    Title: string;
    PostTime: string;
    IsLocked: boolean;
    UserData:GetUserType |undefined;
}

export interface MakePostType{
    UserId: number;
    Content: string;
    Title: string;
    PostTime: string;
    // IsLocked: boolean;
}
export interface Reply{
    Content: string;
    Floor:number;
    PostTime:string;
    ReplyId:number;
    ReplyTo:number;
    ShareId:number;
    UserId:number;
    UserData:GetUserType | undefined;
}

export interface MakeReplyType{
    Content: string;
    PostTime:string;
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

export interface GetUserType{
    UserId:number,
    LastLogintime:string;
    UserName:string;
    gender: string;
    motto: string;
    numofShares:number;
}
export interface ShareAndReplies{
    share: Post[];
    replies: Reply[];
}

export interface HTTPStatus{
    status:number;
}