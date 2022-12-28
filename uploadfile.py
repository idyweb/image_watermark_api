import cloudinary
import os 
import cloudinary.uploader
from config2 import cloudinary_cloud_name, cloudinary_api_key, cloudinary_api_secret



cloudinary.config( 
  cloud_name = cloudinary_cloud_name, 
  api_key = cloudinary_api_key, 
  api_secret = cloudinary_api_secret,
  secure = True
)



def upload_image_to_cloudinary(image_path, watermark):
    output_dict = cloudinary.uploader.upload(image_path)
    #cloudinary_url = output_dict['url']
    cloudinary_filename = output_dict["public_id"]
    srcURL = add_watermark(cloudinary_filename, watermark)
    return srcURL
   


def add_watermark(cloudinary_filename, watermark):
   srcURL = cloudinary.CloudinaryImage(cloudinary_filename).image(overlay={'font_family': "montserrat", 'font_size': 55, 'text': watermark})
   return srcURL


