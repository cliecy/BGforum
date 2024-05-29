import PostGrid from "../UI/PostGrid";

const p = [{title: "ABC", body: "SSSS", date: new Date("2013/03/24")},
    {title: "BCD", body: "SSSS", date: new Date("2013/03/24")}, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }, {
        title: "EFG",
        body: "SSSS",
        date: new Date("2013/03/24")
    }

]


const Home = () => {
    return <PostGrid props={p}></PostGrid>
}

export default Home;