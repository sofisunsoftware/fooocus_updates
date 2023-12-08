import requests


url = "https://discord-api.sofisun.software/api/updateInpaintDataResultImage"
payload = 'key='+str(API_KEY)+'&task_id='+str(task_id)+'&url_image='+str(do_url_image)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.json())
