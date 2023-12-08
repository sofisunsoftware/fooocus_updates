import requests

url = "https://discord-api.sofisun.software/api/getInpaintTask"
payload = 'key=&status=in_progress'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("POST", url, headers=headers, data=payload)
result = response.json()
cid = result['id']
task_id = result['task_id']
inpaint_input_image_url = result['inpaint_input_image_url']
inpaint_mask_url = result['inpaint_mask_url']
inpaint_additional_prompt = result['inpaint_additional_prompt']

print(task_id)