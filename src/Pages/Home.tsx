import PostGrid from "../UI/PostGrid";

const p = [
    {title: "ABC", content: "SSSS", date: new Date("2013/03/24"),shareid: "0",authorid:"sss"},
]


const Home = () => {
    return <PostGrid props={p}></PostGrid>
}

export default Home;