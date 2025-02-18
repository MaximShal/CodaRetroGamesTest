import os
import pandas as pd
from celery_config import celery_app
from coda import Wrapper, settings
from datetime import datetime


wrapper = Wrapper(settings.CODA_DOC_ID, settings.CODA_TABLE_ID)


def convert_time_to_seconds(time_str):
    if isinstance(time_str, str):
        days = 0
        hr = 0
        minutes = 0
        seconds = 0
        time_parts = time_str.split()
        for i, part in enumerate(time_parts):
            if 'day' in part:
                days = int(time_parts[i - 1]) if i > 0 else 0
            if 'hr' in part:
                hr = int(time_parts[i - 1]) if i > 0 else 0
            if 'min' in part:
                minutes = int(time_parts[i - 1]) if i > 0 else 0
            if 'sec' in part:
                seconds = int(time_parts[i - 1]) if i > 0 else 0
        total_seconds = (days * 24 * 3600) + (hr * 60 * 60) + (minutes * 60) + seconds
        return total_seconds
    return 0


@celery_app.task
def get_coda_data():
    data = wrapper.get_list()
    df = pd.DataFrame([{'createdAt': row.get('createdAt'), **row.get('values')} for row in data])
    df['Actual Time (seconds)'] = df['Actual Time'].apply(convert_time_to_seconds)
    df['Planned Time (seconds)'] = df['Planned Time'].apply(convert_time_to_seconds)
    df['Performance'] = pd.to_numeric(df['Performance'], errors='coerce')

    category_summary = df.groupby('Category').agg(
        total_planned_time_sec=('Planned Time (seconds)', 'sum'),
        total_actual_time_sec=('Actual Time (seconds)', 'sum'),
        average_performance=('Performance', 'mean'),
        total_tasks=('Task Name', 'count'),
        completed_tasks=('Status', lambda x: (x == 'Done').sum()),
        pending_tasks=('Status', lambda x: (x == 'In Progress').sum()),
        created_tasks_today=('createdAt', lambda x: (pd.to_datetime(x).dt.date == pd.to_datetime('today').date()).sum())
    ).reset_index()

    output_folder = 'results'
    os.makedirs(output_folder, exist_ok=True)
    file_name = f'{output_folder}/category_summary_{datetime.now().strftime("%Y-%m-%d")}.xlsx'
    category_summary.to_excel(file_name, index=False, engine='openpyxl')
    print(f'File saved {file_name}')
