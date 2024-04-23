import tensorflow as tf


def tokenize(data, max_sequence_length):
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts(data)
    tokenized_data = tokenizer.texts_to_sequences(data)
    padded_data = tf.keras.preprocessing.sequence.pad_sequences(
        tokenized_data, maxlen=max_sequence_length
    )
    return padded_data
