---------TF2
# Evaluating a binary classification with ROC and Accuracy

def auroc(y_true, y_pred):
    return tf.py_func(roc_auc_score, (y_true, y_pred), tf.double)

# Build Model...
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy', auroc])

r = model.fit(.....)
print(r.history['accuracy], 'accuracy)
