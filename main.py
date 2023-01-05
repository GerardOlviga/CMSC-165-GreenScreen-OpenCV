import cv2
import utils


#import bg
bg_white = cv2.imread("bg/bg-white.jpg")
bg_newsroom = cv2.imread("bg/bg-newsroom.png")
bg_street1 = cv2.imread("bg/bg-street1.png")
bg_street2 = cv2.imread("bg/bg-street2.jpg")
bg_street3 = cv2.imread("bg/bg-street3.png")
bg_news2 = cv2.imread("bg/bg-news2.jpg")
bg_weather = cv2.imread("bg/bg-weather.png")
bg_bball = cv2.imread("bg/bg-bball.png")

#frames are collected from splitting the frames from virtualdub, please get the frames first from videos and place it in the respective folders
#videos are not saved in this git repository to save space. You can put your own videos in here.


#this is an example of what is going to happen
# BONG REVILLAIN SCENE 1

#'start'
bong1_fin = utils.load_images_from_directory("frames/001-bong")

#'bong revilla po'
bong2 = utils.load_images_from_directory("frames/002-bong")
bong2_fin = utils.chroma_key_with_bg_image(bong2,bg_white,[20,0,70],[60,255,255])

#'no 16 sa balota'
bong3 = utils.load_images_from_directory("frames/003-bong")
bong3_fin = utils.chroma_key_with_bg_image(bong3,bg_white,[20,0,100],[60,255,255])

#'dance' 
bd1 = utils.load_images_from_directory("frames/004-bd1")
bd2 = utils.load_images_from_directory("frames/004-bd2")
bd3 = utils.load_images_from_directory("frames/004-bd3")


gr_bd3 = utils.chroma_key_with_bg_image(bd3,bg_white,[20,0,70],[60,255,255],offset_x= 600,offset_y= 100)
gr_bd2 = utils.chroma_key_with_bg_frames(bd2,gr_bd3,[20,0,70],[60,255,255],offset_x= -600, offset_y= 100)
bong4_fin = utils.chroma_key_with_bg_frames(bd1,gr_bd2,[20,0,70],[60,255,255])


#'end'
bong5_fin =utils.load_images_from_directory("frames/005-bong")


final_frames = [bong1_fin,bong2_fin,bong3_fin,bong4_fin,bong5_fin]


show_frames = final_frames[0]
for i in range(1,len(final_frames)):
    frames = final_frames[i]
    
    show_frames = show_frames + frames 


utils.slideshow("layered1",show_frames,25)

utils.save_images_to_directory(show_frames,'01-bong','final/01-bong')

# # FAJATIN

# faj1 = utils.load_images_from_directory("frames/007-fajatin")
# faj2_fin = utils.load_images_from_directory("frames/008-fajatin")
# faj3 = utils.load_images_from_directory("frames/009-fajatin")

# faj1_fin = utils.chroma_key_with_bg_image(faj1,bg_newsroom,[20,0,70],[60,255,255])
# faj3_fin = utils.chroma_key_with_bg_image(faj3,bg_street1,[20,0,70],[60,255,255])


# final_frames = [faj1_fin,faj2_fin,faj3_fin]


# show_frames = final_frames[0]
# for i in range(1,len(final_frames)):
#     frames = final_frames[i]
    
#     show_frames = show_frames + frames 


# utils.slideshow("layered1",show_frames,25)

# utils.save_images_to_directory(show_frames,'02-fajatin','final/02-fajatin')

# #bulalord
# bul1 = utils.load_images_from_directory("frames/011-bulalord")
# bul2 = utils.load_images_from_directory("frames/012-bulalord")


# bul1_fin = utils.chroma_key_with_bg_image(bul1,bg_street2,[20,0,70],[80,255,255])
# bul2_fin = utils.chroma_key_with_bg_image(bul2,bg_street3,[20,0,70],[60,255,255])

# final_frames = [bul1_fin,bul2_fin]


# show_frames = final_frames[0]
# for i in range(1,len(final_frames)):
#     frames = final_frames[i]
    
#     show_frames = show_frames + frames 


# utils.slideshow("layered1",show_frames,25)

# utils.save_images_to_directory(show_frames,'03-bulalord','final/03-bulalord')

 
# # tani
# tani1 = utils.load_images_from_directory("frames/014-tani")
# tani2 = utils.load_images_from_directory("frames/015-tani")


# tani1_fin = utils.chroma_key_with_bg_image(tani1,bg_news2,[20,0,70],[80,255,255])
# tani2_fin = utils.chroma_key_with_bg_image(tani2,bg_weather,[20,0,80],[80,255,255])

# final_frames = [tani1_fin,tani2_fin]


# show_frames = final_frames[0]
# for i in range(1,len(final_frames)):
#     frames = final_frames[i]
    
#     show_frames = show_frames + frames 


# utils.slideshow("layered1",show_frames,25)
# utils.save_images_to_directory(show_frames,'04-tani','final/04-tani')

# #lebron
# lebron1_fin = utils.load_images_from_directory("frames/017-lebron")
# lebron2 = utils.load_images_from_directory("frames/018-lebron")


# lebron2_fin = utils.chroma_key_with_bg_image(lebron2,bg_bball,[20,0,70],[55,255,255])

# final_frames = [lebron1_fin,lebron2_fin]


# show_frames = final_frames[0]
# for i in range(1,len(final_frames)):
#     frames = final_frames[i]
    
#     show_frames = show_frames + frames 


# utils.slideshow("layered1",show_frames,25)
# utils.save_images_to_directory(show_frames,'05-lebron','final/05-lebron')

# #we then compile all frames into one folder, along with the transition frames created

# bong = utils.load_images_from_directory("final/01-bong")
# fajatin = utils.load_images_from_directory("final/02-fajatin")
# bulalord = utils.load_images_from_directory("final/03-bulalord")
# tani = utils.load_images_from_directory("final/04-tani")
# lebron = utils.load_images_from_directory("final/05-lebron")
# transition = utils.load_images_from_directory("final/06-transition")
# credits = utils.load_images_from_directory("final/07-credits")


# final_frames = [bong,transition,fajatin,transition,bulalord,transition,tani,transition,lebron,transition,credits]


# show_frames = final_frames[0]
# for i in range(1,len(final_frames)):
#     frames = final_frames[i]
    
#     show_frames = show_frames + frames 

# utils.save_images_to_directory(show_frames,'final-frame','final/00-final-frame')

