from pymongo import MongoClient
import threading
import time
import os

print("SharkPoint Loop System")
print("Created by Neko.")

print("起動しています。。")

db = MongoClient("mongodb://localhost:27017")
db_point = db["Main"].SharkBotGoldPoint
db_gold = db["Main"].SharkBotGoldPoint
print("データベースに接続しました。")

def gold_center_add():
    while True:
        for db_g in db_gold.find():
            user_data = db_point.find_one({"_id": db_g["_id"]})
            if user_data:
                db_gold.update_one({"_id": db_g["_id"]}, {"$inc": {"count": 1}})
            else:
                db_gold.insert_one({"_id": db_g["_id"], "count": 1})
            print(f"錬金術研究所: 「{db_g["_id"]}」にポイントを追加しました。")
        print("錬金術研究所: 1ポイントを追加完了しました。")
        time.sleep(3600)

gold = threading.Thread(target=gold_center_add)
gold.start()

print("起動しました。")
print("============================")
