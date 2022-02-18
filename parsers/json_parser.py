def json_to_table(response):
    formatted_table = ''
    table_data = {}
    column_max_length = {}

    # get the minimum length of column ( useful when the column title is bigger than the actual column data )
    # initialise an empty list for each column
    for key in response[0].keys():
        column_max_length[key] = len(key)
        table_data[key] = []

    # get the maximum length needed for each column
    # add each element to the corresponding column list
    for elem in response:
        for key in elem.keys():
            column_max_length[key] = max(len(str(elem[key])), column_max_length[key])
            table_data[key].append(str(elem[key]))

    # generate the table head
    for key in table_data.keys():
        spacing = ' ' * (column_max_length[key] - len(key) + 1)
        formatted_table += f'{key}' + spacing

    # line of '-' used to separate table head form table data
    formatted_table += '\n' + len(formatted_table) * '-' + '\n'

    # generate the table rows
    for line in range(len(response)):
        for key in table_data.keys():
            spacing = ' ' * (column_max_length[key] - len(table_data[key][line]) + 1)
            formatted_table += f'{table_data[key][line]}' + spacing
        formatted_table += '\n'

    return formatted_table
