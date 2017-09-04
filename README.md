Code for [Two-Stage Synthesis Networks for Transfer Learning in Machine Comprehension](https://arxiv.org/abs/1706.09789).

We provide our components, which include a clean PyTorch implementation of [Latent Predictor Networks](https://arxiv.org/abs/1603.06744), an NER answer chunker, and a procedure to finetune a [BIDAF](https://arxiv.org/abs/1611.01603) model on a combination of synthetic and real question, answer pairs.


We provide the pre-generated synthetic question answer pairs and a pretrained SQuAD BiDAF model that can be trained on NewsQA data.

The question-generation network takes in a passage, extracts answer spans from the passage, and for each answer span, generates a question. In our work, we use the question generator network to finetune a Reading Comprehension Model trained on [SQUAD](https://rajpurkar.github.io/SQuAD-explorer/) to answer questions on [NewsQA](https://datasets.maluuba.com/NewsQA). 

Finally, we also provide several logs from our experiments for single-model, two-model results, and gold answer finetuning under logs/results.

Prerequisites
-------------
- Git LFS

- Python 3.5+
- [Pytorch](https://www.pytorch.org/)
- [Tensorflow](https://tensorflow.org/) version 0.12
- NumPy
- NLTK
- CUDA
- tqdmc

- Python 2.7
- tqdm
- unidecode
- textblob

Quickstart
----------
* To setup the NewsQA dataset, please download and preprocess the NewsQA dataset from [Maluuba's NewsQA][maluuba] repository. Afterwards, please place the train.csv, test.csv and dev.csv files into bidaf/newsqa. 
Then, to setup the NewsQA data, please run these commands:
```
cd bidaf
./download.sh
python3 -m newsqa.prepro
```

To install necessary dependencies, please run 
```
cd ../bidaf
./install.sh
```

To get remaining datasets, please run
```
git lfs pull origin master
```

For a preliminary example of how to extract answers (currently NER), generate questions, and then finetune a BIDAF model on the data, see 
```
./scripts.sh. 
```

** Note: to get the required data to generate questions on NewsQA, you must copy the preprocessed NewsQA dataset by running
```
cd bidaf && python3 -m tests.create_generation_dataset_unsupervised
cd ../
cp datasets/newsqa_unsupervised/train/inputs.txt datasets/newsqa_unsupervised_large/train/inputs.txt
```

To run several of our logs, please execute:
```
cd logs/results
bash script.sh
```

For an end-to-end example of how to train your own question generator network, run
```
$ python3 -m tests.language_model_trainer_test 
```

For an end-to-end example of how to train your own answer chunking model, run
```
$ python3 -m tests.iob_trainer_test
```

A pre-trained BIDAF SQuAD model can be found at bidaf/out/basic/06/save/*
Synthetic question, answer pair datasets can be found at bidaf/newsqa_unsupervised_old (better performance) and bidaf/newsqa_unsupervised_old_verb_filtered (worse performance) 

For all the logs for our reported runs, see https://github.com/davidgolub/ReadingComprehension/

Code Organization
-----
**datasets**
Contains sample datasets used to train the model. C.f. datasets/newsqa_unsupervised. Each dataset needs to have a vocab.txt file, inputs.txt, outputs.txt etc.  

**data_loaders**
Contains code to load a dataset from a directory into memory, and generate batches of examples to train/validate a model.

**models**
Contains core code for the question generator network (language_model.py),  IOB tagging model (iob/iob_model.py), and trainer (language_trainer.py)

**tests**
Contains unit tests for loading, training, predicting the network, and other components of the stack.
newsqa_predictor/* contains tests for predicting on newsqa.
squad_predictor/* contains test for predicting on squad.

**helpers**
Contains various utilities for loading, saving, things that make pytorch easier to work with.

**dnn_units**
Contains the core LSTM units for encoding/decoding.

**trainers**
Contains a trainer for training the answer chunker model.

**bidaf**
Contains a pretrained Reading Comprehension model

[maluuba]: https://github.com/Maluuba/newsqa
[cnn_stories]: http://cs.nyu.edu/~kcho/DMQA/