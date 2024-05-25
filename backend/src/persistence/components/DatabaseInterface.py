from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def save_device(self, device_id: str, device_info: dict):
        pass

    @abstractmethod
    def get_device(self, device_id: str):
        pass

    @abstractmethod
    def delete_device(self, device_id: str):
        pass

    @abstractmethod
    def save_group(self, group_id: str, group_info: dict):
        pass

    @abstractmethod
    def get_group(self, group_id: str):
        pass

    @abstractmethod
    def log_event(self, event_info: dict):
        pass

    @abstractmethod
    def get_events(self, device_id: str):
        pass
