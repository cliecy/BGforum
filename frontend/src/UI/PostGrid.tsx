// import {Col, Row} from 'antd';
// import {Post} from "../Lib/typeDefinition";
// import {NavLink} from 'react-router-dom';
// import MPagination from './MPagination';



// const PostGrid: React.FC<{ props: Post[],PageID:string }> = ({props,PageID}) => {

//     if(PageID==="NOPARAM")
//         PageID = "1"
//     return (
//         <>
//             {props.map((post, index) => (
//                 <Row key={index}>
//                     <Col span={24}>
//                         <NavLink to={`/PostPage/${post.ShareId}`}>{post.Title}</NavLink>
//                         <p>{post.PostTime}</p>
//                     </Col>
//                 </Row>
//             ))}
//             <MPagination pageNum={props.length}/>
//         </>
//     )


// }


// export default PostGrid;

import React from 'react';
import { Col, Row } from 'antd';
import { Post } from "../Lib/typeDefinition";
import { NavLink } from 'react-router-dom';
import MPagination from './MPagination';
import { useEffect } from 'react';
import { GetUserDataById } from '../Lib/lib';
import { useState } from 'react';
interface PostGridProps {
  posts: Post[];
  currentPage: number;
  pageSize: number;
  onPageChange: (page: number) => void;
  onShowSizeChange: (current:number,pageSize:number) =>void;
}

const PostGrid: React.FC<PostGridProps> = ({ posts, currentPage, pageSize, onPageChange,onShowSizeChange }) => {
  const startIndex = (currentPage - 1) * pageSize;
  const currentPosts = posts.slice(startIndex, startIndex + pageSize);
  const [postsWithUserData, setPostsWithUserData] = useState<Post[]>([]);

  useEffect(() => {
    const fetchUserData = async () => {
      const test = currentPosts
        const updatedPosts = await Promise.all(test.map(async (post) => {
            post.UserData = await GetUserDataById(post.UserId);
            return post;
        }));

        setPostsWithUserData(updatedPosts);
    };

    fetchUserData();
}, [posts,currentPage,pageSize]);
  return (
    <>
      {postsWithUserData.map((post, index) => (
        <Row key={index}>
          <Col span={24}>
            <NavLink to={`/PostPage/${post.ShareId}`}>{post.Title}</NavLink>
            <p>{post.PostTime}</p>
            <p>{post.UserId}</p>
            <p style={{ fontWeight: 'bold', color: 'red', border: '1px solid black' }}>{post.UserData?.UserName}</p>
          </Col>
        </Row>
      ))}
      <MPagination total={posts.length} pageSize={pageSize} onPageChange={onPageChange} onShowSizeChange={onShowSizeChange} />
    </>
  );
};

export default PostGrid;