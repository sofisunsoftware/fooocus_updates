# import matplotlib.pyplot as plt

# rgb_img = plt.imread('test.png')

# print(rgb_img)

# from transformers import CLIPVisionModelWithProjection, CLIPVisionConfig, modeling_utils
# from .utils import load_torch_file, transformers_convert, common_upscale
# import os
# import torch
# import contextlib

# import fcbh.ops
# import fcbh.model_patcher
# import fcbh.model_management
# import fcbh.utils

# def clip_preprocess(image, size=224):
#     mean = torch.tensor([ 0.48145466,0.4578275,0.40821073], device=image.device, dtype=image.dtype)
#     std = torch.tensor([0.26862954,0.26130258,0.27577711], device=image.device, dtype=image.dtype)
#     scale = (size / min(image.shape[1], image.shape[2]))
#     image = torch.nn.functional.interpolate(image.movedim(-1, 1), size=(round(scale * image.shape[1]), round(scale * image.shape[2])), mode="bicubic", antialias=True)
#     h = (image.shape[2] - size)//2
#     w = (image.shape[3] - size)//2
#     image = image[:,:,h:h+size,w:w+size]
#     image = torch.clip((255. * image), 0, 255).round() / 255.0
#     return (image - mean.view([3,1,1])) / std.view([3,1,1])

# result = clip_preprocess(image)

from gradio_client import Client
import base64

