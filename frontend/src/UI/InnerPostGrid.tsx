import React, { useEffect } from 'react';
import { Col, Row } from 'antd';
import { ShareAndReplies, Reply } from "../Lib/typeDefinition";
import MPagination from './MPagination';

interface InnerPostGridProps {
    post: ShareAndReplies;
    currentPage: number;
    pageSize: number;
    onPageChange: (page: number) => void;
    onShowSizeChange: (current: number, pageSize: number) => void;
}

const InnerPostGrid: React.FC<InnerPostGridProps> = ({ post, currentPage, pageSize, onPageChange, onShowSizeChange }) => {
    const startIndex = (currentPage - 1) * pageSize;
    const mainPost = post.share[0]
    const repliesInCurrentPage: Reply[] = post.replies.slice(startIndex, startIndex + pageSize)
    console.log(post)
    if(!mainPost)
        return <div>loading</div>
    else{
        const a = (c:number)=>{
            if (c===1){
                return(<Row key={-1}><Col span={24}>{mainPost.Content}</Col></Row>)
            }
        }
    
        return (
            <>
                {a(currentPage)}
                {repliesInCurrentPage.map((reply, index) => (
                        <Row key={index}>
                            <Col span={24}>
                                <p>{reply.Content}</p>
                            </Col>
                        </Row>
                ))}
                <MPagination total={post.replies.length} pageSize={pageSize} onPageChange={onPageChange} onShowSizeChange={onShowSizeChange} />
            </>
        );
    }


};

export default InnerPostGrid;


