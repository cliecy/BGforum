import { useParams } from "react-router";
import PostGrid from "../UI/PostGrid";

const p = [
    { title: "ABC", content: "SSSS", date: new Date("2013/03/24"), shareid: "0", authorid: "sss" },
]


const Home = () => {
    const params = useParams()
    let id: string | undefined = params.id
    if (id !== undefined) {
        return <PostGrid props={p} PageID={id}></PostGrid>
    }
    else {
        return <PostGrid props={p} PageID={"NOPARAM"}></PostGrid>
    }
}

export default Home;