import yaml

 
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def __str__(self):
        return f"User: {self.email}, password: {self.password}"
    
class Config:
    def __init__(self,path_to_yaml_file: str):
        with open(path_to_yaml_file, "rb") as yaml_content:
            config_structure = yaml.safe_load(yaml_content)
            self.users = [User(**user_dict) for user_dict in config_structure["users"]]
            self.sender_email = config_structure["sender_email"]
            self.sender_email_password = config_structure["sender_email_password"]
            self.receiver = config_structure["receiver_email"]
            self.screenshot_path = config_structure["screenshot_path"]

config = Config("../secret.yaml")
