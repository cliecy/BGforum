import { useState, useEffect } from "react";
import { HomeOutlined, LinkOutlined,LoginOutlined } from "@ant-design/icons";
import { Breadcrumb, Layout, Menu, theme, Image, Row, Col } from "antd";
import { NavLink, Outlet, useLocation } from "react-router-dom";
import React from "react";

const { Header, Content,Footer} = Layout;

const menuItems = [
  {
    label: "Home",
    key: "/Home",
    icon: <HomeOutlined />,
  },
  {
    label: "Register",
    key: "/Register",
    icon: <LinkOutlined />,
  },
  {
    label:"Login",
    key:"/Login",
    icon: <LoginOutlined/>
  }
];

const App = () => {
  const {
    token: { colorBgContainer,borderRadiusLG },
  } = theme.useToken();
  const [currentMenu, setCurrentMenu] = useState({});
  // 定义selectedKeys，来控制菜单选中状态和切换页面
  const [selectedKeys, setSelectedKeys] = useState([]);
  // useLocation react-router自带hook，能获取到当前路由信息
  const location = useLocation();
  // 每次切换路由，获取当前最新的pathname,并赋给menu组件
  useEffect(() => {
    // location.pathname对应路由数据中的path属性
    setSelectedKeys([location.pathname]);
    // store current menu
    setCurrentMenu(menuItems.find((item) => item.key === location.pathname));
  }, [location]);

  return (
      <Layout style={{
        justifyContent: "center",
        width: "100%",
        height: "100%",
        display: "flex"
      }
      }>
        <Header style={{alignItems: "center"}}>
          <Row>
            <Col flex="130px">
              <NavLink to="/">
                <Image
                    src="favicon.ico"
                    preview={false}
                    style={{marginLeft: 0, marginRight: 10, width: "70%"}}
                />

              </NavLink>
            </Col>
            <Col flex="auto">
              <Menu
                  theme="dark"
                  mode="horizontal"
                  selectedKeys={selectedKeys}
                  items={menuItems.map((item) => {
                    return {
                      key: item.key,
                      label: <NavLink to={item.key}>{item.label}</NavLink>,
                      disabled: item.disabled,
                      icon: item.icon,
                    };
                  })}
              />
            </Col>
          </Row>
        </Header>



        <Content style={{padding: "30px", background: colorBgContainer}}>
          {location.pathname !== "/" && location.pathname !== "/Home" && (
              <Breadcrumb
                  items={[
                    {
                      href: "/",
                      title: <HomeOutlined/>,
                    },
                    {
                      title: currentMenu?.label,
                    },
                  ]}
              />
          )}
          <Outlet/>
        </Content>
        {/*<Footer>created by cliecy</Footer>*/}
      </Layout>
  );
};

export default App;