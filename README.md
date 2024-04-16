## How to use this repo

1. Fork this repo and copy the https URL of your forked Walkthrough01 repo

1. Log into the cloud IDE with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open the jupyter_notebooks directory in the explorer sidebar, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

1. Choose the kernel that says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code cell.

Your workspace is now ready to use. When you want to return to this project, you can find it in your Cloud IDE Dashboard</a>. You should only create one workspace per project.

## Dataset Content

The dataset contains 5643 images taken from a blood smear workflow (where a drop of blood is placed on a glass slide). The cells are either malaria-parasitised or uninfected.

## Business Requirements

As a Data Analyst from Code Institute Consulting, you are requested by the Health Care division to provide actionable insights and data-driven recommendations to a Global Hospital Institution. The client is currently facing challenges in disease detection, especially with malaria.

- 1 - The client is interested in having a study that visually differentiates a parasitised from an uninfected cell.
- 2 - The client is interested in telling whether a given cell contains a malaria parasite or not.

## Hypothesis and how to validate?

- We suspect malaria-parasitised cells have clear marks/signs, typically in the middle of the cell, differentiating them from uninfected cells.
  - An average image study can help to investigate it

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Data Visualization

  - We will display the "mean" and "standard deviation" images for parasitised and uninfected cells.
  - We will display the difference between average parasitised and uninfected cells.
  - We will display an image montage for either parasitised or uninfected cells.

- **Business Requirement 2**: Classification
  - We want to predict if a given cell is infected or not with malaria.
  - We want to build a binary classifier and generate reports.

## ML Business Case

### MalariaClf

- We want an ML model to predict if a cell is infected with malaria or not based on historical image data. It is a supervised model, a 2-class, single-label classification model.
- Our ideal outcome is to provide the medical team with a faster and more reliable diagnostic for malaria detection.
- The model success metrics are
  - Accuracy of 65% or above on the test set.
- The model output is defined as a flag, indicating if the cell has malaria or not and the associated probability of being infected or not. As usual, the medical staff will do the blood smear workflow and upload the picture to the App. The prediction is made on the fly (not in batches).
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and non-infected cells. A blood smear sample is collected, mixed with a reagent and examined under the microscope. Visual criteria are used to detect malaria parasites. It leaves room to produce inaccurate diagnostics due to human error. On top of that, some specific hospital facilities with malaria centres need more trained staff and expertise and need to be more staffed.
- The training data to fit the model come from the [National Institutes of Health (NIH) Website](https://ceb.nlm.nih.gov/repositories/malaria-datasets/). This dataset contains about 26+ thousand images. We have extracted a subset of 5643 images from this dataset and saved it to [Kaggle dataset directory](https://www.kaggle.com/codeinstitute/malaria-cell-classification/) for quicker model training.
  - Train data - target: infected or not; features: all images

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary

- Quick project summary
  - General Information
    - Malaria is a parasitic infection transmitted by the bite of infected female Anopheles mosquitoes.
    - A blood smear sample is collected, mixed with a reagent and examined in the microscope. Visual criteria are used to detect malaria parasites.
    - According to WHO, in 2019, there were an estimated 229 million cases of malaria worldwide and an estimated 409 thousand deaths due to this disease. Children <5 years are the most vulnerable group, accounting for 67% (274 thousand) of all malaria deaths worldwide in 2019.
  - Project Dataset
    - The available dataset contains 5643 out of +27 thousand images taken from blood smear workflow (when a drop of blood is taken on a glass slide) of cells that are parasitised or uninfected with malaria.
  - Link to additional information
  - Business requirements
    - The client is interested in having a study to differentiate between a parasite-contained and uninfected cell visually.
    - The client is interested in whether a given cell contains a malaria parasite.

### Page 2: Cells Visualizer

- It will answer business requirement 1
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Differences between average parasitised and average uninfected cells
  - Checkbox 3 - Image Montage

### Page 3: Malaria Detector

- Business requirement 2 information - "The client is interested in telling whether a given cell contains a malaria parasite or not."
- Link to download a set of parasite-contained and uninfected cell images for live prediction.
- User Interface with a file uploader widget. The user should upload multiple malaria cell images. It will display the image and a prediction statement, indicating if the cell is infected or not with malaria and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

- Block for each project hypothesis, describe the conclusion and how you validated it.

### Page 5: ML Performance Metrics

- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result
