# Databricks notebook source
import requests
import json

scope = 'key-vault-secrets'
base_url = dbutils.secrets.get(scope,"AzureDatabricksUrl")
Bearer_token =  dbutils.secrets.get(scope,"AzureDatabricksBearerToken")
endpoint = base_url + "api/2.1/jobs/create"
headers = {"Authorization": Bearer_token}

# COMMAND ----------

<<<<<<< HEAD
data_sail_load = r"""
{
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "sail_load",
=======
data = r"""
{

        "name": "sail_load_job_cluster",
        "email_notifications": {
            "no_alert_for_skipped_runs": false
        },
        "timeout_seconds": 0,
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
        "schedule": {
            "quartz_cron_expression": "26 15 0/12 * * ?",
            "timezone_id": "UTC",
            "pause_status": "PAUSED"
        },
        "max_concurrent_runs": 1,
        "tasks": [
            {
<<<<<<< HEAD
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "task_key": "silver_dim_customer",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "Y",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_customer",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_customer/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"CUSTOMER_ACCOUNT_SDUK\", \"CUSTOMERKEY\" ]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_customer",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INT_CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INT_CUSTOMER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DIVISION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXT_CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ACCOUNT_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACCOUNT_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTAL_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ACCOUNT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GLD_ACCOUNT_MAPPED_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ENABLE_CARRIER_UPDATE_FLAG\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CUSTOMERKEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DP_SERVICELINE_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DP_ORGENTITY_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MAPPED_WAREHOUSE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_HUB_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_customer"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_customer"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_dim_warehouse",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_warehouse",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_warehouse/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[\"WAREHOUSE_KEY\" ,\"SOURCE_SYSTEM_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_warehouse",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"WAREHOUSE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BUILDING_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTAL_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GLD_WAREHOUSE_MAPPED_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_warehouse"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_warehouse"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_dim_source_system",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "SOURCE_SYSTEM_KEY",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_source_system",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_source_system/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_source_system",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_GROUP\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DC_FSL_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_source_system"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_source_system"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_dim_carrier_los",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_carrier_los",
                        "src_folder_path": " /mnt/sail/bronze/gld360/inbound/landing/dim_carrier_los/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[\"CARRIER_LOS_KEY\",\"SOURCE_SYSTEM_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_carrier_los",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_DESC\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_NUMERIC_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"EXT_CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_GROUP\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GLD_CARRIER_MAPPED_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_HUB_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_carrier_los"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_carrier_los"
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_transportation",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"TRANSPORTATION_SDUK\"]",
                        "partition_keys": "[\"UTC_ORDER_PLACED_MONTH_PART_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"PICKUP_CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DROPOFF_CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EQUIPMENT_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_SUB_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_COMPANY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_COMPANY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_STATE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SCHEDULED_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_SCHEDULED_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_SCHEDULED_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACTUAL_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ACTUAL_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ACTUAL_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACTUAL_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ACTUAL_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ACTUAL_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_SHIPMENT_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_SHIPMENT_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_SHIPMENT_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_SHIPMENT_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_DELIVERY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_DELIVERY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_DELIVERY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_DELIVERY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PICKUP_CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DROPOFF_CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_WMS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_WMS_SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORIGINAL_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORIGINAL_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORIGINAL_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORIGINAL_SCHEDULED_DELIVERY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORIGINAL_SCHEDULED_DELIVERY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_EARLIEST_PICKUP_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_LATEST_PICKUP_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_EARLIEST_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_LATEST_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_1\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_1\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_1\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_1_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_1_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_2\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_2\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_2\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_2_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_2_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_3\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_3\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_3\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_3_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_3_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_4\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_4\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_4\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_4_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_4_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_5\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_5\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_5\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_5\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_5_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_5_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_6\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_6\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_6\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_6\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_6_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_6_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WMS_PO_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_MODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANS_ONLY_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_NOTES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COMMENTS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GFF_SHIPMENT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GFF_SHIPMENT_INSTANCE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SCOPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SECTOR\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DIRECTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"AUTHORIZER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DELIVERY_INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_CONTACT\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "additional_custom_column": "[{\"name\":\"UTC_ORDER_PLACED_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_ORDER_PLACED_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
                        "tgt_table_name": "fact_transportation"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_transportation",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_transportation_exception",
                "depends_on": [
                    {
                        "task_key": "silver_dim_carrier_los"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_exception",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_exception",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"TRANSPORTATION_EXCEPTION_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_exception",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UTC_EXCEPTION_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXCEPTION_CREATED_DATE_OTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXCEPTION_CREATED_DATE_OTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXCEPTION_CREATED_DATE_DTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXCEPTION_CREATED_DATE_DTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXCEPTION_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_EVENT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_REASON\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_REASON_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_CATEGORY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RESPONSIBLE_PARTY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_PRIMARY_INDICATOR\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"EXCEPTION_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_EXCEPTION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_WMS_SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_WMS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_transportation_exception"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_transportation_exception",
                "depends_on": [
                    {
                        "task_key": "silver_dim_carrier_los"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_dim_item",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_item",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_item/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[\"ITEM_KEY\",\"SOURCE_SYSTEM_KEY\",\"ITEM_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_item",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ITEM_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PART_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PART_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PRIMARY_CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DIMENSIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DIMENSIONS_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_LENGTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_WEIGHT_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_PRICE\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_PRICE_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERIAL_OR_LOT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HARMONIZED_TARIFF_SCHEDULE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UN_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVE_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STD_SKU_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STD_CASE_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CASE_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CASE_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CASE_DEPTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CASE_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"STD_PALLET_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PALLET_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PALLET_DEPTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PALLET_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PALLET_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"UNIT_PER_CASE\",\"nullable\":true,\"type\":\"decimal(22,0)\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ETL_OPS_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SKU_GRP11\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SKU_GRP1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STRATEGICGOODS_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_item"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_item",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_dim_service",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_service",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_service/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"SERVICE_KEY\", \"SERVICE_SDUK\" ]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_service",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"E2K_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"E2K_CHARGE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_NOT_REQUIRED\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_service"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_service"
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-2_2-12:4.7.0"
                        }
                    }
                ],
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_dim_geo_location",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_geo_location",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_geo_location/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[\"GEO_LOCATION_KEY\",\"SOURCE_SYSTEM_KEY\",\"GEO_LOCATION_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_geo_location",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"GEO_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"LOCATION_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTAL_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEO_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "dim_geo_location"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_dim_geo_location"
            },
            {
                "existing_cluster_id": "0414-112247-pl067542",
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-2_2-12:4.7.0"
                        }
                    }
                ],
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_order",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_SDUK\"]",
                        "partition_keys": "[\"UTC_ORDER_PLACED_MONTH_PART_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_PO_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DC_FSL_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_SUB_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_SUB_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"HAZMAT_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCRAP_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MEDICAL_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"STO_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SHIPMENT_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LATEST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_LATEST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_LATEST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_LATEST_ACTIVITY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LATEST_ACTIVITY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSACTION_TYPE_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CANCELLED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_MANAGED\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_INBOUND\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_INTERNATIONAL\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_PO_Number\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_ASN\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_BEFORE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_BEFORE_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_AFTER_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_AFTER_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_DONOT_SHIP_BEFORE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_DONOT_SHIP_AFTER_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_DONOT_SHIP_AFTER_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_DONOT_SHIP_BEFORE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"FREIGHT_CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAYBILL_AIRBILL_NUM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_FTZ\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "additional_custom_column": "[{\"name\":\"UTC_ORDER_PLACED_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_ORDER_PLACED_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
                        "tgt_table_name": "fact_order"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_order"
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-2_2-12:4.7.0"
                        }
                    }
                ],
                "job_cluster_key": "hv_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_order_line",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order_line",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order_line/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_LINE_SDUK\"]",
                        "partition_keys": "[\"UTC_ORDER_PLACED_MONTH_PART_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order_line",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DC_FSL_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_LINE_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_LINE_SUB_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_LINE_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_LINE_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_LINE_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_LINE_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_PICK_RELEASED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_PICK_RELEASED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_PICK_RELEASED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_PICKED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_PICKED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_PICKED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CREATED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CREATED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICK_RELEASED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICK_RELEASED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICKED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICKED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CANCELLED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CANCELLED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LINE_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LINE_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ORDER_LINE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SHIPPED_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CANCEL_REASON\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STD_SKU_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_5\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "additional_custom_column": "[{\"name\":\"UTC_ORDER_PLACED_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_ORDER_PLACED_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
                        "tgt_table_name": "fact_order_line"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_order_line",
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_order_reference",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
=======
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order_reference",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order_reference/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_REFERENCE_SDUK\",\"QUERY_SEQUENCE\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order_reference",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_1_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_1_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_2_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_2_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_3_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_3_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_4_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_4_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_5_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_5_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_6_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_6_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_7_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_7_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_8_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_8_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_9_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_9_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_10_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_10_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_11_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_11_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_12_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_12_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_13_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_13_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_14_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_14_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_15_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_15_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REFERENCE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"QUERY_SEQUENCE\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_order_reference"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_order_reference",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_transportation_callcheck",
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_callcheck",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_callcheck",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"CALLCHECK_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_callcheck",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SourceName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BatteryPercent\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITYTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITYID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SUMMARY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CALLCHECK_PRIORITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_REQUIRED\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CALLCHECK_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ASSIGNEDTO\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_PLANNED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PERCENTAGECOMPLETE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COMPLETE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_COMPLETE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"STATUSDETAILTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STATUSDETAIL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Latitude\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"Longitude\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"DeviceTagId\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Humidity\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Light\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"LocationMethod\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IsMotionDetected\",\"nullable\":true,\"type\":\"boolean\"},{\"metadata\":{},\"name\":\"Pressure\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"ADDRESSTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSISRESIDENTIAL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSISPRIMARY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSLOCATIONCODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSNAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSLINE1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSLINE2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STATEPROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTALCODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRYCODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLATDEGREES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLATDIRECTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLONGDEGREES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLONGDIRECTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CONTACTNAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureC\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"TemperatureF\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"IsButtonPushed\",\"nullable\":true,\"type\":\"boolean\"},{\"metadata\":{},\"name\":\"IsShockExceeded\",\"nullable\":true,\"type\":\"boolean\"},{\"metadata\":{},\"name\":\"CALLCHECK_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"IS_TEMPERATURE\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_transportation_callcheck"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_transportation_callcheck",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_transportation_rates_charges",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_customer"
<<<<<<< HEAD
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_rates_charges",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_rates_charges/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"CHARGE_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_rates_charges",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEQUENCE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RATE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RATE_QUALIFER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_LEVEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EDI_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FREIGHT_CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FAK_FREIGHT_CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CONTRACT_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CURRENCY_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INVOICE_NUMBER\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_transportation_rates_charges"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_transportation_rates_charges",
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_map_milestone_activity",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "SOURCE_SYSTEM_KEY",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_milestone_activity",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_milestone_activity/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"ActivityCode\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/map_milestone_activity",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"MilestoneId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Milestone_Completion_Flag\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SourceActivityName\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "map_milestone_activity"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_map_milestone_activity"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_account_type_digital",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "Account_ID",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/account_type_digital",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/account_type_digital/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"Account_ID\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/account_type_digital",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"Account_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Account_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Account_Name\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "account_type_digital"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_account_type_digital"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_local_courier_service",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ID",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/Local_Courier_Service",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/local_courier_service",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"ID\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/local_courier_service",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SERVICE_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIERNAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICELEVELNAME\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "local_courier_service"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_local_courier_service"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_map_ordersearchstatus",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "SOURCE_SYSTEM_KEY",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_ordersearchstatus",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_ordersearchstatus/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"OrderStatusCode\",\"SOURCE_SYSTEM_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/map_ordersearchstatus",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SourceSystemName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"OrderStatusName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"OrderStatusCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "map_orderSearchStatus"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_map_ordersearchstatus"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_map_transactiontype_milestone",
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "TransactionTypeId",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_transactiontype_milestone",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_transactiontype_milestone",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[ \"TransactionTypeId\",\"MilestoneOrder\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/map_transactiontype_milestone",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"TransactionTypeId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TransactionTypeName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneOrder\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Is_Managed\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Is_Inbound\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Is_International\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_FTZ\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "map_transactiontype_milestone"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_map_transactiontype_milestone",
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_transport_details",
                "depends_on": [
                    {
                        "task_key": "silver_dim_customer"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transport_details",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transport_details/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"SHIPMENT_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transport_details",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_ASN\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEQUENCE\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"CONTAINED_IN\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_HAZMAT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDERED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ORDERED_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PLANNED_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTUAL_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ACTUAL_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_WGT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTUAL_WGT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DIMENSION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COMMODITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DELIVERY_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"TemperatureRange_Min\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Max\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Code\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Planned_Weight_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Actual_Weight_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Dimension_UOM\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_transport_details"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_transport_details",
                "depends_on": [
                    {
                        "task_key": "silver_dim_customer"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_milestone_activity",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_milestone_activity",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_milestone_activity/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"LOAD_TRACK_SDUK\"]",
                        "partition_keys": "[\"ACTIVITY_MONTH_PART_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_milestone_activity",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRACKING_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACTIVITY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTIVITY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTIVITY_COMPLETION_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_PLANNED_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PLANNED_MILESTONE_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"PLANNED_MILESTONE_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"MILESTONE_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MILESTONE_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MILESTONE_COMPLETION_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_TRACK_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_WMS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_ASN\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEGMENT_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTIVITY_NOTES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FTZ_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOGI_NEXT_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_WMS_SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_DATE_TIME\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LATITUDE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LONGITUDE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_LOCATION\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "additional_custom_column": "[{\"name\":\"ACTIVITY_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(ACTIVITY_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
                        "tgt_table_name": "fact_milestone_activity"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_milestone_activity"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_shipment",
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_shipment",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_shipment/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"SHIPMENT_SDUK\"]",
                        "partition_keys": "[\"UTC_SHIPMENT_CREATION_MONTH_PART_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_shipment",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHIPMENT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_SEQUENCE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRACKING_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_SHIPMENT_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_SHIPMENT_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SHIPMENT_CREATION_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHIPMENT_CREATION_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHIPMENT_LENGTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CUBAGE\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"TemperatureRange_Min\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Max\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Code\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Actual_Weight_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Dimension_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_AREA\",\"nullable\":true,\"type\":\"decimal(38,6)\"},{\"metadata\":{},\"name\":\"UOM\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "additional_custom_column": "[{\"name\":\"UTC_SHIPMENT_CREATION_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_SHIPMENT_CREATION_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
                        "tgt_table_name": "fact_shipment"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_shipment",
                "depends_on": [
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_order_line_details",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order_line_details",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order_line_details/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_LINE_DETAILS_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order_line_details",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_DETAIL_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_SERIAL_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_LOT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LPN_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DISPOSITION_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_LINE_DETAILS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_LINE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_INBOUND\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHELF_LIFE\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PRODUCT_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STORAGE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UTC_EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"HOLD_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RECEIPT_NUMBER\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_order_line_details"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_order_line_details"
            },
            {
                "existing_cluster_id": "0414-112247-pl067542",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_fact_order_dim",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_fact_order_dim_inc",
                "depends_on": [
                    {
                        "task_key": "silver_account_type_digital"
                    },
                    {
                        "task_key": "silver_map_ordersearchstatus"
                    },
                    {
                        "task_key": "silver_dim_geo_location"
                    },
                    {
                        "task_key": "silver_local_courier_service"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_fact_order"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    },
                    {
                        "task_key": "silver_dim_service"
                    },
                    {
                        "task_key": "silver_fact_order_deletes"
                    },
                    {
                        "task_key": "silver_dim_source_system"
                    },
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_map_milestone_activity"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112247-pl067542",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_milestone_activity",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_fact_order_dim",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "hv_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_milestone_activity",
                "depends_on": [
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "silver_fact_transport_details"
                    },
                    {
                        "task_key": "silver_fact_milestone_activity"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_callcheck",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_milestone_activity",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "hv_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_transportation_callcheck",
                "depends_on": [
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "silver_fact_transportation_callcheck"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112247-pl067542",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_orders",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_callcheck",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_orders",
                "depends_on": [
                    {
                        "task_key": "silver_fact_order_line"
                    },
                    {
                        "task_key": "silver_fact_transportation_exception"
                    },
                    {
                        "task_key": "gold_digital_summary_milestone_activity"
                    },
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    },
                    {
                        "task_key": "silver_map_temperature_range_details"
                    },
                    {
                        "task_key": "silver_fact_order_reference"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112247-pl067542",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_orders_Container",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_orders",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "hv_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_digital_summary_orders",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_transportation_references"
                    },
                    {
                        "task_key": "gold_digital_summary_exceptions"
                    },
                    {
                        "task_key": "gold_digital_summary_order_tracking"
                    },
                    {
                        "task_key": "gold_digital_summary_transportation_callcheck"
                    },
                    {
                        "task_key": "gold_digital_summary_orders"
                    },
                    {
                        "task_key": "gold_digital_summary_transportation_rates_charges"
                    },
                    {
                        "task_key": "gold_digital_summary_order_lines"
                    },
                    {
                        "task_key": "gold_digital_summary_order_lines_details"
                    },
                    {
                        "task_key": "gold_digital_summary_transportation"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_exceptions",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_orders_Container",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "hv_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_exceptions",
                "depends_on": [
                    {
                        "task_key": "silver_fact_transportation_exception"
                    },
                    {
                        "task_key": "silver_map_milestone_activity"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_inbound_line"
                },
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_exceptions",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_inbound_line",
                "depends_on": [
                    {
                        "task_key": "silver_fact_inbound_line"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_fact_transport_details"
                    },
                    {
                        "task_key": "silver_dim_item"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_inbound_line"
                },
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_inbound_line",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "Y",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_inbound_line",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_inbound_line/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"INBOUND_LINE_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_inbound_line",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ASN_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ASN_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PO_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PO_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RCPT_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RCPT_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_HEADER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_HEADER_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INBND_CARRIER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INBND_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_INBND_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_INBND_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INBND_LINE_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_INBND_LINE_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_INBND_LINE_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INBND_HDR_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_INBND_HDR_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_INBND_HDR_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"IL_FIRST_RCVD_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_IL_FIRST_RCVD_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_IL_FIRST_RCVD_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"IL_LAST_PUTAWAY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_IL_LAST_PUTAWAY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_IL_LAST_PUTAWAY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INBND_LINE_SHIPPED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"INBND_LINE_RECEIVED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"INBOUND_LINE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"INBND_HDR_CREATION_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_HDR_CREATION_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_LINE_CREATION_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_LINE_CREATION_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_HDR_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_HDR_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_FIRST_RCVD_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_FIRST_RCVD_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_LAST_PUTAWAY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_LAST_PUTAWAY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_PO_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_PO_SUB_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INBND_LINE_RECEIVED_CASES\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_10\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_11\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_5\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CASES\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_inbound_line"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_inbound_line",
                "depends_on": [
                    {
                        "task_key": "silver_dim_geo_location"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_milestone",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_milestone",
                "depends_on": [
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "silver_map_transactiontype_milestone"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_order_lines",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_milestone",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_order_lines",
                "depends_on": [
                    {
                        "task_key": "silver_fact_order_line"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_dim_item"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_order_lines_details",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_order_lines",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_order_lines_details",
                "depends_on": [
                    {
                        "task_key": "silver_fact_order_line_details"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_dim_item"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_order_tracking",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_order_lines_details",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_order_tracking",
                "depends_on": [
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "silver_fact_shipment"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_order_tracking",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_transportation",
                "depends_on": [
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    },
                    {
                        "task_key": "silver_fact_transportation"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_details",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_transportation_details",
                "depends_on": [
                    {
                        "task_key": "silver_fact_transport_details"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_rates_charges",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_details",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_transportation_rates_charges",
                "depends_on": [
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "silver_fact_transportation_rates_charges"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_references",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_rates_charges",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "gold_digital_summary_transportation_references",
                "depends_on": [
                    {
                        "task_key": "silver_fact_order_reference"
                    },
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "gold_fact_order_dim_inc"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_order_lines_Container",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_transportation_references",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_digital_summary_order_lines",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_orders"
                    },
                    {
                        "task_key": "gold_digital_summary_inbound_line"
                    },
                    {
                        "task_key": "gold_digital_summary_order_lines"
                    },
                    {
                        "task_key": "gold_digital_summary_order_lines_details"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_milestone_activity_Container",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_order_lines_Container",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_digital_summary_orders_milestone_activity",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_orders"
                    },
                    {
                        "task_key": "gold_digital_summary_milestone_activity"
                    },
                    {
                        "task_key": "silver_map_transactiontype_milestone"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_transportation_callcheck_Container",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_milestone_activity_Container",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_digital_summary_transportation_callcheck",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_orders"
                    },
                    {
                        "task_key": "gold_digital_summary_transportation_callcheck"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112642-msjnoslr",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_transport_details_Container",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_transportation_callcheck_Container",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_digital_summary_transport_details",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_transportation_details"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_transportation_rates_charges_Container",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_transport_details_Container",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "g_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_digital_summary_transportation_rates_charges",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_orders"
                    },
                    {
                        "task_key": "gold_digital_summary_transportation_rates_charges"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ActivityCode",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/wh_wip_mapping_activity",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/wh_wip_mapping_activity/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"ActivityCode\",\"SOURCE_SYSTEM_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/wh_wip_mapping_activity",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"Type\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WIP_ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"WIPActivityOrderId\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "wh_wip_mapping_activity"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_transportation_rates_charges_Container",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "silver_wh_wip_mapping_activity",
                "depends_on": [
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_source_system"
                    },
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112247-pl067542",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ActivityCode",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/wh_wip_mapping_activity",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/wh_wip_mapping_activity/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"ActivityCode\",\"SOURCE_SYSTEM_KEY\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/wh_wip_mapping_activity",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"Type\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WIP_ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"WIPActivityOrderId\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "wh_wip_mapping_activity"
                    }
                },
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_fact_order_deletes",
                "depends_on": [
                    {
                        "task_key": "silver_fact_order"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_deletes_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "DELETETIMESTAMP",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/splus_src_deletes",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/splus_src_deletes",
                        "hash_exclude_columns": "",
                        "primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"ORDER_SDUK\"]",
                        "partition_keys": "",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"ORDER_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"ORIGIN_CONTACT_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"ACCOUNT_USER_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"DEST_CONTACT_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"ORDER_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PKG_AVAILABLE_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"USER_REFERENCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"QUOTED_PRICE\",\"nullable\":true,\"type\":\"double\"},{\"metadata\":{},\"name\":\"QUOTED_DELIV_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PROOF_DELIVERY_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SIGNATURE_REQUIRED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CANCELLED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"DOCUMENT_AUTHENTICATION_NO\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ASSIGNED_TO\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_TIME_ZONE_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DEST_TIME_ZONE_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CREDIT_CARD_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"AUTO_DISPATCH_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CARGO_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"ORDER_COMPLETION_TIME\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ALT_ORDER_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEC_ORDER_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_DELIVERY_INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DEST_DELIVERY_INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_STATE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CURRENT_SEGMENT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SERVICE_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACCOUNT_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CONSIGNEE_ONLY_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CURRENT_LOCATION_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MANAGING_BRANCH_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SOURCE_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_DELIVERY_DEPT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTUAL_PACKAGES_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"REQUESTED_DELIVERY_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXPORTED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_FLFILMNT_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BACK_ORDER_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXPORTED_BATCH_NM\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLOSEST_WHSE_ENABLED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"TAKEN_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DELIVER_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVE_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"DISPATCHED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DISPATCHED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLOSED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"CLOSED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VERSION\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CREATED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CREATED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LAST_UPDATED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LAST_UPDATED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"FINALIZED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FINALIZED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"WEIGHT_UOM_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DIMENSION_UOM_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FA_EXTRACT_BATCH_NM\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"FA_EXTRACT_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"CREATION_START_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"WAREHOUSE_PICKUP_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"POD_DETAILS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_SUBTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INTEGRATION_SERVICE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CANCELLED_AT_OC_STATE_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"BILLING_WEIGHT\",\"nullable\":true,\"type\":\"decimal(11,2)\"},{\"metadata\":{},\"name\":\"BILLING_PICKUP_MILEAGE\",\"nullable\":true,\"type\":\"decimal(11,2)\"},{\"metadata\":{},\"name\":\"BILLING_DROPOFF_MILEAGE\",\"nullable\":true,\"type\":\"decimal(11,2)\"},{\"metadata\":{},\"name\":\"KSMS_STATUS_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPPER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INVENTORY_ACCOUNT_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"FUTURE_PLACEMENT_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"BACK_ORDER_PRIORITY_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"REQ_FUTURE_PLACEMENT_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACCESS_POINT_PKG_RELEASE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"OMS_BATCH_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ROUTING_BRD_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_DEPT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_DETAILS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PRIORITY_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_ALTERED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"INVENTORY_ORDER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_PO_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDITIONAL_ORDER_IDENTIFIER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPPING_PRIORITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INTERNATIONAL_ORDER_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"INVOICE_REQUIRED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"COUNTRY_OF_CONSIGNMENT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BILL_OF_LADING\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BATCH_PICK_ALLOWED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"ORDER_HANDLING_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CONSOLIDATION_ALLOWED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CONTAINER_QTY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CONTAINER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHEPPALLET_INDICATOR\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_ORDER_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"PROGRESSIVE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BILLED_CONTAINER_QTY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_MODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORGANIZATION_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IOR_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POD_ON_HOLD\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"DELETETIMESTAMP\",\"nullable\":true,\"type\":\"timestamp\"}],\"type\":\"struct\"}",
                        "additional_custom_column": "[{\"name\":\"SOURCE_SYSTEM_KEY\",\"value\":\"cast('1002' as bigint)\"},{\"name\":\"ORDER_SDUK\",\"value\":\"cast(ORDER_ID as string)\"}]",
                        "tgt_table_name": "splus_src_deletes"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_order_deletes",
                "depends_on": [
                    {
                        "task_key": "silver_fact_order"
                    }
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_references",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_references/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"REFERENCE_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_references",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPUNIT_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFRENCE_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_LEVEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_transportation_references"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                "job_cluster_key": "hv_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "silver_fact_transportation_references",
                "depends_on": [
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_source_system"
                    },
                    {
                        "task_key": "silver_dim_warehouse"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_dim_warehouse_Container",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "ETL_UPDATE_DATE",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_references",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_references/",
                        "hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
                        "primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"REFERENCE_SDUK\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_references",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPUNIT_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFRENCE_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_LEVEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_transportation_references"
                    }
                },
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "task_key": "cosmos_dim_warehouse",
                "depends_on": [
                    {
                        "task_key": "silver_fact_transportation"
                    },
                    {
                        "task_key": "silver_dim_customer"
                    },
                    {
                        "task_key": "silver_dim_carrier_los"
                    },
                    {
                        "task_key": "silver_dim_source_system"
                    },
                    {
                        "task_key": "silver_dim_warehouse"
                    }
<<<<<<< HEAD
                ]
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_dim_warehouse_Container",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "silver_map_temperature_range_details",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "sort_values": "CarrierCode",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_temperature_range_details",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_temperature_range_details/",
                        "hash_exclude_columns": "[]",
                        "primary_keys": "[\"CarrierCode\",\"LevelOfService\"]",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/map_temperature_range_details/",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"CarrierCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LevelOfService\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureThreshold\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Min\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Max\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "map_temperature_range_details"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_map_temperature_range_details"
            },
            {
                "existing_cluster_id": "0414-112418-kc2c53vk",
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "cosmos_digital_summary_orders_agg",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_orders"
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_orders_agg_Container",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
<<<<<<< HEAD
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "cosmos_digital_summary_orders_agg",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_orders"
                    }
                ]
            }
        ]
    }
=======
                "job_cluster_key": "s_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "s_job_pool_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.1.x-scala2.12",
                    "instance_pool_id": "0404-073311-bayou3-pool-qufaqheo",
                    "driver_instance_pool_id": "0404-073216-bosh2-pool-b4f84jog",
                    "runtime_engine": "STANDARD",
                    "num_workers": 4
                }
            },
            {
                "job_cluster_key": "g_job_pool_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.1.x-scala2.12",
                    "instance_pool_id": "0404-073216-bosh2-pool-b4f84jog",
                    "driver_instance_pool_id": "0404-073216-bosh2-pool-b4f84jog",
                    "runtime_engine": "STANDARD",
                    "num_workers": 8
                }
            },
            {
                "job_cluster_key": "hv_job_pool_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.1.x-scala2.12",
                    "instance_pool_id": "0404-073418-notch4-pool-d695men4",
                    "driver_instance_pool_id": "0404-073216-bosh2-pool-b4f84jog",
                    "runtime_engine": "STANDARD",
                    "num_workers": 8
                }
            },
            {
                "job_cluster_key": "s_job_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.4.x-scala2.12",
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "node_type_id": "Standard_F32s_v2",
                    "driver_node_type_id": "Standard_E8ds_v4",
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": true,
                    "azure_attributes": {
                        "first_on_demand": 1,
                        "availability": "ON_DEMAND_AZURE",
                        "spot_bid_max_price": -1
                    },
                    "autoscale": {
                        "min_workers": 5,
                        "max_workers": 8
                    }
                }
            },
            {
                "job_cluster_key": "g_job_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.4.x-scala2.12",
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "node_type_id": "Standard_E8ds_v4",
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": true,
                    "azure_attributes": {
                        "first_on_demand": 1,
                        "availability": "ON_DEMAND_AZURE",
                        "spot_bid_max_price": -1
                    },
                    "autoscale": {
                        "min_workers": 5,
                        "max_workers": 8
                    }
                }
            },
            {
                "job_cluster_key": "hv_job_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.4.x-scala2.12",
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "node_type_id": "Standard_E16ds_v4",
                    "driver_node_type_id": "Standard_E8ds_v4",
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": true,
                    "azure_attributes": {
                        "first_on_demand": 1,
                        "availability": "ON_DEMAND_AZURE",
                        "spot_bid_max_price": -1
                    },
                    "autoscale": {
                        "min_workers": 5,
                        "max_workers": 8
                    }
                }
            }
        ],
        "format": "MULTI_TASK"
   
}
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
"""

# COMMAND ----------

<<<<<<< HEAD
requests.post(endpoint, data=data_sail_load, headers=headers).json()
=======
requests.post(endpoint, data=data, headers=headers).json()
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3

# COMMAND ----------

data_inventory = r"""
{
<<<<<<< HEAD
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "sail_inventory_load",
        "schedule": {
            "quartz_cron_expression": "36 45 0/12 * * ?",
            "timezone_id": "UTC",
            "pause_status": "PAUSED"
        },
=======
    
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "sail_inventory_load",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "job_cluster_key": "silver_fact_inventory_snapshot_cluster",
                "libraries": [
                    {
<<<<<<< HEAD
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    },
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-2_2-12:4.7.0"
=======
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                        }
                    }
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/silver/autoloader_fact_inventory_transform_bronze_to_silver",
                    "base_parameters": {
                        "log_debug_mode": "N",
                        "checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_inventory_snapshot/",
                        "src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_inventory_snapshot/",
                        "target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_inventory_snapshot",
                        "src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"LPN_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DISPOSITION_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERIAL_OR_LOT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LPN_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_LPN_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_LPN_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"RECEIVED_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ON_HAND_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ON_HOLD_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ALLOCATED_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"AVAILABLE_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"UNALLOCATABLE_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PRN_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"QUARANTINE_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"POTENTIAL_VARIANCE_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"GOOD_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"NEW_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"INVENTORY_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"AVAILABLE_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESIGNATOR\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_SERIAL_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_LOT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INV_REF_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INV_REF_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INV_REF_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INV_REF_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INV_REF_5\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HOLD_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PRODUCT_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BATCH_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHELF_LIFE\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"STORAGE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BATCH_HOLD_REASON\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HOLD_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"NET_AVAILABLE_UNITS\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
                        "tgt_table_name": "fact_inventory_snapshot"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "silver_fact_inventory_snapshot"
            },
            {
                "job_cluster_key": "silver_fact_inventory_snapshot_cluster",
                "notebook_task": {
                    "notebook_path": "/SAIL/gold/pr_load_summary_inventory",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "gold_digital_summary_inventory",
                "depends_on": [
                    {
                        "task_key": "silver_fact_inventory_snapshot"
                    }
                ]
            },
            {
                "job_cluster_key": "silver_fact_inventory_snapshot_cluster",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_inventory_Container",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "cosmos_digital_inventory_snapshot",
                "depends_on": [
                    {
                        "task_key": "gold_digital_summary_inventory"
                    }
                ]
<<<<<<< HEAD
            },
            {
                "job_cluster_key": "silver_fact_inventory_snapshot_cluster",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/load_digital_summary_inventory_agg_Container",
                    "base_parameters": {
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "load_digital_summary_inventory_agg_Container",
                "depends_on": [
                    {
                        "task_key": "cosmos_digital_inventory_snapshot"
                    }
                ]
=======
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "silver_fact_inventory_snapshot_cluster",
                "new_cluster": {
                    "cluster_name": "",
<<<<<<< HEAD
                    "spark_version": "10.3.x-scala2.12",
=======
                    "spark_version": "9.1.x-scala2.12",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "azure_attributes": {
                        "availability": "ON_DEMAND_AZURE",
                        "first_on_demand": 1,
                        "spot_bid_max_price": -1
                    },
                    "node_type_id": "Standard_E16ds_v4",
                    "driver_node_type_id": "Standard_F8",
<<<<<<< HEAD
=======
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "enable_elastic_disk": true,
                    "num_workers": 4
                }
            }
        ]
<<<<<<< HEAD
    }
=======
    
}
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
"""

# COMMAND ----------

requests.post(endpoint, data=data_inventory, headers=headers).json()

# COMMAND ----------

data_cosmos_delete = r"""
{
<<<<<<< HEAD
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "sail_cosmos_delete",
        "schedule": {
            "quartz_cron_expression": "32 0 5 * * ?",
            "timezone_id": "Asia/Kolkata",
            "pause_status": "PAUSED"
        },
=======
    
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "sail_cosmos_delete",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
<<<<<<< HEAD
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_orders",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "DateTimeReceived",
                        "partition_key": "AccountId",
                        "days_back_to_del": "100"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_orders",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_order_lines"
                    }
                ]
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
                "libraries": [
                    {
<<<<<<< HEAD
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    },
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-2_2-12:4.7.0"
=======
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    }
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_inventory",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "NA",
                        "partition_key": "AccountId",
                        "days_back_to_del": "365"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_inventory",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_milestone_activity"
                    }
                ]
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                        }
                    }
                ],
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_milestone_activity",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "ActivityDate",
                        "partition_key": "UpsOrderNumber",
                        "days_back_to_del": "100"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_milestone_activity"
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
<<<<<<< HEAD
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_order_lines",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "SummaryDateTimeReceived",
                        "partition_key": "UpsOrderNumber",
                        "days_back_to_del": "100"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_order_lines",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_inventory"
                    }
                ]
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
<<<<<<< HEAD
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_transport_details",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "NA",
                        "partition_key": "UpsOrderNumber",
                        "days_back_to_del": "365"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_transport_details",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_orders"
                    }
                ]
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
<<<<<<< HEAD
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_transportation_callcheck",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "TemperatureDateTime",
                        "partition_key": "UPSOrderNumber",
                        "days_back_to_del": "100"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_transportation_callcheck",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_transport_details"
                    }
                ]
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
<<<<<<< HEAD
=======
                "libraries": [
                    {
                        "maven": {
                            "coordinates": "com.azure.cosmos.spark:azure-cosmos-spark_3-1_2-12:4.5.1"
                        }
                    },
                    {
                        "pypi": {
                            "package": "azure-cosmos==4.2.0"
                        }
                    }
                ],
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_transportation_rates_charges",
                        "other_del_cond": "1=2",
                        "date_column": "invoiceDateTime",
                        "partition_key": "UpsOrderNumber",
                        "days_back_to_del": "100"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_transportation_rates_charges",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_transportation_callcheck"
                    }
                ]
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/sail_vacuum"
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "sail_vacuum"
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/sail analyze"
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "sail_analyze",
                "depends_on": [
                    {
                        "task_key": "sail_vacuum"
                    }
                ]
<<<<<<< HEAD
            },
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
                "notebook_task": {
                    "notebook_path": "/SAIL/cosmos/delete_cosmos_documents",
                    "base_parameters": {
                        "cosmos_database_name": "SAIL",
                        "log_debug_mode": "N",
                        "cosmos_container_name": "digital_summary_inventory",
                        "other_del_cond": "c.is_deleted = 1",
                        "date_column": "NA",
                        "partition_key": "AccountId",
                        "days_back_to_del": "365"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "del_digital_summary_inventory",
                "depends_on": [
                    {
                        "task_key": "del_digital_summary_milestone_activity"
                    }
                ]
=======
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "cosmos_delete_jobcluster",
                "new_cluster": {
                    "cluster_name": "",
<<<<<<< HEAD
                    "spark_version": "10.2.x-scala2.12",
=======
                    "spark_version": "10.1.x-scala2.12",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "azure_attributes": {
                        "availability": "ON_DEMAND_AZURE",
                        "first_on_demand": 1,
                        "spot_bid_max_price": -1
                    },
                    "node_type_id": "Standard_F16",
                    "driver_node_type_id": "Standard_F8",
                    "enable_elastic_disk": true,
                    "num_workers": 6
                }
            }
        ]
<<<<<<< HEAD
    }
