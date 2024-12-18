from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
import boto3
import requests

def send_email_notification(subject, message):
    ses_client = boto3.client('ses', region_name='us-east-1')
    ses_client.send_email(
        Source='saifshk85@gmail.com',
        Destination={'ToAddresses': ['saifshk85@gmail.com']},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': message}}
        }
    )

def notify_success(context):
    message = f"Glue job {context['task_instance'].task_id} succeeded."
    send_email_notification("Glue Job Success", message)

def notify_failure(context):
    message = f"Glue job {context['task_instance'].task_id} failed."
    send_email_notification("Glue Job Failure", message)

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 13),
    'retries': 2
}

# Define the DAG
dag = DAG(
    'Exec_AWS_Glue_Job',
    default_args=default_args,
    description='Run AWS Glue job with Airflow',
    schedule_interval='@daily',
    catchup=False
)

# Define the AWS Glue Job Operator
run_glue_job = GlueJobOperator(
    task_id='run_glue_job',
    job_name='rs3_ws3_glue_arif',
    iam_role_name='rl_glue_s3_s3',
    region_name='us-east-1',
    dag=dag
)

run_glue_job.on_success_callback = notify_success
run_glue_job.on_failure_callback = notify_failure

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> run_glue_job >> end