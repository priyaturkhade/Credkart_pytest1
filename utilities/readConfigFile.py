import configparser

config = configparser.RawConfigParser()  # this (configparser.RawConfigParser) method is use  to read the data from
# config.ini
# file # .ini file we have # create to save the common data


config.read("F:\\Pycharm projects\\Credkart_pytest1\\Configuration\\config.ini")


class Readconfig:

    @staticmethod
    def getUserEmail():
        UserEmail = config.get('login data', 'UserEmail') # this is gpoing to fetch data from common data section and from Useremail field
        #config.get('section', 'Field')
        return UserEmail

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'Password')
        return Password

    @staticmethod
    def getFirst_Name():
        First_Name = config.get('Checkout data', 'First_Name')
        return First_Name

    @staticmethod
    def getLastName():
        LastName=config.get('Checkout data', 'LastName')
        return LastName

    @staticmethod
    def getPhoneNo():
        PhoneNo=config.get('Checkout data', 'PhoneNo')
        return PhoneNo

    @staticmethod
    def getAddress():
        Address=config.get('Checkout data', 'Address')
        return Address

    @staticmethod
    def getZip():
        Zip=config.get('Checkout data', 'Zip')
        return Zip

    @staticmethod
    def getState():
        State=config.get('Checkout data', 'State')
        return State

    @staticmethod
    def getOwnername():
        Ownername=config.get('Checkout data', 'Ownername')
        return Ownername

    @staticmethod
    def getCVV():
        CVV = config.get('Checkout data', 'CVV')
        return CVV

    @staticmethod
    def getcard_number01():
        card_number01 = config.get('Checkout data', 'card_number01')
        return card_number01

    @staticmethod
    def getcard_number02():
        card_number02 = config.get('Checkout data', 'card_number02')
        return card_number02

    @staticmethod
    def getcard_number03():
        card_number03 = config.get('Checkout data', 'card_number03')
        return card_number03

    @staticmethod
    def getcard_number04():
        card_number04 = config.get('Checkout data', 'card_number04')
        return card_number04
