create_table_querries = []

page_view_dim_table = """CREATE TABLE IF NOT EXISTS 
page_views_dim (id SERIAL PRIMARY KEY, 
name varchar)"""

create_table_querries.append(page_view_dim_table)

currency_dim_table = """CREATE TABLE IF NOT EXISTS
currency_dim (id SERIAL PRIMARY KEY,
currency_name varchar)"""

create_table_querries.append(currency_dim_table)

create_page_view_frequency_table = """CREATE TABLE IF NOT EXISTS
page_view_frequency_fact (id SERIAL PRIMARY KEY,
event_id varchar, 
page_view_id int REFERENCES page_views_dim(id),
page_view_frequency int)"""

create_table_querries.append(create_page_view_frequency_table)

billing_cycle_dim_table = """CREATE TABLE IF NOT EXISTS
billing_cycle_dim (id SERIAL PRIMARY KEY,
billing_cycle varchar)""" 

create_table_querries.append(billing_cycle_dim_table)

event_info_dim_table = """CREATE TABLE IF NOT EXISTS
events_information_dim (id SERIAL PRIMARY KEY,
event_id varchar, event_name varchar, account_id varchar,
original_timestamp timestamp, recieved_at timestamp, 
url_event_was_triggered_on varchar)"""

create_table_querries.append(event_info_dim_table)

account_informartion_dim_table = """CREATE TABLE IF NOT EXISTS
accounts_information_dim (id SERIAL PRIMARY KEY,
event_id varchar, account_id varchar, 
organization_id varchar)"""

create_table_querries.append(account_informartion_dim_table)

event_information_fact_table = """CREATE TABLE IF NOT EXISTS
event_information_fact (id SERIAL PRIMARY KEY,
sites_count int,
currency_id int REFERENCES currency_dim(id),
billing_cycle_id int REFERENCES billing_cycle_dim(id),
event_information_id int REFERENCES events_information_dim(id),
account_information_id int REFERENCES accounts_information_dim(id))"""

create_table_querries.append(event_information_fact_table)