
import {useParams} from "react-router";
import {Col, Row} from "antd";
import {NavLink} from "react-router-dom";
import {GetPostPage} from "../Lib/lib";

const PostPage=() => {
    const params = useParams();
    let id =params.id
    let props = GetPostPage()
    return <div>
        {props.map((reply, index) => (
            <Row key={index}>
                <Col span={24}>
                    <p>{reply.content}</p>
                    <p>{reply.authorid}</p>
                </Col>
            </Row>
        ))}
    </div>
}


export default PostPage;