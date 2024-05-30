import {Post, User,gender, userclass,} from "./typeDefinition";


export function GetPostPage():Post[]{
    var postId = 0;

    return [    {title: "BCD", content: "SSSS", date: new Date("2013/03/24"),shareid: "000",authorid:"3"}, {
        title: "EFG",
        content: "SSSS",
        date: new Date("2013/03/24"),
        shareid:"1",
        authorid:"2"
    }]
}


export function GetAllPost():Post[]{
    return [    {title: "BCD", content: "SSSS", date: new Date("2013/03/24"),shareid: "000",authorid:"3"}, {
        title: "EFG",
        content: "SSSS",
        date: new Date("2013/03/24"),
        shareid:"1",
        authorid:"3"
    }]
}

export function GetUserInfo():User{
    return {
        name:"cliecy",
        userid:"1",
        userclass:userclass.Admin,
        gender: gender.female,
        lastlogintime:new Date()
    }
}