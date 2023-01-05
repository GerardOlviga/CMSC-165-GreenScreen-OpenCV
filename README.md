# REQUIREMENTS
opencv-python

# EDITING PROCEDURE
1.) Place all frames(you can use virtualdub to get the frames) into one folder in the frames folder
2.) Get all frames into one list by using utils.load_images_from_directory(directory)
3.) Remove greenscreen of frames and put on top of background image/frames using 
    utils.chroma_key_with_bg_image(frames,background,lower_green_hue_range,upper_green_hue_range)
4.) Save frames to a directory using utils.save_images_to_directory(image_list,filename,directory_path):
5.) Once the main.py is saved. run main.py.
6.) Finished frames can be compiled to a video again (using virtualdub)