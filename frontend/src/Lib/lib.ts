import {Post, Reply, User,gender, userclass,} from "./typeDefinition";


export function GetPostPage():Reply[]{
    var shareid = 0;

    return [ {
        date:new Date(),
        content:"ssss",
        shareid:"123",
        floor:2323,
        authorid:"sdadas"
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