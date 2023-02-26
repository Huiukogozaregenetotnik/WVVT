from import_targets import *
from instruments import *
""" Модуль содержит функции запуска сканов поиска целей и уязвимостей"""

def vuln_scan(target_list):
    """Спрашивает у пользователя в отношении каких целей надо запустить какие сканирования. Берет соответвующие объекты класса Targets и передает в объекты класса Instruments"""
    for target in target_list:
        run_owasp_zap(target.domain)
