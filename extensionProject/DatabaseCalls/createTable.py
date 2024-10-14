import sqlite3

conn = sqlite3.connect('systeminfo.db')
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS system_information (      
                Machine_Name text,                                    
                Kernel_version text,                                  
                Product_type text,                                    
                product_version text,                                 
                Registered_organization text,                         
                registered_owner text,                                
                system_root text,                                     
                processors text,                                      
                physical_memory text                                  
                )""")
