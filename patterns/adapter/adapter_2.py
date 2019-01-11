import abc


class Cable(abc.ABC):

    @abc.abstractmethod
    def connect(self):
        pass


class IPhoneCableAdapter(Cable):

    def __init__(self, cellphone):
        self.cellphone = cellphone

    def connect(self):
        self.cellphone.charge_iphone()


class GalaxyCableAdapter(Cable):

    def __init__(self, cellphone):
        self.cellphone = cellphone

    def connect(self):
        self.cellphone.charge_galaxy()


class IPhone:

    def charge_iphone(self):
        print('Charging iphone')


class Galaxy:

    def charge_galaxy(self):
        print('Charging galaxy')


class CellphoneOwner:

    def __init__(self, cable):
        self._cable = cable

    def connect_cellphone(self):
        self._cable.connect()


if __name__ == '__main__':
    iphone = IPhone()
    galaxy = Galaxy()

    iphone_adapter = IPhoneCableAdapter(iphone)
    galaxy_adapter = GalaxyCableAdapter(galaxy)

    iphone_owner = CellphoneOwner(iphone_adapter)
    iphone_owner.connect_cellphone()

    galaxy_owner = CellphoneOwner(galaxy_adapter)
    galaxy_owner.connect_cellphone()
