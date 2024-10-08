from abc import ABC, abstractmethod

class ProfileManager(ABC):
    @abstractmethod
    def update_profile(self, user_id: str, profile_data: dict):
        pass

class ReportManager(ABC):
    @abstractmethod
    def generate_report(self, user_id: str):
        pass

class UserManager(ABC):
    @abstractmethod
    def manage_permissions(self, user_id: str, permissions: dict):
        pass

class RegularUser(ProfileManager):
    def update_profile(self, user_id: str, profile_data: dict):
        print(f"Updating profile for user {user_id} with data {profile_data}")

class AdministratorUser(ProfileManager, UserManager, ReportManager):
    def update_profile(self, user_id: str, profile_data: dict):
        print(f"Updating profile for user {user_id} with data {profile_data}")

    def manage_permissions(self, user_id: str, permissions: dict):
        print(f"Updating permissions for user {user_id} with permissions {permissions}")
   
    def generate_report(self, user_id: str):
        print(f"Report for user {user_id}")