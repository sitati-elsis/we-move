drop_page_views_dim_table = "DROP TABLE IF EXISTS page_views_dim CASCADE"
drop_currency_dim_table = """DROP TABLE IF EXISTS
currency_dim CASCADE"""
drop_page_view_frequency_fact_table = """DROP TABLE IF EXISTS
page_view_frequency_fact CASCADE"""
drop_billing_cycle_dim_table = """ DROP TABLE IF EXISTS
billing_cycle_dim CASCADE"""
drop_event_info_dim_table = """DROP TABLE IF EXISTS
events_information_dim CASCADE"""
drop_accounts_information_dim_table = """DROP TABLE IF EXISTS
accounts_information_dim CASCADE"""
drop_event_information_fact_table = """DROP TABLE IF EXISTS
event_information_fact  CASCADE"""

drop_tables_querries = [drop_page_views_dim_table, 
drop_page_view_frequency_fact_table,
drop_currency_dim_table, drop_billing_cycle_dim_table,
drop_event_info_dim_table, drop_accounts_information_dim_table,
drop_event_information_fact_table]