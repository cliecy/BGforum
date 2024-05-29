import {Post} from "./typeDefinition";


export function GetPostPage():Post[]{
    var postId = 0;

    return [    {title: "BCD", body: "SSSS", date: new Date("2013/03/24"),uniqueid: "000"}, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"1"
    }]
}