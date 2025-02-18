import requests
import settings


class Wrapper:
    def __init__(self, doc_id: str, table_id: str):
        self.api_key = settings.CODA_API_TOKEN
        self.doc = doc_id
        self.table = table_id
        self.url = f'https://coda.io/apis/v1/docs/{self.doc}/tables/{self.table}'

    def _get_headers(self) -> dict[str:str]:
        return {'Authorization': f'Bearer {self.api_key}'}

    def _get_allowed_table_headers(self) -> dict:
        response = requests.get(self.url+"/columns", headers=self._get_headers())
        if response.status_code == 200:
            cols = response.json()
            return {col['name']: col['id'] for col in cols.get('items')}
        else:
            print(f'Error: {response.status_code} {response.text}')

    def get_list(self, params: dict = {'useColumnNames': True}) -> dict | None:
        response = requests.get(self.url+"/rows", headers=self._get_headers(), params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("items")
        else:
            print(f'Error: {response.status_code} {response.text}')

    def get_row(self, _id: str) -> dict | None:
        response = requests.get(self.url +f'/rows/{_id}', headers=self._get_headers(), params={'useColumnNames': True})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f'Error: {response.status_code} {response.text}')

    def insert_row(self, clean_row_data: list) -> dict | None:
        response = requests.post(
            f'{self.url}/rows', headers=self._get_headers(), json={'rows': [{'cells': clean_row_data}]}
        )
        if response.status_code == 202:
            data = response.json()
            return data
        else:
            print(f'Error: {response.status_code} {response.text}')

    def insert_row_name_to_id(self, row_data: dict[str:str]) -> dict | None:
        columns_ids = self._get_allowed_table_headers()
        return self.insert_row([
            {'column': columns_ids[name], 'value': val} for name, val in row_data.items() if columns_ids[name]
        ])

    def put_row(self, _id: str, clean_row_data: list) -> dict | None:
        response = requests.put(
            f'{self.url}/rows/{_id}', headers=self._get_headers(), json={'row': {'cells': clean_row_data}}
        )
        if response.status_code == 202:
            data = response.json()
            return data
        else:
            print(f'Error: {response.status_code} {response.text}')

    def put_row_name_to_id(self, _id: str, row_data: dict[str:str]) -> dict | None:
        columns_ids = self._get_allowed_table_headers()
        return self.put_row(_id, [
            {'column': columns_ids[name], 'value': val} for name, val in row_data.items() if columns_ids[name]
        ])

    def delete_rows(self, row_ids: list[str]) -> bool:
        response = requests.delete(
            f'{self.url}/rows/', headers=self._get_headers(), json={'rowIds': row_ids}
        )
        if response.status_code == 202:
            return True
        print(f'Error: {response.status_code} {response.text}')
        return False
