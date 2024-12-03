import pytest

from handlers.admin_handler import AdminHandler
from handlers.seller_handler import SellerHandler
from handlers.buyer_handler import BuyerHandler
from handlers.guest_handler import GuestHandler
from helper.handler_helper import CommandHandlerFactory


def test_handler_factory_creation_admin():
    helper = CommandHandlerFactory()
    admin_handler = helper.get_handler("admin")
    assert isinstance(admin_handler, AdminHandler)


def test_handler_factory_creation_seller():
    helper = CommandHandlerFactory()
    seller_handler = helper.get_handler("seller")
    assert isinstance(seller_handler, SellerHandler)


def test_handler_factory_creation_buyer():
    helper = CommandHandlerFactory()
    buyer_handler = helper.get_handler("buyer")
    assert isinstance(buyer_handler, BuyerHandler)


def test_handler_factory_invalid_type():
    helper = CommandHandlerFactory()
    guest_handler = helper.get_handler("invalid_type")
    assert isinstance(guest_handler, GuestHandler)
