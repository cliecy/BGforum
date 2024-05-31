import React from 'react';
import { Button, Flex, Form, Input, Select } from 'antd';

const MakePostComponent = () => {
  const [form] = Form.useForm();
  return (
    <>
        <Form
      form={form}
      style={{ paddingBlock: 32 }}
      labelCol={{ span: 6 }}
      wrapperCol={{ span: 14 }}
    >

      <Form.Item name="Content" label="Content" rules={[{ required: true }]}>
        <Input.TextArea rows={6} />
      </Form.Item>

      <Form.Item wrapperCol={{ offset: 6 }}>
        <Flex gap="small">
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
          <Button danger onClick={() => form.resetFields()}>
            Reset
          </Button>
        </Flex>
      </Form.Item>
    </Form>
    </>

  );

};

export default MakePostComponent;