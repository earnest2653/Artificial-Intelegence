import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample data
X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [0, 1, 1, 0]

# Build a simple feedforward neural network
model = Sequential([
    Dense(2, input_shape=(2,), activation='relu'),  # Input layer with 2 neurons and ReLU activation
    Dense(1, activation='sigmoid')  # Output layer with 1 neuron and Sigmoid activation
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=1000, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X_train, y_train)
print(f"Loss: {loss}, Accuracy: {accuracy}")

# Make predictions
predictions = model.predict(X_train)
print("Predictions:")
for i in range(len(X_train)):
    print(f"Input: {X_train[i]}, Predicted Output: {predictions[i][0]}")
