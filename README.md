MoleculeMind
Uncertainty-Aware Molecular Property Prediction Using Graph Neural Networks and Active Learning

Project Type: Scientific Machine Learning / Computational Chemistry / Artificial Intelligence
Level: Intermediate
Duration: 12 Weeks
Primary Languages: Python
Research Focus: Molecular Machine Learning, Graph Neural Networks, Uncertainty Quantification, Active Learning

1. Project Overview

MoleculeMind is a scientific machine learning research project focused on predicting molecular properties using artificial intelligence and computational chemistry techniques.

The project aims to investigate how machine learning models can learn relationships between molecular structures and their physical or chemical properties.

Traditional machine learning approaches often represent molecules using manually engineered molecular descriptors or molecular fingerprints. While these representations can be effective, they may not fully capture the structural relationships between atoms and chemical bonds.

MoleculeMind investigates graph-based molecular representations using Graph Neural Networks (GNNs), allowing models to learn directly from molecular structures.

The project also explores predictive uncertainty and active learning to investigate whether models can recognize unreliable predictions and identify informative molecules for future training.

The initial research task focuses on aqueous solubility prediction using the ESOL molecular dataset.

Rather than simply building a predictive application, MoleculeMind is designed as an experimental research framework that compares different machine learning approaches, investigates generalization, evaluates uncertainty, and studies data-efficient learning.

2. Problem Statement

Predicting molecular properties is an important problem in computational chemistry, pharmaceutical research, and materials science.

Experimental measurement of molecular properties can require substantial laboratory resources and time.

Machine learning offers an opportunity to estimate these properties using existing molecular data.

However, several challenges remain:

Molecular structures are complex and contain relationships between atoms and chemical bonds.
Traditional molecular representations may require extensive feature engineering.
Models may perform well on familiar molecules but struggle with structurally different compounds.
Machine learning predictions can be unreliable, particularly for molecules that differ significantly from the training data.
Training datasets may be limited, making efficient selection of informative samples valuable.

MoleculeMind investigates these challenges through molecular graph learning, uncertainty estimation, and active learning.

3. Research Objectives

The primary objectives are:

Objective 1: Molecular Representation

Develop a preprocessing pipeline that converts molecular SMILES representations into structured molecular representations using RDKit.

Objective 2: Traditional Machine Learning Baselines

Implement and evaluate traditional machine learning models using molecular fingerprints and numerical molecular descriptors.

Objective 3: Graph Neural Networks

Implement a Graph Neural Network capable of learning molecular representations from atoms and chemical bonds.

Objective 4: Generalization Evaluation

Investigate model performance on structurally different molecules using scaffold-based dataset splitting.

Objective 5: Uncertainty Quantification

Implement uncertainty estimation using deep ensembles and investigate whether prediction uncertainty correlates with prediction error.

Objective 6: Active Learning

Develop an active-learning simulation that compares uncertainty-guided sample selection against random sample selection.

Objective 7: Scientific Software Engineering

Build a reproducible and modular machine learning framework with documented experiments, automated tests, and an interactive prediction interface.

4. Research Questions

The project is organized around the following research questions.

RQ1: Molecular Representation

Can graph-based molecular representations capture useful structural information for molecular property prediction compared with traditional molecular fingerprints?

RQ2: Model Generalization

How well do molecular machine learning models generalize to compounds containing molecular scaffolds that were not present during training?

RQ3: Predictive Uncertainty

Can deep ensembles identify molecules for which the model produces less reliable predictions?

RQ4: Active Learning

Can uncertainty-based molecule selection improve learning efficiency compared with random sample selection?

RQ5: Model Performance

How do traditional machine learning models and Graph Neural Networks compare in predictive performance, computational cost, and generalization?

5. Dataset
Primary Dataset: ESOL

The initial dataset will be the ESOL dataset, also known as the Delaney solubility dataset.

It contains molecular structures and measured aqueous solubility values.

Dataset characteristics:

Number of molecules: 1,128.
Number of columns: 10.
Molecular representation: SMILES.
Prediction task: Regression.
Target: Measured log solubility in mol/L.

The target variable is:

measured log solubility in mols per litre

The objective is to predict this continuous numerical value from molecular structure.

Initial Dataset Inspection

The initial data exploration produced the following results:

Metric	Observed Value
Number of molecules	1,128
Number of columns	10
Mean target	-3.0501
Standard deviation	2.0964
Median target	-2.86
Minimum target	-11.60
Maximum target	1.58
Missing values	0
Duplicate SMILES strings	0

These results establish the initial dataset baseline. Additional chemical validation and duplicate analysis using canonical molecular representations will be performed during preprocessing.

Additional Dataset

An optional extension is the Lipophilicity dataset from MoleculeNet.

It will provide an opportunity to investigate whether the developed molecular learning framework can be applied to another molecular property prediction task.

