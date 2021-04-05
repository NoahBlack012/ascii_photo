from PIL import Image

class Img:
    def __init__(self, route):
        self.route = route
        self.img = Image.open(route)
        self.width, self.height = self.img.size

    def get_pixel_array(self, resize_factor):
        self.pixels = []
        self.width, self.height = self.img.size
        for x in range(0, self.width, resize_factor):
            row = []
            for y in range(0, self.height, resize_factor):
                pixel_vals = []
                for i in range(0, resize_factor):
                    for j in range(0, resize_factor):
                        try:
                            pixel_vals.append(self.img.getpixel((x + i, y + j)))
                        except IndexError:
                            continue

                avg_r = sum([i[0] for i in pixel_vals]) // len(pixel_vals)
                avg_g = sum([i[1] for i in pixel_vals]) // len(pixel_vals)
                avg_b = sum([i[2] for i in pixel_vals]) // len(pixel_vals)

                average_val = [avg_r, avg_g, avg_b]
                row.append(average_val)



            self.pixels.append(row)


if __name__ == '__main__':
    i = Img("./tree.jpg")
    i.get_pixel_array()
