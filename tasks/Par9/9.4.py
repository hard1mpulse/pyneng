ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def convert_config_to_dict(config_filename):
    '''
    Возвращает словарь,где все команды глобальной конфигурации являются ключами,
    а в случае если у нее есть подкоманды, они записываются в список строк как значение этого ключа
    Как аргумент ожидает название файла конфигурации
    '''
    conf_dict={}
    ignore = ['duplex', 'alias', 'Current configuration']
    with open('Par9_files/'+config_filename,'r') as f:
        for line in f:
            skip_line=False
            is_it_subcmd=False
            if '!' in line:
                skip_line=True
            elif line.startswith(' '):
                is_it_subcmd=True
            else:
                skip_line=ignore_command(line,ignore)
            if not skip_line and not is_it_subcmd:
                a=conf_dict.setdefault(line)
                main_cmd=line
                conf_dict[main_cmd]=[]
            elif is_it_subcmd:
                conf_dict[main_cmd].append(line)
            else:
                pass
    return(conf_dict)
file=input('Enter cfg filename: ')
result=convert_config_to_dict(file)
print(result)