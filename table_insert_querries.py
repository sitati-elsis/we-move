page_view_dim_table_insert = """INSERT INTO 
page_views_dim (name)
VALUES (%s)"""

currency_dim_table_insert = """INSERT INTO
currency_dim (currency_name)
VALUES (%s)"""

page_view_frequency_fact_table_insert = """INSERT INTO
page_view_frequency_fact (event_id, page_view_id,
page_view_frequency)
VALUES (%s, %s, %s)"""

billing_cycle_dim_table_insert = """INSERT INTO 
billing_cycle_dim (billing_cycle)
VALUES (%s)"""

event_info_dim_table_insert = """INSERT INTO 
events_information_dim (event_id,
account_id, event_name,
original_timestamp, recieved_at,
url_event_was_triggered_on)
VALUES (%s, %s, %s, %s, %s, %s)"""

account_informartion_dim_table_insert = """INSERT INTO
accounts_information_dim (event_id, account_id, 
organization_id)
VALUES (%s, %s, %s)"""


event_information_fact_table_insert = """INSERT INTO
event_information_fact (sites_count,
currency_id, billing_cycle_id,
event_information_id, account_information_id)
VALUES (%s, %s, %s, %s, %s)"""