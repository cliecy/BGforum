import {Col, Row} from 'antd';
import {Post} from "../Lib/typeDefinition";
import {NavLink} from 'react-router-dom';
import MPagination from './MPagination';



const PostGrid: React.FC<{ props: Post[],PageID:string }> = ({props,PageID}) => {

    if(PageID==="NOPARAM")
        PageID = "1"
    return (
        <>
            {props.map((post, index) => (
                <Row key={index}>
                    <Col span={24}>
                        <NavLink to={`/PostPage/${post.ShareId}`}>{post.Title}</NavLink>
                        <p>{post.PostTime}</p>
                    </Col>
                </Row>
            ))}
            <MPagination pageNum={props.length}/>
        </>
    )


}


export default PostGrid;