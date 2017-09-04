"""
Constants for easier reference
""" 

TOKENIZER_TEXTBLOB = 'TOKENIZER_TEXTBLOB'
TOKENIZER_NLTK = 'TOKENIZER_NLTK'
TOKENIZER_REGEX = 'TOKENIZER_REGEX'
TOKENIZER_TWITTER = 'TOKENIZER_TWITTER'
TOKENIZER_STANFORD_NLP = 'TOKENIZER_STANFORD_NLP'

TRAIN_INDEX = 0
VAL_INDEX = 1
TEST_INDEX = 2
JOB_ENDPOINT =  'http://ec2-52-33-179-156.us-west-2.compute.amazonaws.com:8000/api/v1'  #'https://104.155.188.251:8080/api/v1'
JOB_ENDPOINT = 'http://104.155.132.60:8080/api/v1'

##
ACCESS_TOKEN = '49553f53ef5178db88e7cf4e192a1db1a77cfdbb'

TRAIN_MODE = 0
TEST_MODE = 1

WORD_LEVEL = 'WORD_LEVEL'
CHAR_LEVEL = 'CHAR_LEVEL'
WORD_CHAR_LEVEL = 'WORD_CHAR_LEVEL' #Word embeddings with char. lvl lstms
WORD_HASHING_LEVEL = 'WORD_HASHING_LEVEL'
WORD_HASHING_CONSTANT = '%'

DATASET_TRAIN = 'DATASET_TRAIN'
DATASET_TEST = 'DATASET_TEST'
DATASET_VALIDATION = 'DATASET_VALIDATION'

GPU_MODE = 'GPU_MODE'
CPU_MODE = 'CPU_MODE'

CLOUD_MODEL_DIR = 'softmax_models'
CLOUD_MODEL_ENDPOINT = 's3.amazonaws.com'

AWS_KEY = 'AKIAJ3OQL4ACVRTLQSJA'
AWS_SECRET = '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'

LOCAL_MODEL_DIR = 'softmax_models'

PREPROCESS_TYPE_INCEPTION = 'PREPROCESS_TYPE_INCEPTION'
PREPROCESS_TYPE_GOOGLENET = 'PREPROCESS_TYPE_GOOGLENET'
PREPROCESS_TYPE_RESNET = 'PREPROCESS_TYPE_RESNET'

PREPROCESS_TYPE_RESNET_50 = 'PREPROCESS_TYPE_RESNET_50'
PREPROCESS_TYPE_RESNET_101 = 'PREPROCESS_TYPE_RESNET_101'
PREPROCESS_TYPE_RESNET_152 = 'PREPROCESS_TYPE_RESNET_152'

NETWORK_TYPE_INCEPTION = 'NETWORK_TYPE_INCEPTION'
NETWORK_TYPE_GOOGLENET = 'NETWORK_TYPE_GOOGLENET'
NETWORK_TYPE_RESNET = 'NETWORK_TYPE_RESNET'

NETWORK_TYPE_RESNET_30 = 'NETWORK_TYPE_RESNET_30'
NETWORK_TYPE_RESNET_50 = 'NETWORK_TYPE_RESNET_50'
NETWORK_TYPE_RESNET_101 = 'NETWORK_TYPE_RESNET_101'
NETWORK_TYPE_RESNET_152 = 'NETWORK_TYPE_RESNET_152'

OPTIMIZER_RMSPROP = 'OPTIMIZER_RMSPROP'
OPTIMIZER_ADAM = 'OPTIMIZER_ADAM'
OPTIMIZER_SGD = 'OPTIMIZER_SGD'

NLTK_DATA_PATH = '../../pretrained_models/nltk'

# Dependency embeddings path
PRETRAINED_EMBEDDINGS_PATH = '../../pretrained_models/word_embeddings/dependency_embeddings/embeddings.npy'
PRETRAINED_VOCAB_PATH = '../../pretrained_models/word_embeddings/dependency_embeddings/vocab.txt'

# Part of speech vocab path
POS_VOCAB_PATH = '../../pretrained_models/word_embeddings/pos_tags/vocab.txt'
STANFORD_CORENLP_PATH = '../../pretrained_models/stanford_corenlp/2015-12-09/*'

MACHINE_READING_MODEL_JOINT_HARD_NEGATIVES_OP = "MACHINE_READING_MODEL_JOINT_HARD_NEGATIVES_OP"
MACHINE_READING_MODEL_JOINT_OP = "MACHINE_READING_MODEL_JOINT_OP"
MACHINE_READING_MODEL_SENTENCE_OP = "MACHINE_READING_MODEL_SENTENCE_OP"
MACHINE_READING_MODEL_ANSWER_OP = "MACHINE_READING_MODEL_ANSWER_OP"

# Initializer for weights (zero, uniform and random)
INITIALIZER_ZERO = 'INITIALIZER_ZERO'
INITIALIZER_UNIFORM_RANDOM = 'INITIALIZER_UNIFORM_RANDOM'

# To load vocab things
PATH_NPY_ARRAY = 'PATH_NPY_ARRAY'
PATH_TEXT_ARRAY = 'PATH_TEXT_ARRAY'