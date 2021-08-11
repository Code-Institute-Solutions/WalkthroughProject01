## Dataset Meaning
The dataset contains images taken from blood smear workflow (when a drop of blood it taken on a glass slide) of cells that are parasitized or uninfected with malaria.


## Business Requirements
As a Data Analyst from Code Institute Consulting, you are requested by HealthCare division to provide actionable insights and data driven recommendations to a Global Hospital Institution. The hospital is currently facing challenges on disease detection, specially with malaria.
* 1 - I am interested to differentiate visually an infected and uninfected cell.
* 2 - I am interested to tell whether or not a given cell is infected with malaria.


## Hypothesis and how to validate?
* We suspect malaria infected cell have clear marks/signs in the middle that can differentiate from a un-infected cell
  * A average image study can help to investigate it


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization 
	* We will display a image montage for all classes or individual classes
	* We will display the "average" image for each class

* **Business Requirement 2**:  Classification
	* We want to predict if a given cell is infected or not with malaria. 
	* We want to build a binary classifier


## ML Business Case
### MalariaClf
* We want a ML model to predict if a cell xxxxxx, based on historical data from customer base, which doesn't include tenure and total charges, since these values are zero for a prospect. It is a supervised model, a 2-class, single-label, classification model: 0 (no churn), 1 (yes churn)
* Our ideal outcome is provide to our sales team a reliable insight on how to onboard customer with a higher sense of loyalty.
* The model success metrics are
	* at least 85% Recall for Churn, on train and test set (We don't want to miss a potential churner)
	* The ML model is considered a failure if:
		* after 3 months of usage, more than 30% of new onboarded custormer churn (it is an indication that the offers are not working or the model is not detecting potential churners)
		* Precision for non churn customer is lower than 80% on train and test set. (We don't want to offer free discount to many non churnable prospects)
* The model output is defined as flag, indicating if a prospect will churn or not, and the associate probability of churning. If the prospect is online, the prospect will have already provided the input data via a form. If the prospect is talking to a sales person, the sales person will conduct a interview to gather the input data and feed into the App. The prediction is made on the fly (not in batches).
* Heuristics: Traditional diagnosis of malaria in laboratory requires an experienced person and careful inspection to discriminate healthy and infected red blood cells. It is also very time-consuming and may produce inaccurate reports due to human errors [link](https://www.hindawi.com/journals/wcmc/2020/8895429/). Thick blood smears assist in detecting the presence of parasites while thin blood smears assist in identifying the species of the parasite causing the infection [link](https://peerj.com/articles/4568/) Alternative techniques such as polymerase chain reaction (PCR) and rapid diagnostic tests (RDT) are used; however, PCR analysis is limited in its performance.  malaria detection can be considered a manual process which may be automated using ML. There might have problems if we do not have the right expertise in specific regions around the world
* The training data to fit the model come from [National Institutes of Health (NIH) Website](https://ceb.nlm.nih.gov/repositories/malaria-datasets/). This dataset contains about 30 thousand images. We will provide the data already in a GitHub repo.
	* Train data - target: infected or not; features: all images



## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary
* Quick project summary

### Page 2: User Inteface
* User Interface with a file uploader widget. The user should upload a malaria cell image and it will display a prediction statement, indicating if the cell is infected or not with malaria and the probability associated to this statement. 

### Page 3: Image Montage
* It will answer business requirement 1

### Page 4: ML: Malaria Classifier Infection
* Evaluation metrics/performance on MalariaClf
  * For both train and test set: Confusion Matrix and Classification Report
