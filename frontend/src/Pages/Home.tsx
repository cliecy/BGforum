// import React, { useEffect, useState } from "react";
// import { useParams } from "react-router";
// import PostGrid from "../UI/PostGrid";
// import { GetAllPost } from "../Lib/lib";
// import { Post } from "../Lib/typeDefinition";

// const placeholderPosts: Post[] = [
//   { Title: "ABC", Content: "SSSS", PostTime:"2013/03/24", ShareId: "0", UserId: "sss" ,IsLocked:false},
// ];

// const Home: React.FC = () => {
//   const [posts, setPosts] = useState<Post[]>([]);
//   const params = useParams<{ id: string }>();

//   useEffect(() => {
//     const fetchPosts = async () => {
//       const myALLPOSTS = await GetAllPost();
//       setPosts(myALLPOSTS);
//     };

//     fetchPosts();
//   }, []);

//   const id = params.id;

//   if (id !== undefined) {
//     return <PostGrid props={posts} PageID={id} />;
//   } else {
//     return <PostGrid props={placeholderPosts} PageID={"NOPARAM"} />;
//   }
// };

// export default Home;

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router';
import PostGrid from '../UI/PostGrid';
import { GetAllPost } from '../Lib/lib';
import { Post } from '../Lib/typeDefinition';

const placeholderPosts: Post[] = [
    {ShareId:undefined,Title: "ABC", Content: "SSSS", PostTime:"2013-03-24 13:30:20", UserId: 2 ,IsLocked:false}];

const Home: React.FC = () => {
  const [posts, setPosts] = useState<Post[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [pageSize] = useState<number>(20); // 每页显示的帖子数量
  const params = useParams<{ id: string }>();

  useEffect(() => {
    const fetchPosts = async () => {
      const myALLPOSTS = await GetAllPost();
      setPosts(myALLPOSTS);
    };

    fetchPosts();
  }, []);

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
  };

  const id = params.id || 'NOPARAM';

  return (
    <PostGrid
      posts={id === 'NOPARAM' ? placeholderPosts : posts}
      currentPage={currentPage}
      pageSize={pageSize}
      onPageChange={handlePageChange}
    />
  );
};

export default Home;