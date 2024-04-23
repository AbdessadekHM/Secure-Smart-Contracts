import tensorflow as tf
from keras.preprocessing.text import Tokenizer  # type: ignore
from keras.preprocessing.sequence import pad_sequences  # type: ignore
from tokenizer import tokenize


def model(model, source_code, max_sequence_length):
    # model = tf.keras.models.load_model("./models/lstm_model_1.h5")
    # data preprocessing before giving it to prediction
    data = tokenize(source_code, max_sequence_length)
    predictions = model.predict(data)

    vl = [
        "access-control",
        "arithmetic",
        "other",
        "reentrancy",
        "safe",
        "unchecked-calls",
        "locked-ether",
        "bad-randomness",
        "double-spending",
    ]
    threshold = 0.5
    binary_predictions = [1 if pred > threshold else 0 for pred in predictions[0]]
    for i in range(len(binary_predictions)):
        if binary_predictions[i]:
            print(vl[i])
    print("Predictions:", binary_predictions)
    print(predictions[0])
    return binary_predictions
