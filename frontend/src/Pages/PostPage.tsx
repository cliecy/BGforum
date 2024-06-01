import {useParams} from "react-router";
import {GetPostPage} from "../Lib/lib";
import React, { useEffect, useState } from 'react';
import { ShareAndReplies } from "../Lib/typeDefinition";
import MakePostComponent from '../UI/MakePostComponent';
import InnerPostGrid from "../UI/InnerPostGrid";

const PostPage: React.FC=() => {
    const [posts, setReplies] = useState<ShareAndReplies>({share:[], replies:[]});
    const [currentPage, setCurrentPage] = useState<number>(1);
    const [pageSize,setpageSize] = useState<number>(20); // 每页显示的帖子数量

    const params = useParams();
    let id: number
    if (params.id != undefined){
        id=parseInt(params.id,10)
    }else{
        id=-1
    }

    useEffect(() => {
        const fetchPosts = async () => {
          const post: ShareAndReplies = await GetPostPage(id);
          setReplies(post);
        };
        fetchPosts();
      }, []);
    
    const handlePageChange = (page: number) => {
        setCurrentPage(page);
    };

    const handleShowSizeChange = (current:number,pageSize:number) =>{
        setpageSize(pageSize);
    }

    return (
        <>
            <InnerPostGrid 
                post={posts}
                currentPage={currentPage}
                pageSize={pageSize}
                onPageChange={handlePageChange}
                onShowSizeChange={handleShowSizeChange}
        />
        <MakePostComponent></MakePostComponent>
        </>
    );
};


export default PostPage;