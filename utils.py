
import cv2
import numpy as np
import os

# solution from
# https://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
def load_images_from_directory(directory_path):
    print(f"loading from {directory_path}...")
    images = []
    for filename in os.listdir(directory_path):
        img = cv2.imread(os.path.join(directory_path,filename))
        if img is not None:
            images.append(img)

    print("images loaded successfully.")
    return images


def save_images_to_directory(image_list,filename,directory_path,no_of_zeros=4):
    print(f"saving to {directory_path}...")

    for i in range(0,len(image_list)):
       
        img = image_list[i]
        full_filename = f'{filename}-{str(i).zfill(no_of_zeros)}.png'
        print(f'saving as {full_filename}...')
        cv2.imwrite(os.path.join(directory_path,full_filename),img)

    print(f'images saved successfully..')




# perform a slide show of the list of images.
def slideshow(image_name,images,waitkey):
    
    for img in images:

        resize_img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2),cv2.INTER_AREA)
        cv2.imshow(image_name,resize_img)
        cv2.waitKey(waitkey)

    cv2.destroyAllWindows()


#translate image based on the offset
def translateImage(image, offset_x, offset_y):
# translate frame
    #Translation Matrix
    matrix = np.float32([
        [1, 0, offset_x],
        [0, 1, offset_y]
    ])

    shifted = cv2.warpAffine(image,matrix,(image.shape[1],image.shape[0]))


    #box the left most area
    if offset_x > 0:
        shifted[:,:offset_x] = [0,255,0]
    #box the rightmost area
    elif offset_x < 0:
        shifted[:,offset_x:] = [0,255,0]

    #box the top
    if offset_y > 0:
        shifted[:offset_y,:] = [0,255,0]
    #box the bottom
    elif offset_y < 0:
        shifted[offset_y:,:] = [0,255,0]


    return shifted



#remove green screen given list of frames, hsv lower green range(array of three), and hsv upper green range (array of three)
def chroma_key_with_bg_image(fg_frames,bg_image,l_green_arr,u_green_arr,offset_x = 0,offset_y = 0):
    print("chroma_keying(bg image)...")

    gsremoved_frames =[]

    for frame in fg_frames:

        #optional: translate the greenscreened image
        if(offset_x != 0 or offset_y != 0):
            frame = translateImage(frame,offset_x,offset_y)

        res_image = cv2.resize(bg_image,(frame.shape[1],frame.shape[0]),cv2.INTER_AREA)

        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        #hsv range
        u_green = np.array(u_green_arr)
        l_green = np.array(l_green_arr)

        #create mask then remove
        mask = cv2.inRange(hsv_frame, l_green, u_green)

        mask_inv = cv2.bitwise_not(mask)    

        gs_bg = cv2.bitwise_and(res_image, res_image, mask = mask)
        object_bg = cv2.bitwise_and(frame,frame,mask = mask_inv)

        
        gsremoved = cv2.add(gs_bg,object_bg)

 
        # cv2.imshow("gs_screen",cv2.resize(gsremoved,(400,225)))
        # cv2.waitKey(5)

        #turn back to bgr then append to list
        gsremoved_frames.append(gsremoved)

    cv2.destroyAllWindows()
    return gsremoved_frames 
    

#remove green screen given list of foreground frames and background frames, hsv lower green range(array of three), and hsv upper green range (array of three)
def chroma_key_with_bg_frames(fg_frames,bg_frames,l_green_arr,u_green_arr,offset_x = 0,offset_y = 0):
    print("chroma_keying(bg frames)...")

    gsremoved_frames =[]

    # Get minimum frames (to avoid out of bounds error)
    frame_no = min(len(fg_frames),len(bg_frames))



    for iter in range(0,frame_no):

        #foreground frame
        fg = fg_frames[iter]

        #background frame
        bg = bg_frames[iter]

        #optional: translate the greenscreened image
        if(offset_x != 0 or offset_y != 0):
            fg = translateImage(fg,offset_x,offset_y)

        res_image = cv2.resize(bg,(fg.shape[1],fg.shape[0]),cv2.INTER_AREA)

        hsv_frame = cv2.cvtColor(fg,cv2.COLOR_BGR2HSV)

        #hsv range
        u_green = np.array(u_green_arr)
        l_green = np.array(l_green_arr)

        #create mask then remove
        mask = cv2.inRange(hsv_frame, l_green, u_green)

        mask_inv = cv2.bitwise_not(mask)    

        gs_bg = cv2.bitwise_and(res_image, res_image, mask = mask)
        object_bg = cv2.bitwise_and(fg,fg,mask = mask_inv)

        
        gsremoved = cv2.add(gs_bg,object_bg)

 
        # cv2.imshow("gs_screen",cv2.resize(gsremoved,(400,225)))
        # cv2.waitKey(5)

        #turn back to bgr then append to list
        gsremoved_frames.append(gsremoved)

    cv2.destroyAllWindows()
    return gsremoved_frames 