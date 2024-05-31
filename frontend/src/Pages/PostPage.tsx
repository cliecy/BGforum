import React, { useEffect, useState } from 'react';
import { Post } from '../Lib/typeDefinition';
import {useParams} from "react-router";
import {Col, Row} from "antd";
import {NavLink} from "react-router-dom";
import {GetPostPage} from "../Lib/lib";

const PostPage: React.FC = () => {
    const [posts, setPosts] = useState<Post[]>([]);
    const [currentPage, setCurrentPage] = useState<number>(1);
    const [pageSize] = useState<number>(20); // 每页显示的帖子数量
    const params = useParams<{ id: string }>();
    let id = params.id
    
    useEffect(() => {
        const fetchPosts = async () => {
            const myALLPOSTS = await GetPostPage(id);
            setPosts(myALLPOSTS);
        }
    }, [])

    let replies = props.replies
    return <div>
        {props.map((userId, ) => (
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