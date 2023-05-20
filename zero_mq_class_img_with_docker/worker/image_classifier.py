from classifier import Classifier
import tensorflow as tf
import os


class Image_Classifier(Classifier):
    # Load the dataset
    def captar(self):
        (self.train_images, self.train_labels), (
            self.test_images,
            self.test_labels,
        ) = tf.keras.datasets.mnist.load_data()

    # Preprocess the data
    def preprocessar(self):
        self.train_images = self.train_images / 255.0
        self.test_images = self.test_images / 255.0

    # Define the model architecture and Compile the model
    def configurar(
        self,
        *,
        size_of_dense_layer_with_relu_activation_1: int,
        size_of_dense_layer_with_relu_activation_2: int
    ):
        self.size_of_dense_layer_with_relu_activation_1 = (
            size_of_dense_layer_with_relu_activation_1
        )
        self.size_of_dense_layer_with_relu_activation_2 = (
            size_of_dense_layer_with_relu_activation_2
        )

        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Flatten(input_shape=(28, 28)),
                tf.keras.layers.Dense(
                    self.size_of_dense_layer_with_relu_activation_1, activation="relu"
                ),
                tf.keras.layers.Dense(
                    self.size_of_dense_layer_with_relu_activation_2, activation="relu"
                ),
                tf.keras.layers.Dense(10, activation="softmax"),
            ]
        )

        self.model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

    # Train the model
    def treinar(self):
        self.model.fit(self.train_images, self.train_labels, epochs=5)

    # Evaluate the model
    def testar(self):
        self.test_loss, self.test_acc = self.model.evaluate(
            self.test_images, self.test_labels
        )


# if __name__ == "__main__":

#     #-----CPU Device-----
#     os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

#     # ----Configs----
#     classificador = Image_Classifier().instance()
#     classificador.configurar(size_of_dense_layer_with_relu_activation_1 = 64, size_of_dense_layer_with_relu_activation_2 = 64)
#     classificador.executar()
#     print(classificador.test_loss)
#     print(classificador.test_acc)
