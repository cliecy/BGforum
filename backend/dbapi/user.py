from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from ..dbapi.models import User
from fastapi import HTTPException
from datetime import datetime
import json
from ..dbapi.database import getdb
from ..networkapi import schemas


class UserCURD:
    @classmethod
    def createUserbyJson(cls, receivedJson: str):
        s = getdb()
        jsondict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        user = User(
            UserId=jsondict["UserId"],
            UserClass=jsondict["UserClass"],
            UserName=jsondict["UserName"],
            motto=jsondict["motto"],
            LastLogintime=datetime.strptime(jsondict["LastLogintime"], date_format),
            gender=jsondict["gender"],
            password=jsondict["password"],
            numofShares=jsondict["numofShares"],
        )
        s.add(user)
        s.commit()
    @classmethod
    def createUserbyObject(cls, user: schemas.UserCreate):
        s = getdb()
        dbuser = User(
            UserId=user.UserId,
            UserClass=user.UserClass,
            UserName=user.UserName,
            motto=user.motto,
            LastLogintime=user.LastLogintime,
            gender=user.gender,
            password=user.password,
            numofShares=user.numofShares,
        )
        s.add(dbuser)
        s.commit()
        
    @classmethod
    def getUserByUserId(cls, userId):
        s = getdb()
        stmt = select(User).where(User.UserId == userId)
        result = s.scalars(stmt).first()
        return result

    @classmethod
    def getUserByUserName(cls, userName):
        s = getdb()
        stmt = select(User).where(User.UserName == userName)
        result = s.scalars(stmt)
        return result

    @classmethod
    async def updateUser(cls, receivedJson):
        jsondict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        s = getdb()

        try:
            # 查找现有用户
            stmt = select(User).where(User.UserId == jsondict["UserId"])
            result = await s.execute(stmt)
            user = result.scalars().first()

            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            #只有管理员能修改权限
            if user.UserClass == 1:
                user.UserClass = jsondict.get("UserClass", user.UserClass)
            # 更新用户信息
            user.UserName = jsondict.get("UserName", user.UserName)
            user.motto = jsondict.get("Motto", user.motto)
            if "LastLogintime" in jsondict:
                user.LastLogintime = datetime.strptime(jsondict["LastLogintime"], date_format)
            user.gender = jsondict.get("Gender", user.gender)
            user.password = jsondict.get("Password", user.password)
            user.numofShares = jsondict.get("NumOfShares", user.numofShares)

            # 提交更新
            s.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="User not found")

    @classmethod
    def updateUserbyObject(cls, founduser: schemas.UserResponse):
        date_format = "%Y-%m-%d %H:%M:%S"
        s = getdb()
        try:
            # 查找现有用户
            stmt = select(User).where(User.UserId == founduser.UserId)
            result = s.execute(stmt)
            user = result.scalars().first()

            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            if user.UserClass == 1:
                user = user.values(UserClass=founduser.UserClass)
            user = user.values(
                UserName=founduser.UserName,
                motto=founduser.motto,
                gender=founduser.gender,
                password=founduser.password,
            )

            s.execute(user)
            s.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="User not found")
    @classmethod
    async def deleteUserByUserId(cls, receivedJson, userId):
        jsondict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        s = getdb()
        try:
            # 查找现有用户
            stmt = select(User).where(User.UserId == userId)
            result = await s.execute(stmt)
            user = result.scalars().first()

            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            if user.UserClass != 1:
                print("Permission denied: You are not admin")
                return
            stmt = select(User).where(User.UserId == userId)
            result = s.execute(stmt).scalars().first()
            s.delete(result)
            s.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="User not found")

    @classmethod
    def userLogin(cls, userinfo: schemas.UserLogin):
        s = getdb()
        userName = userinfo.UserName
        password = userinfo.password

        stmt = select(User).where(User.UserName == userName)
        result = s.execute(stmt)
        user = result.scalars().first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if password != user.password:
            raise HTTPException(status_code=401, detail="Incorrect password")

        return schemas.returnStatus(status="Success",message="Login Successful")


if __name__ == "__main__":
    mainuser = '{"UserId":2, "UserClass":1, "UserName":"Mitsuhiro", "motto":"Hello", "LastLogintime":"2024-05-29 00:00:00", "gender":"Male", "password":"123456", "numofShares": 6}'#json
    #UserCURD.createUserbyJson(mainuser)
    session = getdb()
    main = UserCURD.getUserByUserId(2)
    userinfo = schemas.UserLogin(UserName="Mitsuhiro", password="123456")
    print(UserCURD.userLogin(userinfo))

