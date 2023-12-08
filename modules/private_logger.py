import os
import args_manager
import modules.config

from PIL import Image
from modules.util import generate_temp_filename

import requests

# UPLOAD FILE TO THE DIGITALOCEAN SPACE
import boto3
from botocore.client import Config

from settings import *

# #OUR API KEY
# API_KEY = 'lnXUaLVQ5z26JufxNyc3feCXj4bvg2Ddnz9zDf0uf3cJNBPeOFlBq'

# #DIGITAL OCEAN SPACE (S3)
# DO_S3_ACCESS_ID = 'DO00EX6BHL6MGWNQU9K9'
# DO_S3_SECRET_KEY = '+dy4Zqic9RRoU/y5VpOCZZcp6UgKRdl7u7KCl/J8x6U'



log_cache = {}

def getTaskData():
    url = "https://discord-api.sofisun.software/api/getInpaintTask"
    payload = 'key='+str(API_KEY)+'&status=in_progress'
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

    return [cid, task_id, inpaint_input_image_url, inpaint_mask_url, inpaint_additional_prompt]

def updateInpaintDataResultImage(task_id, do_url_image):
    url = "https://discord-api.sofisun.software/api/updateInpaintDataResultImage"
    payload = 'key='+str(API_KEY)+'&task_id='+str(task_id)+'&url_image='+str(do_url_image)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # result = response.json()
    
    return ''

def get_current_html_path():
    date_string, local_temp_filename, only_name = generate_temp_filename(folder=modules.config.path_outputs,
                                                                         extension='png')
    html_name = os.path.join(os.path.dirname(local_temp_filename), 'log.html')
    return html_name


def log(img, dic, single_line_number=3):
    if args_manager.args.disable_image_log:
        return

    date_string, local_temp_filename, only_name = generate_temp_filename(folder=modules.config.path_outputs, extension='png')
    os.makedirs(os.path.dirname(local_temp_filename), exist_ok=True)
    Image.fromarray(img).save(local_temp_filename)
    html_name = os.path.join(os.path.dirname(local_temp_filename), 'log.html')

    existing_log = log_cache.get(html_name, None)

    if existing_log is None:
        if os.path.exists(html_name):
            existing_log = open(html_name, encoding='utf-8').read()
        else:
            existing_log = f'<p>Fooocus Log {date_string} (private)</p>\n<p>All images do not contain any hidden data.</p>'

    div_name = only_name.replace('.', '_')
    item = f'<div id="{div_name}">\n'
    item += f"<p>{only_name}</p>\n"
    for i, (k, v) in enumerate(dic):
        if i < single_line_number:
            item += f"<p>{k}: <b>{v}</b> </p>\n"
        else:
            if (i - single_line_number) % 2 == 0:
                item += f"<p>{k}: <b>{v}</b>, "
            else:
                item += f"{k}: <b>{v}</b></p>\n"
    item += f"<p><img src=\"{only_name}\" width=auto height=100% loading=lazy style=\"height:auto;max-width:512px\" onerror=\"document.getElementById('{div_name}').style.display = 'none';\"></img></p><hr></div>\n"
    existing_log = item + existing_log

    image_full_path_name = os.path.join(os.path.dirname(local_temp_filename), only_name)

    task_data = getTaskData()
    cid = task_data[0]
    task_id = task_data[1]

    # Initiate session DO S3
    session = boto3.Session()
    client = session.client('s3', region_name='nyc3', endpoint_url='https://generatedimages.sfo3.digitaloceanspaces.com', aws_access_key_id=DO_S3_ACCESS_ID, aws_secret_access_key=DO_S3_SECRET_KEY)

    # Upload a file to your Space
    for x in range(6):
        if os.path.exists(image_full_path_name):
            key = client.upload_file(image_full_path_name, 'images_inpaint', str(task_id)+'/'+str(only_name), ExtraArgs={'ACL': 'public-read'})
            break
        else:
            time.sleep(2)
    do_url_image = 'https://generatedimages.sfo3.digitaloceanspaces.com/images_inpaint/' + str(task_id)+'/'+str(only_name)

    updateInpaintDataResultImage(task_id, do_url_image)

    with open(html_name, 'w', encoding='utf-8') as f:
        f.write(existing_log)

    print(f'Image generated with private log at: {html_name}')

    log_cache[html_name] = existing_log

    return