The ESOL dataset remains the primary research benchmark.

6. Technical Methodology

The project will follow a structured machine learning research pipeline.

6.1 Data Acquisition

Download the ESOL dataset and store the original file in:

data/raw/esol.csv

The original dataset will remain unchanged.

6.2 Molecular Preprocessing

Use RDKit to:

Parse SMILES strings.
Validate molecular structures.
Generate canonical SMILES.
Detect invalid molecules.
Calculate molecular descriptors.
Generate molecular fingerprints.
Convert molecules into graph representations.
6.3 Molecular Feature Engineering

Two principal molecular representations will be investigated.

A. Molecular Fingerprints

Morgan fingerprints will be used to represent molecular substructures as numerical bit vectors.

These fingerprints will provide input features for traditional machine learning algorithms.

B. Molecular Graphs

Molecules will be represented as graphs:

G = (V, E)

Where:

V represents atoms.
E represents chemical bonds.

Node features will describe atomic characteristics.

Edge features will describe bond characteristics.

These representations will be used as inputs to the Graph Neural Network.

6.4 Dataset Splitting

The dataset will be divided into:

Training set: 80%.
Validation set: 10%.
Test set: 10%.

The primary evaluation will use scaffold-based splitting.

This approach aims to reduce structural overlap between training and testing molecules.

The test set will remain untouched during model development and hyperparameter selection.

6.5 Baseline Models

Before implementing deep learning models, traditional machine learning baselines will be developed.

Models:

Random Forest.
XGBoost.
Graph Neural Network.

Random Forest and XGBoost will use molecular fingerprints and/or molecular descriptors.

The GNN will use molecular graph representations.

6.6 Graph Neural Network Architecture

The proposed architecture will use a message-passing neural network.

General architecture:

Molecular Graph ↓ Atom and Bond Feature Encoding ↓ Message Passing Layers ↓ Node Embeddings ↓ Graph Pooling ↓ Fully Connected Layers ↓ Solubility Prediction

The model will learn molecular representations through interactions between neighboring atoms.

The final graph representation will be used to predict aqueous solubility.

6.7 Uncertainty Quantification

Deep ensembles will be implemented to estimate predictive uncertainty.

Multiple independently trained models will generate predictions for the same molecule.

The ensemble prediction will be calculated as:

ŷ = (1/M) Σ fᵢ(x)

Where:

M is the number of models.
fᵢ(x) is the prediction of model i.
ŷ is the average prediction.

Prediction variance will be used as an uncertainty indicator.

Experiments will investigate whether higher uncertainty is associated with larger prediction errors.

6.8 Active Learning

An active-learning simulation will investigate whether intelligent sample selection improves learning efficiency.

Two selection strategies will be compared:

Random Sampling

Select new training molecules randomly.

Uncertainty-Based Sampling

Select molecules with the highest predictive uncertainty.

The models will be retrained after each acquisition round.

Performance will be evaluated using learning curves.

This is a simulation using an existing labeled dataset, not a physical laboratory experiment.

7. Model Evaluation

The primary evaluation metrics will be:

Mean Absolute Error

MAE measures the average absolute difference between predicted and actual values.

MAE = (1/n) Σ |yᵢ - ŷᵢ|

Root Mean Squared Error

RMSE penalizes larger prediction errors more strongly.

RMSE = √[(1/n) Σ(yᵢ - ŷᵢ)²]

Coefficient of Determination

R² measures how much of the variation in the target is explained by the model relative to a mean-prediction baseline.

Additional evaluation will include:

Prediction versus actual plots.
Residual analysis.
Uncertainty calibration.
Error analysis across molecular scaffolds.
Training time.
Inference time.
Active-learning learning curves.

No performance improvements will be assumed in advance. Results will be reported based on actual experiments.

8. Software Architecture

MoleculeMind will use a modular Python architecture.

text
moleculemind/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_rdkit_basics.ipynb
│   └── 02_esol_exploration.ipynb
│
├── src/
│   └── moleculemind/
│       │
│       ├── data/
│       │   ├── download_esol.py
│       │   ├── preprocessing.py
│       │   └── splitting.py
│       │
│       ├── features/
│       │   ├── fingerprints.py
│       │   └── molecular_graphs.py
│       │
│       ├── models/
│       │   ├── random_forest.py
│       │   ├── xgboost_model.py
│       │   └── gnn.py
│       │
│       ├── uncertainty/
│       │   └── ensemble.py
│       │
│       ├── active_learning/
│       │   └── acquisition.py
│       │
│       └── evaluation/
│           ├── metrics.py
│           └── analysis.py
│
├── experiments/
│   ├── train_baseline.py
│   ├── train_gnn.py
│   ├── train_ensemble.py
│   └── run_active_learning.py
│
├── tests/
│
├── app/
│   └── dashboard.py
│
├── reports/
│   ├── figures/
│   └── research_report.pdf
│
├── docs/
│   └── PROJECT_OVERVIEW.md
│
├── configs/
│
├── requirements.txt
└── README.md
9. Technology Stack
Technology	Application
Python 3.11	Main programming language
RDKit	Molecular chemistry processing
NumPy	Numerical computation
Pandas	Dataset management
Matplotlib	Scientific visualization
Seaborn	Statistical visualization
Scikit-learn	Traditional ML and evaluation
XGBoost	Gradient boosting
PyTorch	Deep learning
PyTorch Geometric	Graph Neural Networks
JupyterLab	Scientific experimentation
Git	Version control
Streamlit	Interactive dashboard
Pytest	Automated testing
10. Experimental Plan

