import plotly.express as px
import pandas as pd
import requests
import json

def request(endpoint:str):
    try:
        response = requests.get("https://yc-oss.github.io/api/"+endpoint)
        if response.status_code == 200:
            data = response.json()
            return data
    except Exception as e:
        print(f"Endpoint Error: {e}")
        return None
    
def industries():
    data = request("meta.json")
    industries = data["industries"]
    return industries

if __name__ == "__main__":
    industry = []
    counts = []

    data = industries()
    #print(json.dumps(data, indent=4))
    for label in data:
        if label == "b2b" or label == "consumer":
            continue
        industry.append(data[label]["name"])
        counts.append(data[label]["count"])

    df = pd.DataFrame(dict(theta=industry, r=counts))
    fig = px.line_polar(df, r='r', theta='theta', template="plotly_dark", title="Number of Startups by Industry", line_close=True)
    fig.update_traces(fill='toself')
    fig.show()
