"""Модуль содержит форматы описания целей"""
from ipaddress import *


class Target:
    """Класс содержит формат описания целелей, которые будет использовать инструмент для выявления уязвимостей."""
    idcounter = 1 #счетчик для self.unique_id
    def __init__(self, domain: str = None):

        self.unique_id = Target.idcounter
        Target.idcounter +=1
        self.domain = domain
        #self.ip = ip_address(ip) #айпишник пусть вычисляется через whois https://www.thepythoncode.com/article/extracting-domain-name-information-in-python
        #self.name = name