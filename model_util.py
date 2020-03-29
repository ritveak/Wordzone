import pandas as pd
import numpy as np
import keras
import tensorflow as tf
from keras.preprocessing.sequence import TimeseriesGenerator
import pickle

def train(data_path):
  with open(data_path, 'rb') as f:
    data_list = pickle.load(f)

  df = pd.DataFrame(data_list, columns=['frequency'])

  frequency_train = df['Close'].values

  look_back = 15

  train_generator = TimeseriesGenerator(frequency_train, frequency_train, length=look_back, batch_size=20)

  from keras.models import Sequential
  from keras.layers import LSTM, Dense

  model = Sequential()
  model.add(
      LSTM(10,
          activation='relu',
          input_shape=(look_back,1))
  )
  model.add(Dense(1))
  model.compile(optimizer='adam', loss='mse')

  num_epochs = 25
  model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

  with open('./models/model_' + data_path 'wb') as f:
    pickle.dump(model, f)


def train_and_test(data_path):
  with open(data_path, 'rb') as f:
    data_list = pickle.load(f)

  df = pd.DataFrame(data_list, columns=['frequency'])

  frequency = df['Close'].values
  frequency = frequency.reshape((-1,1))

  split_percent = 0.80
  split = int(split_percent*len(frequency))

  frequency_train = frequency[:split]
  frequency_test = frequency[split:]


  look_back = 15

  train_generator = TimeseriesGenerator(frequency_train, frequency_train, length=look_back, batch_size=20)     
  test_generator = TimeseriesGenerator(frequency_test, frequency_test, length=look_back, batch_size=1)

  from keras.models import Sequential
  from keras.layers import LSTM, Dense

  model = Sequential()
  model.add(
      LSTM(10,
          activation='relu',
          input_shape=(look_back,1))
  )
  model.add(Dense(1))
  model.compile(optimizer='adam', loss='mse')

  num_epochs = 25
  model.fit_generator(train_generator, epochs=num_epochs, verbose=1)

  with open('./models/model_' + data_path 'wb') as f:
    pickle.dump(model, f)

  prediction = model.predict_generator(test_generator)

  frequency_train = frequency_train.reshape((-1))
  frequency_test = frequency_test.reshape((-1))
  prediction = prediction.reshape((-1))

  return prediction

  def predict(data_path, model, num_prediction=1):

    with open(data_path, 'rb') as f:
      data_list = pickle.load(f)

    df = pd.DataFrame(data_list, columns=['frequency'])

    frequency = df['Close'].values

    prediction_list = frequency[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
        
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

num_prediction = 30
forecast = predict(num_prediction, model)
forecast_dates = predict_dates(num_prediction)