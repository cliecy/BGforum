import { Col, Row } from 'antd';
import {Post} from "../Lib/typeDefinition";
import { NavLink } from 'react-router-dom';





const PostGrid: React.FC<{ props: Post[] }> = ({ props    }) => (
    <>
        {props.map((post, index) => (
            <Row key={index}>
                <Col span={24}>
                    <NavLink to={}>{post.title}</NavLink>
                    <p>{post.date.toDateString()}</p>
                </Col>
            </Row>
        ))}
    </>

    );


export default PostGrid;