"""A closer look to Abstract Factory in Python."""
import abc


class CellphoneFactory(abc.ABC):

    @abc.abstractmethod
    def create_high_end_cell(self):
        pass


class HighendProduct(abc.ABC):

    @abc.abstractmethod
    def take_a_picture(self):
        pass


class IPhone(HighendProduct):

    def take_a_picture(self):
        print("Taking a real good picture from IPhone")


class Galaxy(HighendProduct):

    def take_a_picture(self):
        print("Taking a real good picture from Galaxy")


class SamsungFactory(CellphoneFactory):

    def create_high_end_cell(self):
        return Galaxy()


class AppleFactory(CellphoneFactory):

    def create_high_end_cell(self):
        return IPhone()


class CellphoneStore:

    def show_picture_to_customer(self, cellphone):
        cellphone.take_a_picture()


class SpecializedCellphoneStore:

    def __init__(self, cellphone_factory):
        self.cellphone = cellphone_factory.create_high_end_cell()

    def show_picture_to_customer(self):
        self.cellphone.take_a_picture()


if __name__ == '__main__':
    apple_factory = AppleFactory()
    samsung_factory = SamsungFactory()

    cellphone_store = CellphoneStore()
    cellphone_store.show_picture_to_customer(apple_factory.create_high_end_cell())
    cellphone_store.show_picture_to_customer(samsung_factory.create_high_end_cell())

    specialized_apple_store = SpecializedCellphoneStore(apple_factory)
    specialized_samsung_store = SpecializedCellphoneStore(samsung_factory)

    specialized_apple_store.show_picture_to_customer()
    specialized_samsung_store.show_picture_to_customer()
