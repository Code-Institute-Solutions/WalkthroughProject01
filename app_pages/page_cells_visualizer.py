import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread


def page_cells_visualizer_body():
    st.write("### Cells Visualizer")
    st.info(
        f"* The client is interested to have a study to visually differentiate "
        f"an parasitized and uninfected cell.")

    st.write("* Image Montage")

    my_data_dir = 'inputs/malaria_dataset/cell_images'
    image_montage(dir_path= my_data_dir + '/train', label_to_display='Uninfected',
              nrows=6, ncols=3, figsize=(10,15))


import itertools
import random

# what is the the label you are interested
# dir_path, in this case, train_path
# nrows, ncols, figsize

# logic
# if label exists in the folder
  # check if your montage space is greater tha nsubset size
  # create list of axes indices based on nrows and ncols
  # create a Figure and display images
    # in this loop, load and plot given image


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")

  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:




    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"{label_to_display}: {img_shape[1]}px x {img_shape[0]}px")
    plt.tight_layout()
    st.pyplot(fig=fig)
    # plt.show()


  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")