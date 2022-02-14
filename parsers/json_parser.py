def json_to_table(response):
    result = ''
    table_data = {}
    data_max_length = {}
    counter = 0
    for elem in response:
        counter += 1
        for key in elem.keys():
            if key not in table_data:
                table_data[key] = [str(elem[key])]
                data_max_length[key] = len(key)
                if len(str(elem[key])) > data_max_length[key]:
                    data_max_length[key] = len(str(elem[key]))
            else:
                table_data[key].append(str(elem[key]))
                if len(str(elem[key])) > data_max_length[key]:
                    data_max_length[key] = len(str(elem[key]))

    for key in table_data.keys():
        result += f'{key}' + ' ' * (data_max_length[key] - len(key) + 1)
    result += '\n' + len(result)*'-' + '\n'
    for line in range(counter):
        for key in table_data.keys():
            result += f'{table_data[key][line]}' + ' ' * (data_max_length[key] - len(table_data[key][line]) + 1)
        result += '\n'
    return result