=======
    
}
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
"""

# COMMAND ----------

requests.post(endpoint, data=data_cosmos_delete, headers=headers).json()

# COMMAND ----------

data_optimize = r"""
{
<<<<<<< HEAD
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "optimize_sail_load",
        "schedule": {
            "quartz_cron_expression": "33 45 3/4 * * ?",
            "timezone_id": "UTC",
            "pause_status": "PAUSED"
        },
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "job_cluster_key": "hv_job_cluster",
=======
    
        "timeout_seconds": 0,
        "email_notifications": {},
        "name": "optimize_sail_load",
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_milestone_activity",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_milestone_activity",
                "description": ""
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_order",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_order"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_shipment",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_shipment"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_order_line_details",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_order_line_details"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_transportation",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_transportation"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_transportation_exception",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_transportation_exception"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_order_reference",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_order_reference"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_order_line",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_order_line"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_inbound_line",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_inbound_line"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_transportation_callcheck",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_transportation_callcheck"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_transportation_rates_charges",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_transportation_rates_charges"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_transportation_references",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_transportation_references"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_transport_details",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_transport_details"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "dim_customer",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "dim_customer"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "dim_warehouse",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "dim_warehouse"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "dim_item",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "dim_item"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "dim_carrier_los",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "dim_carrier_los"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "dim_service",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "dim_service"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "dim_geo_location",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "dim_geo_location"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "fact_order_dim_inc",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "fact_order_dim_inc"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_order_lines",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_order_lines"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_milestone",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_milestone"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_transport_details",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_transport_details"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_milestone_activity",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_milestone_activity"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_transportation_callcheck",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_transportation_callcheck"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_transportation_references",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_transportation_references"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_transportation_rates_charges",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_transportation_rates_charges"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "s_job_cluster",
=======
                "existing_cluster_id": "0301-051519-b7nxfnfn",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_order_tracking",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_order_tracking"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_orders",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_orders"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "hv_job_cluster",
=======
                "existing_cluster_id": "0301-051816-jv2btm8l",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_transportation",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_transportation"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_order_lines_details",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_order_lines_details"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_exceptions",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_exceptions"
            },
            {
<<<<<<< HEAD
                "job_cluster_key": "g_job_cluster",
=======
                "existing_cluster_id": "0301-051624-cl37tr9d",
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
                "notebook_task": {
                    "notebook_path": "/SAIL/includes/optimize/optimize",
                    "base_parameters": {
                        "table_name": "digital_summary_inbound_line",
                        "log_debug_mode": "N"
                    }
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "task_key": "digital_summary_inbound_line"
            }
<<<<<<< HEAD
        ],
        "job_clusters": [
            {
                "job_cluster_key": "hv_job_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.1.x-scala2.12",
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "azure_attributes": {
                        "availability": "ON_DEMAND_AZURE",
                        "first_on_demand": 1,
                        "spot_bid_max_price": -1
                    },
                    "node_type_id": "Standard_E16ds_v4",
                    "driver_node_type_id": "Standard_E8d_v4",
                    "enable_elastic_disk": true,
                    "num_workers": 8
                }
            },
            {
                "job_cluster_key": "s_job_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.1.x-scala2.12",
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "azure_attributes": {
                        "availability": "ON_DEMAND_AZURE",
                        "first_on_demand": 1,
                        "spot_bid_max_price": -1
                    },
                    "node_type_id": "Standard_F32s_v2",
                    "driver_node_type_id": "Standard_E8ds_v4",
                    "enable_elastic_disk": true,
                    "num_workers": 4
                }
            },
            {
                "job_cluster_key": "g_job_cluster",
                "new_cluster": {
                    "cluster_name": "",
                    "spark_version": "10.1.x-scala2.12",
                    "spark_conf": {
                        "spark.databricks.delta.preview.enabled": "true"
                    },
                    "azure_attributes": {
                        "availability": "ON_DEMAND_AZURE",
                        "first_on_demand": 1,
                        "spot_bid_max_price": -1
                    },
                    "node_type_id": "Standard_E8ds_v4",
                    "driver_node_type_id": "Standard_E8ds_v4",
                    "enable_elastic_disk": true,
                    "num_workers": 8
                }
            }
        ]
    }
