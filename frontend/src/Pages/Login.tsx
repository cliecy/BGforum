import type { FormProps } from 'antd';
import { Button, Checkbox, Form, Input } from 'antd';
import { LoginFunc } from '../Lib/lib';
import { useNavigate } from "react-router";
import { useEffect } from "react";
import storageUtils from '../Lib/storageUtils';

const Redirect = ()=>{
    const Navigate = useNavigate()
    useEffect(()=>{Navigate("/")})
    return <></>
}
export type FieldType = {
    userName?: string;
    password?: string;
    remember?: boolean;
};

const onFinish: FormProps<FieldType>['onFinish'] = async (values) => {
    await LoginFunc(values)
};

const onFinishFailed: FormProps<FieldType>['onFinishFailed'] = async (errorInfo) => {
    console.log('Failed:', errorInfo);
};

const Login: React.FC = () => (
    
    <Form
        name="basic"
        labelCol={{ span: 8 }}
        wrapperCol={{ span: 16 }}
        style={{ maxWidth: 600 }}
        initialValues={{ remember: true }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
    >
        {storageUtils.getUser() && <Redirect/>}
        <Form.Item<FieldType>
            label="Username"
            name="userName"
            rules={[{ required: true, message: 'Please input your username!' }]}
        >
            <Input />
        </Form.Item>

        <Form.Item<FieldType>
            label="Password"
            name="password"
            rules={[{ required: true, message: 'Please input your password!' }]}
        >
            <Input.Password />
        </Form.Item>

        <Form.Item<FieldType>
            name="remember"
            valuePropName="checked"
            wrapperCol={{ offset: 8, span: 16 }}
        >
            <Checkbox>Remember me</Checkbox>
        </Form.Item>

        <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Button type="primary" htmlType="submit">
                Submit
            </Button>
        </Form.Item>
    </Form>
);

export default Login;