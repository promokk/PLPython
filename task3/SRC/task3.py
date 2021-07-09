import logging


class Barrel:
    def __init__(self, limit): 
        self.limit = limit
        self.volume = limit
        self.countPour= 0
        self.countPourError = 0
        self.volumePouPTrue = 0
        self.volumePourFalse = 0
        self.percentPourError = 0
        self.countScoop = 0
        self.countScoopError = 0
        self.volumeScoopTrue = 0
        self.volumeScoopFalse = 0
        self.percentScoopError = 0
    
    # Наливаем воду
    def pour(self, x: int):
        if x <= 0:
            return print("usage")
        self.countPour += 1
        if self.volume + x > self.limit:
            self.countPourError += 1
            self.volumePourFalse += x
            self.percentPourError = self.countPourError / self.countPour * 100
        else:
            self.volume += x
            self.volumePouPTrue += x

    # Черпаем воду
    def scoop(self, x: int):
        if x <= 0:
            return print("usage")
        self.countScoop += 1
        if x > self.volume:
            self.countScoopError += 1
            self.volumeScoopFalse += x
            self.percentScoopError = self.countScoopError / self.countScoop * 100
        else:
            self.volume -= x
            self.volumeScoopTrue += x
    
    def logCheck(self):
        logging.basicConfig(filename="myLog.log", level=logging.INFO)
        logging.info(f"Объем бочки - {self.limit}")
        logging.info(f"Текущий объем воды в бочке - {self.volume}")
        logging.info(f"Кол-во попыток pour - {self.countPour}")
        logging.info(f"Процент ошибок pour - {self.percentPourError}%")
        logging.info(f"Объем pour за период - {self.volumePouPTrue}")
        logging.info(f"Объем pourError за период - {self.volumePourFalse}")
        logging.info(f"Кол-во попыток scoop - {self.countScoop}")
        logging.info(f"Процент ошибок scoop - {self.percentScoopError}%")
        logging.info(f"Объем scoop за период - {self.volumeScoopTrue}")
        logging.info(f"Объем scoopError за период - {self.volumeScoopFalse}")


def main():
    barrel = Barrel(200)
    barrel.pour(10)
    barrel.scoop(20)
    barrel.scoop(90)
    barrel.scoop(110)
    barrel.scoop(150)
    barrel.pour(30)
    barrel.pour(50)
    barrel.pour(20)
    barrel.pour(150)
    barrel.pour(-1)
    barrel.scoop(-1)
    barrel.logCheck()



if __name__ == '__main__':
    main()