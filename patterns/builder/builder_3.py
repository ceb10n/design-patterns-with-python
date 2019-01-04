class Cellphone:

    def __init__(self, display=None, camera=None):
        self.display = display
        self.camera = camera

    def __repr__(self):
        return '<Cellphone: display="{}" camera="{}">'.format(
            self.display, self.camera)


class SamsungBuilder:

    def __init__(self):
        self.cellphone = Cellphone()

    def create_display(self):
        print('Creating some fancy samsung display')
        self.cellphone.display = 'Samsung display'

    def create_camera(self):
        print('Creating some high tech samsung camera')
        self.cellphone.camera = 'Samsung Camera'

    def get_cellphone(self):
        return self.cellphone


class AppleBuilder:

    def __init__(self):
        self.cellphone = Cellphone()

    def create_display(self):
        print('Creating some fancy apple display')
        self.cellphone.display = 'Apple display'

    def create_camera(self):
        print('Creating some high tech apple camera')
        self.cellphone.camera = 'Apple Camera'

    def get_cellphone(self):
        return self.cellphone


class CellphoneManufacturer:

    def build_cellphone(self, builder):
        builder.create_display()
        builder.create_camera()


if __name__ == '__main__':
    manufacturer = CellphoneManufacturer()

    samsung_builder = SamsungBuilder()
    apple_builder = AppleBuilder()
    
    manufacturer.build_cellphone(samsung_builder)
    galaxy = samsung_builder.get_cellphone()
    print(galaxy)

    manufacturer.build_cellphone(apple_builder)
    iphone = apple_builder.get_cellphone()
    print(iphone)
