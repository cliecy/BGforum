import { Col, Row } from 'antd';
import {Post} from "../Lib/typeDefinition";





const PostGrid: React.FC<{ props: Post[] }> = ({ props    }) => (
    <>
        {props.map((post, index) => (
            <Row key={index}>
                <Col span={24}>
                    <h1>{post.title}</h1>
                    <p>{post.date.toDateString()}</p>
                </Col>
            </Row>
        ))}
    </>

    );


export default PostGrid;