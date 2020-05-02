# video2images_images2video
video and images/frames conversion

Explanation for video2images (part 1):
In video2images part, we just have to mention the video name with it’s extension. Here my video name is “video.mp4”. You can set frame rate which is widely known as fps (frames per second). Here I set 0.5 so it will capture a frame at every 0.5 seconds, means 2 frames (images) for each second.
It will save images with name as frame1.jpg, frame2.jpg and so on.

Explanation for images2video (part 2):
In images2video part, We have to add pathIn (path of the folder which contains all the images). I set framerate with 0.5 so it will take 2 images for 1 second.)
It will generate output video in any format. (eg.: .avi, .mp4, etc.)
Note that all images will be automatically ordered like frame1.jpg, frame2.jpg and so on.

After running images2video on a floder of processed images for car recognization. I get a video "nijmegen2_10x.mp4". 

<center>
<video width="400" height="200" src="nijmegen2_10x.mp4" type="video/mp4" controls>
</video>
</center>
