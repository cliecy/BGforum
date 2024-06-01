from sqlalchemy import select, delete, update
from sqlalchemy.exc import NoResultFound
from backend.dbapi.models import User
from fastapi import HTTPException
from datetime import datetime
import json
from backend.dbapi.models import User
from backend.dbapi.database import getdb
from backend.networkapi import schemas


class UserCURD:
    @classmethod
    def createUserbyJson(cls, receivedJson: str):
        s = getdb()
        jsondict = json.loads(receivedJson)
        date_format = "%Y-%m-%d %H:%M:%S"
        user = User(
            #UserId=jsondict["UserId"],
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
        s.close()

    @classmethod
    def createUserbyObject(cls, user: schemas.UserCreate):
        s = getdb()

        existing_user = select(User).where(UserName=user.UserName)
        existing_user = s.scalars(existing_user).first()
        #existing_user = s.query(User).filter_by(UserName=user.UserName).first()
        if existing_user is not None:
            raise HTTPException(status_code=400, detail="User already exists")

        dbuser = User(
            #UserId=user.UserId,
            UserName=user.UserName,
            motto=user.motto,
            LastLogintime=user.LastLogintime,
            gender=user.gender,
            password=user.password,
            numofShares=user.numofShares,
        )
        s.add(dbuser)
        s.commit()
        s.close()
        return {"status": "Success", "message": "Register Successful"}
        
    @classmethod
    def getUserByUserId(cls, userId):
        s = getdb()
        stmt = select(User).where(User.UserId == userId)
        result = s.scalars(stmt).first()
        s.close()
        return result

    @classmethod
    def getUserByUserName(cls, userName):
        s = getdb()
        stmt = select(User).where(User.UserName == userName)
        result = s.scalars(stmt)
        s.close()
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
        finally:
            s.close()

    @classmethod
    def updateUserbyObject(cls, founduser: schemas.UserResponse):
        date_format = "%Y-%m-%d %H:%M:%S"
        s = getdb()
        try:
            # 查找现有用户
            stmt = select(User).where(User.UserId == founduser.UserId)
            result = s.execute(stmt).scalars().first()

            if result.UserClass == 1:
                stmt = update(User).where(User.UserId == founduser.UserId).values(UserClass=1)
                s.execute(stmt)
            stmt = update(User).where(User.UserId == founduser.UserId).values(UserName=founduser.UserName,motto=founduser.motto,gender=founduser.gender)
            existing_user = select(User).where(UserName=founduser.UserName)
            existing_user = s.scalars(existing_user).first()
            # existing_user = s.query(User).filter_by(UserName=user.UserName).first()
            if existing_user is not None:
                raise HTTPException(status_code=400, detail="UserName already exists")
            s.execute(stmt)
            s.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="User not found")
        finally:
            s.close()

    @classmethod
    def updateSharenumberbyObject(cls, founduser: schemas.UserResponse):
        s = getdb()
        try:
            # 查找现有用户
            stmt = select(User).where(User.UserId == founduser.UserId)
            result = s.execute(stmt)
            user = result.scalars().first()

            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            stmt = update(User).where(User.UserId == founduser.UserId).values(numofshares=user.numofShares+1)
            s.execute(stmt)
            s.commit()
        except NoResultFound:
            raise HTTPException(status_code=404, detail="User not found")
        finally:
            s.close()
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
        finally:
            s.close()

    @classmethod
    def getUserIdbyName(cls,UserName: str):
        s=getdb()
        stmt = select(User).where(User.UserName==UserName)
        result = s.execute(stmt)
        if not result:
            raise HTTPException(status_code=404, detail="UserName not found")
        result = result.scalars().first()
        s.close()
        return result.UserId

    @classmethod
    def userLogin(cls, userinfo: schemas.UserLogin):
        s = getdb()
        userName = userinfo.UserName
        password = userinfo.password

        stmt = select(User).where(User.UserName == userName)
        result = s.execute(stmt)
        user = result.scalars().first()
        print("hello")
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if password != user.password:
            raise HTTPException(status_code=401, detail="Incorrect password")
        s.close()
        return {"status": "Success", "message": "Login Successful"}


if __name__ == "__main__":
    #mainuser = '{"UserClass":1, "UserName":"Hitsuhiro", "motto":"Hello", "LastLogintime":"2024-05-29 00:00:00", "gender":"Male", "password":"123456", "numofShares": 0}'#json
    #print(UserCURD.createUserbyJson(mainuser))
    #user2 = schemas.UserResponse(UserName="Brian",motto="Mamba Out",LastLogintime="2024-06-01 23:01:59",gender="Male",password="123456",passwordconfirm="123456",numofShares=0)
    #print(UserCURD.createUserbyObject(user2))
    #main = UserCURD.getUserByUserId(2)
    #userinfo = schemas.UserLogin(UserName="Brian", password="123456")
    #print(UserCURD.userLogin(userinfo))
    print(UserCURD.getUserIdbyName("Mitsuhiro"))