Four principal experiments will be conducted.

Experiment 1: Traditional ML vs. Graph Neural Networks

Compare Random Forest, XGBoost, and GNN performance.

Research objective: Understand how molecular representation influences predictive performance.

Experiment 2: Molecular Generalization

Evaluate performance using scaffold-based splits.

Research objective: Investigate whether models generalize to structurally different compounds.

Experiment 3: Uncertainty Estimation

Train deep ensembles and investigate the relationship between predictive uncertainty and actual prediction error.

Research objective: Determine whether the model can identify potentially unreliable predictions.

Experiment 4: Active Learning

Compare random and uncertainty-guided molecule selection.

Research objective: Investigate whether uncertainty-based selection improves learning efficiency.

11. Development Timeline

The project will be developed over approximately 12 weeks.

Period	Main Objective	Deliverable
Weeks 1–2	Scientific foundations and data pipeline	Validated molecular dataset
Weeks 3–4	Traditional ML baselines	Baseline comparison
Weeks 5–6	Graph Neural Network	Trained GNN
Weeks 7–8	Uncertainty estimation	Deep ensemble
Weeks 9–10	Active learning	Learning curve experiments
Week 11	Software engineering	Interactive application
Week 12	Research documentation	Final report and presentation
12. Expected Deliverables

The final project will include:

Reproducible molecular preprocessing pipeline.
ESOL dataset exploration and analysis.
Molecular descriptor generation.
Morgan fingerprint generation.
Traditional machine learning implementations.
Custom Graph Neural Network implementation.
Scaffold-based evaluation.
Deep ensemble uncertainty estimation.
Active-learning simulation.
Model performance comparisons.
Scientific visualizations.
Interactive prediction dashboard.
Automated tests.
Technical documentation.
Final research report.
13. Research Contribution

The intended contribution of MoleculeMind is an integrated experimental framework for investigating molecular property prediction under structural distribution shifts.

Its central focus is the relationship between:

Molecular representation.
Predictive performance.
Generalization to unseen molecular scaffolds.
Prediction uncertainty.
Data-efficient learning.

Rather than assuming that graph neural networks or uncertainty-based sampling will outperform simpler methods, the project will investigate these hypotheses through controlled experiments.

The results will be analyzed and documented to identify strengths, weaknesses, and limitations of each approach.

14. Potential Extensions

After completing the main research objectives, possible extensions include:

Applying the framework to additional MoleculeNet datasets.
Exploring molecular explainability.
Investigating alternative message-passing architectures.
Studying computational efficiency.
Adding scientific literature retrieval.
Exploring molecular dynamics and simulation-related machine learning.

These extensions are optional and will not take priority over completing the core experiments.

15. Project Relevance

MoleculeMind combines several areas of computer science and scientific research:

Artificial Intelligence.
Machine Learning.
Graph Neural Networks.
Computational Chemistry.
Scientific Computing.
Statistical Learning.
Uncertainty Quantification.
Active Learning.

The project is designed to demonstrate the ability to develop scientific software, implement machine learning algorithms, design meaningful experiments, analyze results, and communicate technical findings.

These skills are relevant to research environments working at the intersection of machine learning, computational science, and molecular modeling.

16. Project Success Criteria

MoleculeMind will be considered successfully completed when:

The molecular data pipeline is reproducible.
Traditional ML baselines are implemented and evaluated.
A graph-based molecular prediction model is implemented.
Models are evaluated using scaffold-based splitting.
Predictive uncertainty is investigated experimentally.
Active learning is compared against random sampling.
Results are documented with appropriate scientific visualizations.
The software is modular, tested, and documented.
The final research report clearly explains methodology, findings, and limitations.

The project's success will be determined by experimental rigor, reproducibility, and the quality of the technical contribution rather than by achieving an arbitrary accuracy target.

Project Name: MoleculeMind
Research Theme: Uncertainty-Aware Molecular Machine Learning
Primary Research Task: Molecular Aqueous Solubility Prediction
Development Duration: 12 Weeks

This document serves as the central technical and research specification for MoleculeMind. It will be updated as implementation progresses and experimental findings become available.