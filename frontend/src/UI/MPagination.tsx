// import React from 'react';
// import type { PaginationProps } from 'antd';
// import { Pagination } from 'antd';

// const onChange: PaginationProps['onChange'] = (pageNumber) => {
//   console.log('Page: ', pageNumber);
// };

// const MPagination: React.FC <{pageNum:number}> = ({pageNum}) => {

//   return (  <>
//     <Pagination showQuickJumper defaultCurrent={1} total={pageNum} onChange={onChange} />
//   </>)

// };

// export default MPagination;
import React from 'react';
import type { PaginationProps } from 'antd';
import { Pagination } from 'antd';

interface MPaginationProps {
  total: number;
  pageSize: number;
  onPageChange: (page: number) => void;
  onShowSizeChange: (current:number,pageSize:number) => void;
}

const MPagination: React.FC<MPaginationProps> = ({ total, pageSize, onPageChange,onShowSizeChange }) => {
  const handleChange: PaginationProps['onChange'] = (pageNumber) => {
    onPageChange(pageNumber);
  };

  return (
    <Pagination
      showQuickJumper
      defaultCurrent={1}
      total={total}
      pageSize={pageSize}
      onChange={handleChange}
      onShowSizeChange={onShowSizeChange}
    />
  );
};

export default MPagination;