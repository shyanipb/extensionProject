import sqlite3

conn = sqlite3.connect('systeminfo.db')
c = conn.cursor()


def get_value(item, **kwargs):
    info = item.strip().split(':')
    val = info[1].strip().split(',')
    return val[0].strip()


def insert_data(filename, **kwargs):
    # read all the lines of the file
    with open(filename) as f:
        file_data = f.readlines()

    kernel_version = ''
    product_type = ''
    product_version = ''

    for item in file_data:
        if 'Kernel version' in item:
            kernel_version = get_value(item)
        elif 'Product type' in item:
            product_type = get_value(item)
        elif 'Product version' in item:
            product_version = get_value(item)

    c.execute(
        '''insert into system_information
        (Kernel_version, Product_type, Product_version)
        values(?, ?, ?)''',
        (kernel_version, product_type, product_version,)
    )
    conn.commit()
