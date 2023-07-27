from PIL import Image
import os

def remove_metadata(input_image_path, output_image_path):
    try:
        with Image.open(input_image_path) as img:
            new_img = Image.new(img.mode, img.size)
            new_img.putdata(list(img.getdata()))
            new_img.info = {}
            new_img.save(output_image_path)
            print("Metadata deleted successfully.")
    except Exception as e:
        print("error has occurred::", e)

if __name__ == "__main__":
    input_image_path = input("Enter image file path: ")
    output_image_path = os.path.splitext(input_image_path)[0] + "_Metadata deleted" + os.path.splitext(input_image_path)[1]
    remove_metadata(input_image_path, output_image_path)