=======
        ]
    
}
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
"""

# COMMAND ----------

<<<<<<< HEAD
requests.post(endpoint, data=data_optimize, headers=headers).json()
=======
data_sail_v2 = r'''
{
	"settings": {
		"timeout_seconds": 0,
		"email_notifications": {},
		"name": "sail_load_v2",
		"max_concurrent_runs": 1,
		"tasks": [
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "Y",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_customer",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_customer/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"CUSTOMER_ACCOUNT_SDUK\", \"CUSTOMERKEY\" ]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_customer",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INT_CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INT_CUSTOMER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DIVISION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXT_CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ACCOUNT_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACCOUNT_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTAL_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ACCOUNT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GLD_ACCOUNT_MAPPED_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ENABLE_CARRIER_UPDATE_FLAG\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CUSTOMERKEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DP_SERVICELINE_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DP_ORGENTITY_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MAPPED_WAREHOUSE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_HUB_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_customer"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_customer"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_warehouse",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_warehouse/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[\"WAREHOUSE_KEY\" ,\"SOURCE_SYSTEM_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_warehouse",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"WAREHOUSE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BUILDING_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTAL_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GLD_WAREHOUSE_MAPPED_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_warehouse"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_warehouse"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "SOURCE_SYSTEM_KEY",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_source_system",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_source_system/",
						"hash_exclude_columns": "[]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_source_system",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_GROUP\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DC_FSL_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_source_system"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_source_system"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_carrier_los",
						"src_folder_path": " /mnt/sail/bronze/gld360/inbound/landing/dim_carrier_los/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[\"CARRIER_LOS_KEY\",\"SOURCE_SYSTEM_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_carrier_los",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_DESC\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_NUMERIC_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"EXT_CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_GROUP\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GLD_CARRIER_MAPPED_KEY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_HUB_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_carrier_los"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_carrier_los"
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"TRANSPORTATION_SDUK\"]",
						"partition_keys": "[\"UTC_ORDER_PLACED_MONTH_PART_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"PICKUP_CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DROPOFF_CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EQUIPMENT_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_SUB_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_COMPANY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_COMPANY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_STATE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SCHEDULED_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_SCHEDULED_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_SCHEDULED_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACTUAL_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ACTUAL_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ACTUAL_SHIPMENT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACTUAL_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ACTUAL_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ACTUAL_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_SHIPMENT_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_SHIPMENT_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_SHIPMENT_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_SHIPMENT_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_DELIVERY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCHEDULED_DELIVERY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_DELIVERY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTUAL_DELIVERY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PICKUP_CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DROPOFF_CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_WMS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_WMS_SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORIGINAL_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORIGINAL_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORIGINAL_SCHEDULED_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORIGINAL_SCHEDULED_DELIVERY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORIGINAL_SCHEDULED_DELIVERY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_EARLIEST_PICKUP_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_LATEST_PICKUP_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_EARLIEST_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_LATEST_DELIVERY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOAD_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_1\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_1\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_1\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_1_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_1_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_2\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_2\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_2\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_2_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_2_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_3\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_3\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_3\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_3_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_3_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_4\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_4\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_4\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_4_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_4_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_5\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_5\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_5\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_5\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_5_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_5_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONE_6\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_6\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_TRANSPORT_MILESTONEDATE_6\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_TRANSPORT_MILESTONEDATE_6\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_6_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORT_MILESTONEDATE_6_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WMS_PO_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_MODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANS_ONLY_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_NOTES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COMMENTS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GFF_SHIPMENT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GFF_SHIPMENT_INSTANCE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SCOPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SECTOR\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DIRECTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"AUTHORIZER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DELIVERY_INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_CONTACT\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"additional_custom_column": "[{\"name\":\"UTC_ORDER_PLACED_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_ORDER_PLACED_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
						"tgt_table_name": "fact_transportation"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_transportation",
				"depends_on": [
					{
						"task_key": "silver_dim_geo_location"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_exception",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_exception",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"TRANSPORTATION_EXCEPTION_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_exception",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UTC_EXCEPTION_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXCEPTION_CREATED_DATE_OTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXCEPTION_CREATED_DATE_OTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXCEPTION_CREATED_DATE_DTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXCEPTION_CREATED_DATE_DTZ\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXCEPTION_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_EVENT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_REASON\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_REASON_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_CATEGORY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RESPONSIBLE_PARTY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXCEPTION_PRIMARY_INDICATOR\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"EXCEPTION_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_EXCEPTION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_WMS_SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_WMS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_transportation_exception"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_transportation_exception",
				"depends_on": [
					{
						"task_key": "silver_dim_carrier_los"
					},
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_dim_geo_location"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_item",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_item/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[\"ITEM_KEY\",\"SOURCE_SYSTEM_KEY\",\"ITEM_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_item",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ITEM_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PART_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PART_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PRIMARY_CUSTOMER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DIMENSIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DIMENSIONS_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_LENGTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_WEIGHT_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_PRICE\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ITEM_PRICE_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERIAL_OR_LOT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HARMONIZED_TARIFF_SCHEDULE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UN_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVE_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STD_SKU_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STD_CASE_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CASE_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CASE_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CASE_DEPTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CASE_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"STD_PALLET_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PALLET_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PALLET_DEPTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PALLET_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PALLET_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"UNIT_PER_CASE\",\"nullable\":true,\"type\":\"decimal(22,0)\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ETL_OPS_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SKU_GRP11\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SKU_GRP1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STRATEGICGOODS_FLAG\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_item"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_item",
				"depends_on": [
					{
						"task_key": "silver_dim_geo_location"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_service",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_service/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"SERVICE_KEY\", \"SERVICE_SDUK\" ]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_service",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"E2K_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"E2K_CHARGE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_NOT_REQUIRED\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_service"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_service"
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/dim_geo_location",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/dim_geo_location/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[\"GEO_LOCATION_KEY\",\"SOURCE_SYSTEM_KEY\",\"GEO_LOCATION_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/dim_geo_location",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"GEO_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"LOCATION_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESS_LINE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTAL_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOCATION_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEO_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
						"tgt_table_name": "dim_geo_location"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_dim_geo_location"
			},
			{
				"existing_cluster_id": "0301-051816-jv2btm8l",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_SDUK\"]",
						"partition_keys": "[\"UTC_ORDER_PLACED_MONTH_PART_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_PO_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DC_FSL_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_SUB_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_SUB_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"HAZMAT_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SCRAP_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MEDICAL_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"STO_ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORDER_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_REC_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SHIPMENT_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LATEST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_LATEST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_LATEST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_LATEST_ACTIVITY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LATEST_ACTIVITY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TRANSACTION_TYPE_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CANCELLED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_MANAGED\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_INBOUND\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_INTERNATIONAL\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_PO_Number\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_ASN\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_BEFORE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_BEFORE_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_AFTER_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DONOT_SHIP_AFTER_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_RECEIVED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_DONOT_SHIP_BEFORE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_DONOT_SHIP_AFTER_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_DONOT_SHIP_AFTER_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_DONOT_SHIP_BEFORE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"FREIGHT_CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAYBILL_AIRBILL_NUM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_FTZ\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
						"additional_custom_column": "[{\"name\":\"UTC_ORDER_PLACED_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_ORDER_PLACED_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
						"tgt_table_name": "fact_order"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_order"
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order_line",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order_line/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_LINE_SDUK\"]",
						"partition_keys": "[\"UTC_ORDER_PLACED_MONTH_PART_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order_line",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SERVICE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DC_FSL_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_LINE_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_ORDER_LINE_SUB_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_LINE_CANCELLED_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_PLACED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_LINE_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ORDER_LINE_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ORDER_LINE_CREATED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_PICK_RELEASED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_PICK_RELEASED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_PICK_RELEASED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_PICKED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_PICKED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_PICKED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"OL_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_OL_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_OL_CANCELLED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_PLACED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CREATED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CREATED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICK_RELEASED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICK_RELEASED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICKED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_PICKED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CANCELLED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"OL_CANCELLED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LINE_COUNT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_LINE_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ORDER_LINE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SHIPPED_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"CANCEL_REASON\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STD_SKU_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_REF_VALUE_5\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"additional_custom_column": "[{\"name\":\"UTC_ORDER_PLACED_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_ORDER_PLACED_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
						"tgt_table_name": "fact_order_line"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_order_line",
				"depends_on": [
					{
						"task_key": "silver_dim_geo_location"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order_reference",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order_reference/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_REFERENCE_SDUK\",\"QUERY_SEQUENCE\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order_reference",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_1_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_1_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_2_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_2_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_3_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_3_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_4_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_4_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_5_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_5_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_6_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_6_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_7_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_7_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_8_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_8_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_9_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_9_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_10_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_10_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_11_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_11_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_12_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_12_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_13_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_13_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_14_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_14_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_15_LABEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REF_15_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_REFERENCE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"QUERY_SEQUENCE\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_order_reference"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_order_reference",
				"depends_on": [
					{
						"task_key": "silver_dim_geo_location"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_callcheck",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_callcheck",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"CALLCHECK_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_callcheck",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SourceName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BatteryPercent\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITYTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITYID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SUMMARY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CALLCHECK_PRIORITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_REQUIRED\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CALLCHECK_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ASSIGNEDTO\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_PLANNED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PERCENTAGECOMPLETE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COMPLETE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_COMPLETE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"STATUSDETAILTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STATUSDETAIL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Latitude\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"Longitude\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"DeviceTagId\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Humidity\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Light\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"LocationMethod\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IsMotionDetected\",\"nullable\":true,\"type\":\"boolean\"},{\"metadata\":{},\"name\":\"Pressure\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"ADDRESSTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSISRESIDENTIAL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSISPRIMARY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSLOCATIONCODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSNAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSLINE1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDRESSLINE2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STATEPROVINCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POSTALCODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COUNTRYCODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLATDEGREES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLATDIRECTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLONGDEGREES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"GEOLONGDIRECTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CONTACTNAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureC\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"TemperatureF\",\"nullable\":true,\"type\":\"decimal(18,2)\"},{\"metadata\":{},\"name\":\"IsButtonPushed\",\"nullable\":true,\"type\":\"boolean\"},{\"metadata\":{},\"name\":\"IsShockExceeded\",\"nullable\":true,\"type\":\"boolean\"},{\"metadata\":{},\"name\":\"CALLCHECK_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_LOS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DESTINATION_LOCATION_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"IS_TEMPERATURE\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_transportation_callcheck"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_transportation_callcheck",
				"depends_on": [
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_dim_customer"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_rates_charges",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_rates_charges/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"CHARGE_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_rates_charges",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEQUENCE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RATE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RATE_QUALIFER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_LEVEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EDI_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FREIGHT_CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FAK_FREIGHT_CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHARGE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"CONTRACT_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CURRENCY_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INVOICE_NUMBER\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_transportation_rates_charges"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_transportation_rates_charges",
				"depends_on": [
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_dim_carrier_los"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "SOURCE_SYSTEM_KEY",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_milestone_activity",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_milestone_activity/",
						"hash_exclude_columns": "[]",
						"primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"ActivityCode\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/map_milestone_activity",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"MilestoneId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Milestone_Completion_Flag\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SourceActivityName\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "map_milestone_activity"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_map_milestone_activity"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "Account_ID",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/account_type_digital",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/account_type_digital/",
						"hash_exclude_columns": "[]",
						"primary_keys": "[\"Account_ID\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/account_type_digital",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"Account_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Account_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Account_Name\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "account_type_digital"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_account_type_digital"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ID",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/Local_Courier_Service",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/local_courier_service",
						"hash_exclude_columns": "[]",
						"primary_keys": "[\"ID\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/local_courier_service",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SERVICE_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIERNAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SERVICELEVELNAME\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "local_courier_service"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_local_courier_service"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "SOURCE_SYSTEM_KEY",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_ordersearchstatus",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_ordersearchstatus/",
						"hash_exclude_columns": "[]",
						"primary_keys": "[\"OrderStatusCode\",\"SOURCE_SYSTEM_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/map_ordersearchstatus",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SourceSystemName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"OrderStatusName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"OrderStatusCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
						"tgt_table_name": "map_orderSearchStatus"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_map_ordersearchstatus"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "TransactionTypeId",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_transactiontype_milestone",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_transactiontype_milestone",
						"hash_exclude_columns": "[]",
						"primary_keys": "[ \"TransactionTypeId\",\"MilestoneOrder\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/map_transactiontype_milestone",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"TransactionTypeId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"TransactionTypeName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneId\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneOrder\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Is_Managed\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Is_Inbound\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"Is_International\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_FTZ\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
						"tgt_table_name": "map_transactiontype_milestone"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_map_transactiontype_milestone",
				"depends_on": [
					{
						"task_key": "silver_dim_warehouse"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transport_details",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transport_details/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"SHIPMENT_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transport_details",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_ASN\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEQUENCE\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"CONTAINED_IN\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLASS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IS_HAZMAT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDERED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ORDERED_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"PLANNED_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTUAL_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"ACTUAL_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_WGT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTUAL_WGT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_DIMENSION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"COMMODITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DELIVERY_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"TemperatureRange_Min\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Max\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Code\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Planned_Weight_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Actual_Weight_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Dimension_UOM\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_transport_details"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_transport_details",
				"depends_on": [
					{
						"task_key": "silver_dim_customer"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_milestone_activity",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_milestone_activity/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"LOAD_TRACK_SDUK\"]",
						"partition_keys": "[\"ACTIVITY_MONTH_PART_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_milestone_activity",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRACKING_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_ACTIVITY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACTIVITY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTIVITY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTIVITY_COMPLETION_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PLANNED_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_PLANNED_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PLANNED_MILESTONE_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"PLANNED_MILESTONE_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_MILESTONE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"MILESTONE_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MILESTONE_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MILESTONE_COMPLETION_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_TRACK_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_WMS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_ASN\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEGMENT_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACTIVITY_NOTES\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FTZ_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TIME_ZONE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVITY_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOGI_NEXT_FLAG\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_WMS_SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_DATE_TIME\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LATITUDE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LONGITUDE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_OF_DELIVERY_LOCATION\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"additional_custom_column": "[{\"name\":\"ACTIVITY_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(ACTIVITY_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
						"tgt_table_name": "fact_milestone_activity"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_milestone_activity"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_shipment",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_shipment/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"SHIPMENT_SDUK\"]",
						"partition_keys": "[\"UTC_SHIPMENT_CREATION_MONTH_PART_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_shipment",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHIPMENT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_SEQUENCE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRACKING_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LEVEL_OF_SERVICE_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_SHIPMENT_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_SHIPMENT_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"SHIPMENT_CREATION_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHIPMENT_CREATION_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHIPMENT_LENGTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_WIDTH\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_HEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_WEIGHT\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_QUANTITY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"SHIPMENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CARRIER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CUBAGE\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"TemperatureRange_Min\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Max\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Code\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Actual_Weight_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"Dimension_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPMENT_DESCRIPTION\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LOAD_AREA\",\"nullable\":true,\"type\":\"decimal(38,6)\"},{\"metadata\":{},\"name\":\"UOM\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"additional_custom_column": "[{\"name\":\"UTC_SHIPMENT_CREATION_MONTH_PART_KEY\",\"value\":\"cast(date_format(nvl(UTC_SHIPMENT_CREATION_DATE,'1900-01-01'),'yyyyMM') as bigint)\"}]",
						"tgt_table_name": "fact_shipment"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_shipment",
				"depends_on": [
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_dim_carrier_los"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_order_line_details",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_order_line_details/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"ORDER_LINE_DETAILS_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order_line_details",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_LINE_DETAIL_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_SERIAL_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VENDOR_LOT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LPN_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DISPOSITION_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_LINE_DETAILS_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_LINE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IS_INBOUND\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SHELF_LIFE\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PRODUCT_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"STORAGE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UTC_EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_EXPIRATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"HOLD_CODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RECEIPT_NUMBER\",\"nullable\":true,\"type\":\"string\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_order_line_details"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_order_line_details"
			},
			{
				"existing_cluster_id": "0301-051816-jv2btm8l",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_fact_order_dim",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_fact_order_dim_inc",
				"depends_on": [
					{
						"task_key": "silver_account_type_digital"
					},
					{
						"task_key": "silver_map_ordersearchstatus"
					},
					{
						"task_key": "silver_dim_geo_location"
					},
					{
						"task_key": "silver_local_courier_service"
					},
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_fact_order"
					},
					{
						"task_key": "silver_dim_carrier_los"
					},
					{
						"task_key": "silver_dim_service"
					},
					{
						"task_key": "silver_fact_order_deletes"
					},
					{
						"task_key": "silver_dim_source_system"
					},
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_map_milestone_activity"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051816-jv2btm8l",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_milestone_activity",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_milestone_activity",
				"depends_on": [
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "silver_fact_transport_details"
					},
					{
						"task_key": "silver_fact_milestone_activity"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_transportation_callcheck",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_transportation_callcheck",
				"depends_on": [
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "silver_fact_transportation_callcheck"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051816-jv2btm8l",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_orders",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_orders",
				"depends_on": [
					{
						"task_key": "silver_fact_order_line"
					},
					{
						"task_key": "silver_fact_transportation_exception"
					},
					{
						"task_key": "gold_digital_summary_milestone_activity"
					},
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_dim_carrier_los"
					},
					{
						"task_key": "silver_map_temperature_range_details"
					},
					{
						"task_key": "silver_fact_order_reference"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051816-jv2btm8l",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_orders_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_orders",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_transportation_references"
					},
					{
						"task_key": "gold_digital_summary_exceptions"
					},
					{
						"task_key": "gold_digital_summary_order_tracking"
					},
					{
						"task_key": "gold_digital_summary_transportation_callcheck"
					},
					{
						"task_key": "gold_digital_summary_orders"
					},
					{
						"task_key": "gold_digital_summary_transportation_rates_charges"
					},
					{
						"task_key": "gold_digital_summary_order_lines"
					},
					{
						"task_key": "gold_digital_summary_order_lines_details"
					},
					{
						"task_key": "gold_digital_summary_transportation"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_exceptions",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_exceptions",
				"depends_on": [
					{
						"task_key": "silver_fact_transportation_exception"
					},
					{
						"task_key": "silver_map_milestone_activity"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_inbound_line"
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_inbound_line",
				"depends_on": [
					{
						"task_key": "silver_fact_inbound_line"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_fact_transport_details"
					},
					{
						"task_key": "silver_dim_item"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "Y",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_inbound_line",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_inbound_line/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"INBOUND_LINE_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_inbound_line",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"WAREHOUSE_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"ITEM_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ASN_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ASN_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PO_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PO_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RCPT_HEADER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"RCPT_LINE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_HEADER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_HEADER_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INBND_CARRIER_NAME\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INBND_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_INBND_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_INBND_HDR_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INBND_LINE_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_INBND_LINE_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_INBND_LINE_CREATION_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INBND_HDR_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_INBND_HDR_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_INBND_HDR_SHIPPED_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"IL_FIRST_RCVD_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_IL_FIRST_RCVD_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_IL_FIRST_RCVD_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"IL_LAST_PUTAWAY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"UTC_IL_LAST_PUTAWAY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LOFST_IL_LAST_PUTAWAY_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INBND_LINE_SHIPPED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"INBND_LINE_RECEIVED_QTY\",\"nullable\":true,\"type\":\"decimal(22,4)\"},{\"metadata\":{},\"name\":\"INBOUND_LINE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WAREHOUSE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ITEM_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"INBND_HDR_CREATION_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_HDR_CREATION_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_LINE_CREATION_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_LINE_CREATION_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_HDR_SHIPPED_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"INBND_HDR_SHIPPED_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_FIRST_RCVD_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_FIRST_RCVD_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_LAST_PUTAWAY_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"IL_LAST_PUTAWAY_TIME_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_PO_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_PO_SUB_STATUS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INBND_LINE_RECEIVED_CASES\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"DML_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DML_DATE_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_2\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_10\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_11\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_1\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_3\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_4\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_INBOUND_LINE_REFERENCE_5\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CASES\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_inbound_line"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_inbound_line",
				"depends_on": [
					{
						"task_key": "silver_dim_geo_location"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_milestone",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_milestone",
				"depends_on": [
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "silver_map_transactiontype_milestone"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_order_lines",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_order_lines",
				"depends_on": [
					{
						"task_key": "silver_fact_order_line"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_dim_item"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_order_lines_details",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_order_lines_details",
				"depends_on": [
					{
						"task_key": "silver_fact_order_line_details"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_dim_item"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_order_tracking",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_order_tracking",
				"depends_on": [
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "silver_fact_shipment"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_transportation",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_transportation",
				"depends_on": [
					{
						"task_key": "gold_fact_order_dim_inc"
					},
					{
						"task_key": "silver_fact_transportation"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_transportation_details",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_transportation_details",
				"depends_on": [
					{
						"task_key": "silver_fact_transport_details"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_transportation_rates_charges",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_transportation_rates_charges",
				"depends_on": [
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "silver_fact_transportation_rates_charges"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/gold/pr_load_summary_transportation_references",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "gold_digital_summary_transportation_references",
				"depends_on": [
					{
						"task_key": "silver_fact_order_reference"
					},
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "gold_fact_order_dim_inc"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_order_lines_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_order_lines",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_orders"
					},
					{
						"task_key": "gold_digital_summary_inbound_line"
					},
					{
						"task_key": "gold_digital_summary_order_lines"
					},
					{
						"task_key": "gold_digital_summary_order_lines_details"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_milestone_activity_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_orders_milestone_activity",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_orders"
					},
					{
						"task_key": "gold_digital_summary_milestone_activity"
					},
					{
						"task_key": "silver_map_transactiontype_milestone"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_transportation_callcheck_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_transportation_callcheck",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_orders"
					},
					{
						"task_key": "gold_digital_summary_transportation_callcheck"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051624-cl37tr9d",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_transport_details_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_transport_details",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_transportation_details"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_transportation_rates_charges_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_transportation_rates_charges",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_orders"
					},
					{
						"task_key": "gold_digital_summary_transportation_rates_charges"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ActivityCode",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/wh_wip_mapping_activity",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/wh_wip_mapping_activity/",
						"hash_exclude_columns": "[]",
						"primary_keys": "[\"ActivityCode\",\"SOURCE_SYSTEM_KEY\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/wh_wip_mapping_activity",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"Type\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"MilestoneName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ActivityCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"WIP_ActivityName\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"WIPActivityOrderId\",\"nullable\":true,\"type\":\"integer\"}],\"type\":\"struct\"}",
						"tgt_table_name": "wh_wip_mapping_activity"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_wh_wip_mapping_activity",
				"depends_on": [
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_dim_source_system"
					},
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_dim_carrier_los"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051816-jv2btm8l",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_deletes_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "DELETETIMESTAMP",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/splus_src_deletes",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/splus_src_deletes",
						"hash_exclude_columns": "",
						"primary_keys": "[\"SOURCE_SYSTEM_KEY\",\"ORDER_SDUK\"]",
						"partition_keys": "",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_order",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"ORDER_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"ORIGIN_CONTACT_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"ACCOUNT_USER_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"DEST_CONTACT_ID\",\"nullable\":true,\"type\":\"long\"},{\"metadata\":{},\"name\":\"ORDER_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PKG_AVAILABLE_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"USER_REFERENCE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"QUOTED_PRICE\",\"nullable\":true,\"type\":\"double\"},{\"metadata\":{},\"name\":\"QUOTED_DELIV_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PROOF_DELIVERY_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SIGNATURE_REQUIRED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CANCELLED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"DOCUMENT_AUTHENTICATION_NO\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ASSIGNED_TO\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_TIME_ZONE_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DEST_TIME_ZONE_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CREDIT_CARD_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"AUTO_DISPATCH_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CARGO_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"ORDER_COMPLETION_TIME\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ALT_ORDER_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SEC_ORDER_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORIGIN_DELIVERY_INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DEST_DELIVERY_INSTRUCTIONS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_STATE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CURRENT_SEGMENT\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"SERVICE_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ACCOUNT_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CONSIGNEE_ONLY_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CURRENT_LOCATION_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"MANAGING_BRANCH_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"ORDER_SOURCE_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"PROOF_DELIVERY_DEPT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTUAL_PACKAGES_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"REQUESTED_DELIVERY_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"EXPORTED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ORDER_FLFILMNT_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BACK_ORDER_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"EXPORTED_BATCH_NM\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLOSEST_WHSE_ENABLED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"TAKEN_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DELIVER_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ACTIVE_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"DISPATCHED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"DISPATCHED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLOSED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"CLOSED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"VERSION\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CREATED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CREATED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"LAST_UPDATED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LAST_UPDATED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"FINALIZED_BY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FINALIZED_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"WEIGHT_UOM_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"DIMENSION_UOM_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"FA_EXTRACT_BATCH_NM\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"FA_EXTRACT_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"CREATION_START_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"WAREHOUSE_PICKUP_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"POD_DETAILS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_SUBTYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INTEGRATION_SERVICE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CANCELLED_AT_OC_STATE_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"BILLING_WEIGHT\",\"nullable\":true,\"type\":\"decimal(11,2)\"},{\"metadata\":{},\"name\":\"BILLING_PICKUP_MILEAGE\",\"nullable\":true,\"type\":\"decimal(11,2)\"},{\"metadata\":{},\"name\":\"BILLING_DROPOFF_MILEAGE\",\"nullable\":true,\"type\":\"decimal(11,2)\"},{\"metadata\":{},\"name\":\"KSMS_STATUS_TYPE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPPER_ACCOUNT_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INVENTORY_ACCOUNT_ID\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"FUTURE_PLACEMENT_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"BACK_ORDER_PRIORITY_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"REQ_FUTURE_PLACEMENT_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ACCESS_POINT_PKG_RELEASE_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"OMS_BATCH_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ROUTING_BRD_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_NM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_DEPT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_DETAILS\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SAME_DAY_ACP_POD_DTM\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"PRIORITY_CD\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORDER_ALTERED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"INVENTORY_ORDER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_PO_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ADDITIONAL_ORDER_IDENTIFIER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPPING_PRIORITY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"INTERNATIONAL_ORDER_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"INVOICE_REQUIRED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"COUNTRY_OF_CONSIGNMENT\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BILL_OF_LADING\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BATCH_PICK_ALLOWED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"ORDER_HANDLING_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CONSOLIDATION_ALLOWED_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"CONTAINER_QTY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CONTAINER_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CHEPPALLET_INDICATOR\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"HAZMAT_ORDER_IND\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"PROGRESSIVE_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"BILLED_CONTAINER_QTY\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TRANSPORTATION_MODE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CUSTOMER_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ORGANIZATION_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"IOR_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"POD_ON_HOLD\",\"nullable\":true,\"type\":\"decimal(1,0)\"},{\"metadata\":{},\"name\":\"DELETETIMESTAMP\",\"nullable\":true,\"type\":\"timestamp\"}],\"type\":\"struct\"}",
						"additional_custom_column": "[{\"name\":\"SOURCE_SYSTEM_KEY\",\"value\":\"cast('1002' as bigint)\"},{\"name\":\"ORDER_SDUK\",\"value\":\"cast(ORDER_ID as string)\"}]",
						"tgt_table_name": "splus_src_deletes"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_order_deletes",
				"depends_on": [
					{
						"task_key": "silver_fact_order"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "ETL_UPDATE_DATE",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/fact_transportation_references",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/fact_transportation_references/",
						"hash_exclude_columns": "[\"ETL_INSERT_DATE\",\"ETL_UPDATE_DATE\",\"ETL_BATCH_NUMBER\"]",
						"primary_keys": "[ \"SOURCE_SYSTEM_KEY\",\"REFERENCE_SDUK\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/fact_transportation_references",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"SOURCE_SYSTEM_KEY\",\"nullable\":true,\"type\":\"integer\"},{\"metadata\":{},\"name\":\"CLIENT_KEY\",\"nullable\":true,\"type\":\"decimal(18,0)\"},{\"metadata\":{},\"name\":\"LOAD_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"UPS_ORDER_NUMBER\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"CLIENT_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"SHIPUNIT_ID\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_TYPE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFRENCE_VALUE\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_LEVEL\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"REFERENCE_SDUK\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_BATCH_NUMBER\",\"nullable\":true,\"type\":\"decimal(18,0)\"}],\"type\":\"struct\"}",
						"tgt_table_name": "fact_transportation_references"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_fact_transportation_references",
				"depends_on": [
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_dim_source_system"
					},
					{
						"task_key": "silver_dim_warehouse"
					},
					{
						"task_key": "silver_dim_carrier_los"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_dim_warehouse_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_dim_warehouse",
				"depends_on": [
					{
						"task_key": "silver_fact_transportation"
					},
					{
						"task_key": "silver_dim_customer"
					},
					{
						"task_key": "silver_dim_carrier_los"
					},
					{
						"task_key": "silver_dim_source_system"
					},
					{
						"task_key": "silver_dim_warehouse"
					}
				]
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/silver/autoloader_transform_bronze_to_silver",
					"base_parameters": {
						"log_debug_mode": "N",
						"sort_values": "CarrierCode",
						"checkpoint_location": "/mnt/sail/bronze/gld360/inbound/checkpoint/map_temperature_range_details",
						"src_folder_path": "/mnt/sail/bronze/gld360/inbound/landing/map_temperature_range_details/",
						"hash_exclude_columns": "[]",
						"primary_keys": "[\"CarrierCode\",\"LevelOfService\"]",
						"target_folder_path": "/mnt/sail/silver/gld360/inbound/map_temperature_range_details/",
						"src_schema": "{\"fields\":[{\"metadata\":{},\"name\":\"CarrierCode\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"LevelOfService\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureThreshold\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Min\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_Max\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"TemperatureRange_UOM\",\"nullable\":true,\"type\":\"string\"},{\"metadata\":{},\"name\":\"ETL_INSERT_DATE\",\"nullable\":true,\"type\":\"timestamp\"},{\"metadata\":{},\"name\":\"ETL_UPDATE_DATE\",\"nullable\":true,\"type\":\"timestamp\"}],\"type\":\"struct\"}",
						"tgt_table_name": "map_temperature_range_details"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "silver_map_temperature_range_details"
			},
			{
				"existing_cluster_id": "0301-051519-b7nxfnfn",
				"notebook_task": {
					"notebook_path": "/SAIL/cosmos/load_digital_summary_orders_agg_Container",
					"base_parameters": {
						"log_debug_mode": "N"
					}
				},
				"timeout_seconds": 0,
				"email_notifications": {},
				"task_key": "cosmos_digital_summary_orders_agg",
				"depends_on": [
					{
						"task_key": "gold_digital_summary_orders"
					}
				]
			}
		]
	}
}
'''

# COMMAND ----------

requests.post(endpoint, data=data_sail_v2, headers=headers).reason

# COMMAND ----------

requests.post(endpoint, data=data_sail_v2, headers=headers).json()
>>>>>>> 13a8667ae9724d5105090f0851a8408bc1b29ef3
