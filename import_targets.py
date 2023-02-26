""""Этот модуль содержит функции для импорта целей, ручного или автоматического из инструментов"""

from Targets import Target

def manual_create_targets():
    """Запрашивает данные о целях у пользователя, создает объекты класса Targets"""
    target_list = [] #создаем пустой список куда будем кидать ссылки на созданые цели
    domain_from_user = input('Enter domain to analyze: ')
    target_list.append(Target(domain_from_user)) #создаем цель и помещаем ее в список
    print(f'We have created next targets: {target_list}')
    return target_list


#def import_targets():
    """Импортирует данные о целях из популярных инструментов, создает объекты класса Targets. Информирует о промежуточных результатах """


