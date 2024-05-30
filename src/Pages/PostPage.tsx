
import {useParams} from "react-router";
import {Col, Row} from "antd";
import {NavLink} from "react-router-dom";
import {GetPostPage} from "../Lib/lib";

const PostPage=() => {
    const params = useParams();
    let id =params.id
    let props = GetPostPage()
    return <div>
        {props.map((post, index) => (
            <Row key={index}>
                <Col span={24}>
                    <NavLink to={`/PostPage/${post.shareid}`}>{post.title}</NavLink>
                    <p>{post.date.toDateString()}</p>
                </Col>
            </Row>
        ))}
    </div>
}


export default PostPage;