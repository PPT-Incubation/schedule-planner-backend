from pydantic import BaseSettings

class Settings(BaseSettings):
    # python 3.4 Connection string, 3.6 or later is unuseable for passing phase issue
    connection_string : str = "mongodb://ppt:parapencarituhan@cluster0-shard-00-00.m5kxu.mongodb.net:27017,cluster0-shard-00-01.m5kxu.mongodb.net:27017,cluster0-shard-00-02.m5kxu.mongodb.net:27017/schedule-planner?ssl=true&replicaSet=atlas-3qy7xb-shard-0&authSource=admin&retryWrites=true&w=majority"
    secret_key : str = "a8fd428cf86eca78df0350f2c54bed62c385576d0359f126b7b74071c8bd92ae"
    
settings = Settings()