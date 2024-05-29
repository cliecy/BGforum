import PostGrid from "../UI/PostGrid";

const p = [{title: "ABC", body: "SSSS", date: new Date("2013/03/24"),uniqueid: "0"},
    {title: "BCD", body: "SSSS", date: new Date("2013/03/24"),uniqueid: "000"}, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"1"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"2"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"3"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid: "11"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"4"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"5"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"6"
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24"),
        uniqueid:"7"
    }
]


const Home = () => {
    return <PostGrid props={p}></PostGrid>
}

export default Home;