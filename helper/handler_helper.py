from handlers.admin_handler import AdminHandler
from handlers.seller_handler import SellerHandler
from handlers.buyer_handler import BuyerHandler
from handlers.guest_handler import GuestHandler


class CommandHandlerFactory:
    @staticmethod
    def get_handler(user_role):
        if user_role == "admin":
            return AdminHandler()
        elif user_role == "seller":
            return SellerHandler()
        elif user_role == "buyer":
            return BuyerHandler()
        else:
            return GuestHandler()
