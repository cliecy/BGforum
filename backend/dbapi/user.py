from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from BGforum.backend.dbapi.models import User
from fastapi import HTTPException
import datetime
import json
from BGforum.backend.dbapi.database import getdb


class UserCURD:
    @classmethod
    def createUser(cls, receivedJson: str):
        s = getdb()
        jsondict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        user = User(
            UserId=jsondict["UserId"],
            UserClass=jsondict["UserClass"],
            UserName=jsondict["UserName"],
            motto=jsondict["motto"],
            LastLogintime=datetime.datetime.strptime(jsondict["LastLogintime"], date_format),
            gender=jsondict["gender"],
            password=jsondict["password"],
            numofShares=jsondict["numofShares"],
        )
        s.add(user)
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
                user.LastLogintime = datetime.datetime.strptime(jsondict["LastLogintime"], date_format)
            user.gender = jsondict.get("Gender", user.gender)
            user.password = jsondict.get("Password", user.password)
            user.numofShares = jsondict.get("NumOfShares", user.numofShares)

            # 提交更新
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


if __name__ == "__main__":
    mainuser = '{"UserId":2, "UserClass":1, "UserName":"Mitsuhiro", "motto":"Hello", "LastLogintime":"2024-05-29 00:00:00", "gender":"Male", "password":"123456", "numofShares": 6}'#json
    UserCURD.createUser(mainuser)
    session = getdb()
    main = UserCURD.getUserByUserId(1, session)
    print(main.UserId, main.UserClass, main.UserName, main.motto, main.LastLogintime)
