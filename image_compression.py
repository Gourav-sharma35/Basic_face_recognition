import tinify
tinify.key="q3hGlkqcvZsC3td5Rllkw0gkkS69V1D9"

source = tinify.from_file("gourav.jpg")
resized = source.resize(
    method="cover",
    width=500,
    height=300
)
resized.to_file("new.jpg")
print("image is successfully resized")
