import numpy as np
import normalizer
import time
import os
import warnings
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings
warnings.filterwarnings("ignore") #Hide messy Numpy warnings


def build_model(layers):
    model = Sequential()

    model.add(LSTM(
        input_shape=(layers[1], layers[0]),
        output_dim=layers[1],activation='relu',
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],activation='relu',
        return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(
        output_dim=layers[3]))
    model.add(Dense(
        output_dim=layers[4]))
    #model.add(Activation("linear"))

    start = time.time()
    model.compile(loss="mse", optimizer="rmsprop")
    print("> Compilation Time : ", time.time() - start)
    return model

def load_data(imf_index,seq_len,mode):
    std_cpu, std_ram, mean_cpu, mean_ram, ts, cpu_values_normalize, ram_values_normalize \
        = normalizer.normalizer(imf_index,plot=False)




    sequence_length = seq_len + 1
    if mode==1:
        # %%%%%%%%%%%% CPU %%%%%%%%%%%%%%%%%%%%%%%
        result = []
        for index in range(len(cpu_values_normalize) - sequence_length): ## looks like a moving avg !!!
            result.append(cpu_values_normalize[index: index + sequence_length])

        result = np.array(result)
        print('------------')
        print('shape of sequense created is ',result.shape) # (len(total_data)-seq_length)   *   seq_length
        print('length of each sequence is ',len(result[0]))
        print('------------')
        ts=ts[:result.shape[0]-1]

    elif mode==2:
        # %%%%%%%%%%%% RAM %%%%%%%%%%%%%%%%%%%%%%%
        result = []
        for index in range(len(ram_values_normalize) - sequence_length):  ## looks like a moving avg !!!
            result.append(ram_values_normalize[index: index + sequence_length])

        result = np.array(result)
        print('------------')
        print('shape of sequense created is ', result.shape)  # (len(total_data)-seq_length)   *   seq_length
        print('length of each sequence is ', len(result[0]))
        print('------------')
        ts = ts[:result.shape[0] - 1]

    row = round(0.9 * result.shape[0])
    train = result[:int(row), :]

    np.random.shuffle(train)
    x_train = train[:, :-1]
    ts_train = ts[:int(row)]
    y_train = train[:, -1]
    x_test = result[int(row):, :-1]
    y_test = result[int(row):, -1]
    ts_test = ts[int(row)-1:]
    if mode==1:
        y_train_original_part = cpu_values_normalize[:int(row)]
    elif mode==2:
        y_train_original_part = ram_values_normalize[:int(row)]

    l = len(result)
    l_train = x_train.shape
    l_test = x_test.shape
    print('total data length is :',l)
    print('train set length : ',l_train)
    print('test set length :', l_test)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1)) # make 3D
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    return [x_train, y_train,y_train_original_part, x_test, y_test,ts_train,ts_test]



def predict_point_by_point(model, data):
    #Predict each timestep given the last sequence of true data, in effect only predicting 1 step ahead each time
    predicted = model.predict(data)
    predicted = np.reshape(predicted, (predicted.size,))
    return predicted





