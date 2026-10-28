from PIL import Image, ImageFilter


def convert_grayscale(image):
    return image.convert("L")


def convert_black_white(image):
    gray = image.convert("L")
    return gray.point(lambda pixel: 255 if pixel > 128 else 0)


def apply_blur(image):
    return image.filter(ImageFilter.BLUR)


def main():
    filename = input("Enter image filename: ")

    try:
        image = Image.open(filename)
        print("1. Grayscale")
        print("2. Black and White")
        print("3. Blur")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = convert_grayscale(image)
        elif choice == "2":
            result = convert_black_white(image)
        elif choice == "3":
            result = apply_blur(image)
        else:
            print("Invalid choice.")
            return

        result.show()
        result.save("processed_image.png")
        print("Processed image saved successfully.")

    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
