import pandas as pd
import  os
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    if os.path.isfile('titanic.csv') == True:
        return pd.read_csv('titanic.csv')
    else:
        titanic_df  = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        titanic_df.to_csv('titanic.csv')
        return pd.read_csv('titanic.csv')


iris_sql="SELECT measurements.measurement_id, \
    measurements.sepal_length, measurements.sepal_width, measurements.petal_length, \
        measurements.petal_width, species.species_name, species.species_id \
            FROM measurements JOIN species ON(species.species_id=measurements.species_id)"

def get_iris_data():
    if os.path.isfile('iris.csv') == True:
  
        return pd.read_csv('iris.csv')
    else:
         iris_df = pd.read_sql(iris_sql,get_connection('iris_db'))
         iris_df.to_csv('iris.csv')
         return pd.read_csv('iris.csv')
    


telco_sql= " select * \
from customers \
join customer_contracts using(customer_id) \
join internet_service_types using(internet_service_type_id) \
join payment_types using(payment_type_id) "

def get_telco_data():
    if os.path.isfile('telco.csv') == True:
        return pd.read_csv('telco.csv')
    else:
         df = pd.read_sql(telco_sql,get_connection('telco_churn')),
         return df.read_csv('telco.csv')