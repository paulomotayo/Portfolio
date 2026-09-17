import json


class Manager:
    def __init__(self):
        try:
            with open("data.json") as file:
                self.history = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.history = {}

    @staticmethod
    def check_string(*text):
        if not all(isinstance(x, str) for x in text):
            raise TypeError("All inputs must be strings")

    def save(self):
        with open("data.json", "w") as file:
            json.dump(self.history, file, indent=4)

    def add(self, site, username, password):
        self.check_string(site, username, password)
        
        site = site.lower().strip()
        username = username.strip()
        password = password.strip()

        if not (site and username and password):
            return "Fields cannot be empty"
       
        if site in self.history:
            return "Site already exists"
       
        self.history[site] = {"username": username, "password": password}
       
        self.save()


    def get(self, site):
        self.check_string(site)

        return self.history.get(site.lower().strip())


    def delete(self, site):
        self.check_string(site)
        
        site = site.lower().strip()

        if site not in self.history:
            return f"{site} not found"
        
        del self.history[site]
        
        self.save()
        
        return "Deletion successful"


    def list_sites(self):
        return tuple(sorted(self.history))


    def update(self, site, username="", password=""):
        self.check_string(site, username, password)
                
        site = site.lower().strip()
        
        if site not in self.history:
            return f"{site} not found"

        username = username.strip()
        password = password.strip()

        if not username and not password:
            return "Update either username or password or both"
        
        if username:
            self.history[site]["username"] = username

        if password:
            self.history[site]["password"] = password

        self.save()

        return "Updated successfully"
