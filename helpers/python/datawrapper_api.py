"""Small Datawrapper v3 client for recurring map workflows.

Source: data-toolbox helper `datawrapper-api`.
"""

from __future__ import annotations

import requests


class DatawrapperClient:
    def __init__(self, token, timeout=60):
        if not token:
            raise ValueError("DATAWRAPPER_API_KEY is missing")
        self.base_url = "https://api.datawrapper.de/v3"
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _request(self, method, path, **kwargs):
        response = self.session.request(
            method,
            f"{self.base_url}{path}",
            timeout=self.timeout,
            **kwargs,
        )
        if not response.ok:
            excerpt = response.text[:1000]
            raise RuntimeError(
                f"Datawrapper {method} {path}: HTTP {response.status_code}: {excerpt}"
            )
        return response

    def create_choropleth(
        self,
        title,
        theme="datawrapper",
        language="en-GB",
        folder_id=None,
    ):
        payload = {
            "title": title,
            "type": "d3-maps-choropleth",
            "theme": theme,
            "language": language,
        }
        if folder_id is not None:
            payload["folderId"] = int(folder_id)
        return self._request("POST", "/charts", json=payload).json()

    def upload_data(self, chart_id, csv_bytes):
        self._request(
            "PUT",
            f"/charts/{chart_id}/data",
            data=csv_bytes,
            headers={"Content-Type": "text/csv; charset=utf-8"},
        )

    def upload_topology(self, chart_id, topology_bytes):
        self._request(
            "PUT",
            f"/charts/{chart_id}/assets/{chart_id}.map.json",
            data=topology_bytes,
            headers={"Content-Type": "application/json"},
        )

    def update_chart(self, chart_id, payload):
        return self._request(
            "PATCH",
            f"/charts/{chart_id}",
            json=payload,
            headers={"Content-Type": "application/merge-patch+json"},
        ).json()

    def publish_chart(self, chart_id):
        response = self._request("POST", f"/charts/{chart_id}/publish", json={})
        return response.json() if response.content else {}
