import React from "react";
import { Button, Flex, Form, Input, Select } from "antd";
import storageUtils from "../Lib/storageUtils";
import { GetUserIdByUserName, MakePost, MakeReply } from "../Lib/lib";
import { formatDatefordate } from "../Lib/lib";
export type PostFieldType = {
  content: string;
};

const mp = async (values: PostFieldType) => {
  let now = new Date()
  let userid:number;
  if(storageUtils.getUser()){
    userid = await GetUserIdByUserName(storageUtils.getUserName())
    const shareid = localStorage.getItem("currentShareid")
    if(shareid){
      await MakeReply(
        {UserId:userid,Content:values.content,PostTime:formatDatefordate(now),ShareId:parseInt(shareid,10)}
      )
    }
    else{
      console.log("not current shareid ,can't make reply")
    }
      ;
  }
  else{
    console.log("LOGIN STATE ERROR")
    window.location.reload()
  }
};
interface MakeReplyProps{
  shareid:number;
}

const MakeReplyComponent :React.FC<MakeReplyProps>=({shareid}) => {
  const [form] = Form.useForm();
  if (storageUtils.getUser() == false) return <></>;
  return (
    <>
      <Form
        form={form}
        style={{ paddingBlock: 32 }}
        labelCol={{ span: 6 }}
        wrapperCol={{ span: 14 }}
        onFinish={mp}
      >

        <Form.Item<PostFieldType>
          name="content"
          label="content"
          rules={[{ required: true }]}
        >
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

export default MakeReplyComponent;
