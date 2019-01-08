class Singleton:

    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance == None:
            Singleton._instance = Singleton()
        
        return Singleton._instance


if __name__ == '__main__':
    singleton_1 = Singleton().get_instance()
    singleton_2 = Singleton().get_instance()
    
    singleton_3 = Singleton.get_instance()
    singleton_4 = Singleton.get_instance()

    print(singleton_1 is singleton_2)
    print(singleton_3 is singleton_4)
    print(singleton_1 is singleton_3)