with open('test.png', 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    # print(base64_bytes)

client = Client("https://d2d1f3f79098c7eb91.gradio.live/", serialize=True)
# result = client.predict(
# 		'',
# 		'',
# 		["Fooocus V2"],
# 		'Speed',
# 		'1152×896 <span style="color: grey;"> ∣ 9:7</span>',
# 		2,
# 		'1392364049256999292',
# 		2,
# 		4,
# 		'juggernautXL_version6Rundiffusion.safetensors',
# 		'None',
# 		0.5,
# 		'sd_xl_offset_example-lora_1.0.safetensors',
# 		0.1,
# 		'None',
# 		1,
# 		'None',
# 		1,
# 		'None',
# 		1,
# 		'None',
# 		1,
# 		True,
# 		'inpaint',
# 		'Disabled',
# 		None,
# 		[],
# 		'https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png',
# 		'https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png',
# 		'Color is black',
# 		None,
# 		0.5,
# 		0.6,
# 		'ImagePrompt',
# 		None,
# 		0.5,
# 		0.6,
# 		'ImagePrompt',
# 		None,
# 		0.5,
# 		0.6,
# 		'ImagePrompt',
# 		None,
# 		0.5,
# 		0.6,
# 		'ImagePrompt',
# 		# fn_index=6
# 		fn_index=8
# )
# print(result)



# for fn_index in range(40):
# 	print("")
# 	print("fn_index: ", fn_index)
# 	try:
# 		result = client.predict(
# 			"",	# str in 'parameter_10' Textbox component
# 			"",	# str in 'Negative Prompt' Textbox component
# 			["Fooocus V2"],	# List[str] in 'Selected Styles' Checkboxgroup component
# 			"Speed",	# str in 'Performance' Radio component
# 			"704×1408 <span style=\"color: grey;\"> ∣ 1:2</span>",	# str in 'Aspect Ratios' Radio component
# 			1,	# int | float (numeric value between 1 and 32) in 'Image Number' Slider component
# 			0,	# str in 'Seed' Textbox component
# 			0,	# int | float (numeric value between 0.0 and 30.0) in 'Image Sharpness' Slider component
# 			1,	# int | float (numeric value between 1.0 and 30.0) in 'Guidance Scale' Slider component
# 			"null",	# str (Option from: []) in 'Base Model (SDXL only)' Dropdown component
# 			"None",	# str (Option from: ['None']) in 'Refiner (SDXL or SD 1.5)' Dropdown component
# 			0.1,	# int | float (numeric value between 0.1 and 1.0) in 'Refiner Switch At' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 1' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 2' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 3' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 4' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 5' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			True,	# bool in 'Input Image' Checkbox component
# 			"Howdy!",	# str in 'parameter_73' Textbox component
# 			"Disabled",	# str in 'Upscale or Variation:' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Drag above image to here' Image component
# 			["Left"],	# List[str] in 'Outpaint Direction' Checkboxgroup component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Drag above image to here' Image component
# 			"Howdy!",	# str in 'Inpaint Additional Prompt' Textbox component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image)								in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			fn_index=fn_index
# 		)
# 		print(result)
# 	except:
# 		pass







# for fn_index in range(40):
# 	print("")
# 	print("fn_index: ", fn_index)
# 	try:
# 		result = client.predict(
# 			"",	# str in 'parameter_10' Textbox component
# 			"",	# str in 'Negative Prompt' Textbox component
# 			["Fooocus V2"],	# List[str] in 'Selected Styles' Checkboxgroup component
# 			"Speed",	# str in 'Performance' Radio component
# 			"704×1408 <span style=\"color: grey;\"> ∣ 1:2</span>",	# str in 'Aspect Ratios' Radio component
# 			1,	# int | float (numeric value between 1 and 32) in 'Image Number' Slider component
# 			1,	# str in 'Seed' Textbox component
# 			2,	# int | float (numeric value between 0.0 and 30.0) in 'Image Sharpness' Slider component
# 			4,	# int | float (numeric value between 1.0 and 30.0) in 'Guidance Scale' Slider component
# 			"juggernautXL_version6Rundiffusion.safetensors",	# str (Option from: []) in 'Base Model (SDXL only)' Dropdown component
# 			"None",	# str (Option from: ['None']) in 'Refiner (SDXL or SD 1.5)' Dropdown component
# 			0.5,	# int | float (numeric value between 0.1 and 1.0) in 'Refiner Switch At' Slider component
# 			"sd_xl_offset_example-lora_1.0.safetensors",	# str (Option from: ['None']) in 'LoRA 1' Dropdown component
# 			0.1,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 2' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 3' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 4' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			"None",	# str (Option from: ['None']) in 'LoRA 5' Dropdown component
# 			-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
# 			True,	# bool in 'Input Image' Checkbox component
# 			"Howdy!",	# str in 'parameter_73' Textbox component
# 			"Disabled",	# str in 'Upscale or Variation:' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Drag above image to here' Image component
# 			["Left"],	# List[str] in 'Outpaint Direction' Checkboxgroup component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Drag above image to here' Image component
# 			"Howdy!",	# str in 'Inpaint Additional Prompt' Textbox component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image)								in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
# 			0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
# 			0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
# 			"ImagePrompt",	# str in 'Type' Radio component
# 			fn_index=fn_index
# 		)
# 		print(result)
# 	except:
# 		pass






result = client.predict(
	"",	# str in 'parameter_10' Textbox component
	"",	# str in 'Negative Prompt' Textbox component
	["Fooocus V2"],	# List[str] in 'Selected Styles' Checkboxgroup component
	"Speed",	# str in 'Performance' Radio component
	"704×1408 <span style=\"color: grey;\"> ∣ 1:2</span>",	# str in 'Aspect Ratios' Radio component
	1,	# int | float (numeric value between 1 and 32) in 'Image Number' Slider component
	1,	# str in 'Seed' Textbox component
	2,	# int | float (numeric value between 0.0 and 30.0) in 'Image Sharpness' Slider component
	4,	# int | float (numeric value between 1.0 and 30.0) in 'Guidance Scale' Slider component
	"juggernautXL_version6Rundiffusion.safetensors",	# str (Option from: []) in 'Base Model (SDXL only)' Dropdown component
	"None",	# str (Option from: ['None']) in 'Refiner (SDXL or SD 1.5)' Dropdown component
	0.5,	# int | float (numeric value between 0.1 and 1.0) in 'Refiner Switch At' Slider component
	"sd_xl_offset_example-lora_1.0.safetensors",	# str (Option from: ['None']) in 'LoRA 1' Dropdown component
	0.1,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
	"None",	# str (Option from: ['None']) in 'LoRA 2' Dropdown component
	-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
	"None",	# str (Option from: ['None']) in 'LoRA 3' Dropdown component
	-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
	"None",	# str (Option from: ['None']) in 'LoRA 4' Dropdown component
	-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
	"None",	# str (Option from: ['None']) in 'LoRA 5' Dropdown component
	-2,	# int | float (numeric value between -2 and 2) in 'Weight' Slider component
	True,	# bool in 'Input Image' Checkbox component
	"Howdy!",	# str in 'parameter_73' Textbox component
	"Disabled",	# str in 'Upscale or Variation:' Radio component
	"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Drag above image to here' Image component
	[],	# List[str] in 'Outpaint Direction' Checkboxgroup component
	"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Drag above image to here' Image component
	"Howdy!",	# str in 'Inpaint Additional Prompt' Textbox component
	"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
	0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
	0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
	0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
	0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image)								in 'Image' Image component
	0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
	0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	"https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png",	# str (filepath or URL to image) in 'Image' Image component
	0,	# int | float (numeric value between 0.0 and 1.0) in 'Stop At' Slider component
	0,	# int | float (numeric value between 0.0 and 2.0) in 'Weight' Slider component
	"ImagePrompt",	# str in 'Type' Radio component
	fn_index=29
)
print(result)


# result = client.predict(
# 	'',
# 	'',
# 	["Fooocus V2"],
# 	'Speed',
# 	'1152×896 <span style="color: grey;"> ∣ 9:7</span>',
# 	2,
# 	'1392364049256999292',
# 	2,
# 	4,
# 	'juggernautXL_version6Rundiffusion.safetensors',
# 	'None',
# 	0.5,
# 	'sd_xl_offset_example-lora_1.0.safetensors',
# 	0.1,
# 	'None',
# 	1,
# 	'None',
# 	1,
# 	'None',
# 	1,
# 	'None',
# 	1,
# 	True,
# 	'inpaint',
# 	'Disabled',
# 	None,
# 	[],
# 	'https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png',
# 	'https://generatedimages.sfo3.digitaloceanspaces.com/images/11700674134/d18fb8ef-545e-43ad-bf9d-f3ec3640c157.png',
# 	'Color is black',
# 	None,
# 	0.5,
# 	0.6,
# 	'ImagePrompt',
# 	None,
# 	0.5,
# 	0.6,
# 	'ImagePrompt',
# 	None,
# 	0.5,
# 	0.6,
# 	'ImagePrompt',
# 	None,
# 	0.5,
# 	0.6,
# 	'ImagePrompt',
# 	fn_index=29
# )
# print(result)
