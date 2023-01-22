from os import getenv

TOKEN = getenv("TOKEN", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority")
