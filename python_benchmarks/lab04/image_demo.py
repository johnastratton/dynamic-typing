import image

# -------------------------------
# EXAMPLE PROGRAM #1: RED FILTER
# -------------------------------

#img = image.load_from_file('crayons.png')
img = image.new_image(360,280)
img = image.new_image(360,280)
img = image.new_image(360,280)
img = image.new_image(360,280)
#red_only_img = img
#red_only_img = image.copy_image(img)

#w = img.width()
#h = img.height()

# loop over every (x,y) pair
#for x in range(w):
#    for y in range(h):
        # filter out green and blue
#        test = red_only_img.get_green(x, y)
#        red_only_img.set_green(x, y, 0)
#        red_only_img.set_blue(x, y, 0)

# save the new image to a file
#image.save_to_file(red_only_img, 'red_crayons.png')

# -------------------------------
# EXAMPLE PROGRAM #2: COPY TOP
# -------------------------------

#img = image.load_from_file('crayons.png')
#img_copy = image.copy_image(img)

#w = img.width()
#h = img.height()

# loop over every x value...
#for x in range(w):
#    # ... but only loop over y values in top half
#    for y in range(h/2):
        # get rgb from top half of original image
#        r, g, b = img.get_rgb(x, y)
        
        # copy over rgb from top half to bottom half
#        img_copy.set_rgb(x, y + h/2, r, g, b)


# save the new image to a file
#image.save_to_file(img_copy, 'copy_top.png')

# create window that displays both the original and modified images
#image.display_images(img, red_only_img, img_copy)
