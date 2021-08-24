## Dataset Content
The dataset contains +27 thousand images taken from blood smear workflow (when a drop of blood it taken on a glass slide) of cells that are parasitized or uninfected with malaria.


## Business Requirements
As a Data Analyst from Code Institute Consulting, you are requested by HealthCare division to provide actionable insights and data driven recommendations to a Global Hospital Institution. The client is currently facing challenges on disease detection, specially with malaria.
* 1 - The client is interested to have a study to visually differentiate an parasitized and uninfected cell.
* 2 - The client is interested to tell whether or not a given cell is parasitized with malaria or not.


## Hypothesis and how to validate?
* We suspect malaria parasitized cell have clear marks/signs, typically in the middle of the cell, that can differentiate from a un-infected cell
  * A average image study can help to investigate it


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization 
	* We will display a image montage for all classes and/or individual classes
	* We will display the "average" image for each class

* **Business Requirement 2**:  Classification
	* We want to predict if a given cell is infected or not with malaria. 
	* We want to build a binary classifier


## ML Business Case
### MalariaClf
* We want a ML model to predict if a cell is infected with malaria or not, based on historical image data. It is a supervised model, a 2-class, single-label, classification model
* Our ideal outcome is provide to the medical team a faster and reliable diagnostic if a given cell is infected or not with malaria.
* The model success metrics are
	* at least XXXXXXXXXXXXXXXXX% Recall for infected, on train and test set (We don't want to miss a potential infected cell)
	* The ML model is considered a failure if:
		* Recall for not infected cells is lower than XXXXXX0% on train and test set. (We don't want to inform a person has malaria when it doesn't)
* The model output is defined as flag, indicating if the cell has malaria or not, and the associated probability of being infected or not. The medical staff will do the blood smear workflow as usual, and upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and not infected cells. In addition, it is  time consuming and it leaves room to produce inaccurate diagnostics due to human errors. On top of that, there are some specific hospital facilities, with malaria center, that don't have the sufficient right staff and expertise, it is typically understaffed.
* The training data to fit the model come from [National Institutes of Health (NIH) Website](https://ceb.nlm.nih.gov/repositories/malaria-datasets/). This dataset contains about 30 thousand images. We will provide the data already in a GitHub repo.
	* Train data - target: infected or not; features: all images



## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary
* Quick project summary

### Page 2: User Inteface
* User Interface with a file uploader widget. The user should upload a malaria cell image and it will display the image and a prediction statement, indicating if the cell is infected or not with malaria and the probability associated to this statement. 

### Page 3: Image Montage
* It will answer business requirement 1

### Page 4: ML: Malaria Classifier Infection
* Evaluation metrics/performance on MalariaClf
  * For both train and test set: Confusion Matrix and Classification Report
