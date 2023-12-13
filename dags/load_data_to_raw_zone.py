import psycopg2
from bs4 import BeautifulSoup
import requests
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago


location = 'berlin'
url = 'https://www.quandoo.de/en/result?destination=' + location

def get_total_page():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    total_page = soup.find_all('button', class_='sc-1vrhx70-1')
    last_page = total_page[len(total_page)-1].string
    return last_page

def get_restaurants(page):
    url = 'https://www.quandoo.de/en/result?destination=' + location + f"&page={page}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    restaurants = soup.find_all('div', class_='kvjosH')
    return restaurants

def get_restaurant(restaurant):               
    #scrapping for each element that is needed in DB which are (name, cousin, price_range, rating)
    name = restaurant.find('h3', class_ = 'jjhqNf').string
    replaced_name = name.replace("'", "").replace('"', "")
    cousin = restaurant.find('span', class_ = 'kPKdEs').string
    price_range_span = restaurant.find_all('span', class_ = 'jpCGqx')
    #jpCGqx class for price range is scrapped by twice might couse of commented lines on FE
    price_range = len(price_range_span)//2
    rating = restaurant.find('div', class_ = 'WkOwr')
    if rating is not None:
        rating = rating.text.split('/')[0]
    else:
        rating = ''
    restaurant = (replaced_name, cousin, price_range, rating)
    return restaurant
 
def build_query(query):
    query = ''.join([str(e) for e in query])
    return query
    
    
def load_data_to_raw_zone():
    total_page = int(get_total_page())
    page = 1
    query = []
    
    for page in range(1, total_page+1):
        restaurants = get_restaurants(page)
        for restaurant in restaurants:
            restaurant = get_restaurant(restaurant)
            query.append(f"INSERT INTO public.restaurants(name, category, price_range, rating) VALUES{restaurant};")
    
    query = build_query(query)

    try:     
        #connection for the database
        conn = psycopg2.connect(
            database = "airflow",
            user = "airflow",
            password = "airflow",
            host='postgres',
            port=5432
        )
        
        cur = conn.cursor()

        #truncate table before loading the data
        cur.execute("TRUNCATE TABLE public.restaurants")
        #load data
        cur.execute(query)

        conn.commit()    
    
    except err: 
        print(err)


args = {
    'owner': 'Ezgi Karvan',
    'start_date': days_ago(1)
}

dag = DAG(
    dag_id = 'load_data_to_raw_zone',
    default_args = args,
    schedule_interval = None
)

with dag:
    load_data_to_raw_zone = PythonOperator(
        task_id = 'load_data_to_raw_zone',
        python_callable = load_data_to_raw_zone,
    )
    