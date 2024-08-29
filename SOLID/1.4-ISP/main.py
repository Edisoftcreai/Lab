from abc import ABC, abstractmethod

class UserManager(ABC):
    @abstractmethod
    def update_profile(self, user_id: str, profile_data: dict):
        pass

    @abstractmethod
    def manage_permissions(self, user_id: str, permissions: dict):
        pass

    @abstractmethod
    def generate_report(self, user_id: str):
        pass

class RegularUser(UserManager):
    def update_profile(self, user_id: str, profile_data: dict):
        print(f"Updating profile for user {user_id} with data {profile_data}")

    def manage_permissions(self, user_id: str, permissions: dict):
        raise NotImplementedError("RegularUser does not support managing permissions.")

    def generate_report(self, user_id: str):
        raise NotImplementedError("RegularUser does not support generating reports.")
