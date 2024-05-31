import React from 'react';
import type { PaginationProps } from 'antd';
import { Pagination } from 'antd';

const onChange: PaginationProps['onChange'] = (pageNumber) => {
  console.log('Page: ', pageNumber);
};

const MPagination: React.FC = () => (
  <>
    <Pagination showQuickJumper defaultCurrent={1} total={500} onChange={onChange} />
  </>
);

export default MPagination;
