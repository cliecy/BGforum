import React from 'react';
import type { PaginationProps } from 'antd';
import { Pagination } from 'antd';

const onChange: PaginationProps['onChange'] = (pageNumber) => {
  console.log('Page: ', pageNumber);
};

const MPagination: React.FC <{pageNum:number}> = ({pageNum}) => {

  return (  <>
    <Pagination showQuickJumper defaultCurrent={1} total={pageNum} onChange={onChange} />
  </>)

};

export default MPagination;
