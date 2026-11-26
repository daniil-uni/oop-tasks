from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: int) -> str: ...

    @abstractmethod
    def render_square(self, side: int) -> str: ...


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f'<circle r="{radius}"/>'

    def render_square(self, side):
        return f'<rect width="{side}" height="{side}"/>'


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f'({"o" * radius})'

    def render_square(self, side):
        return '\n'.join('#' * side for _ in range(side))



class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def set_renderer(self, renderer: Renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        ...

    @abstractmethod
    def resize(self, factor: float) -> None:
        ...


class Circle(Shape):
    def __init__(self, radius: int, renderer: Renderer):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> str:
        return self.renderer.render_circle(self.radius)

    def resize(self, factor: float) -> None:
        self.radius = round(self.radius * factor)


class Square(Shape):
    def __init__(self, side: int, renderer: Renderer):
        super().__init__(renderer)
        self.side = side

    def draw(self) -> str:
        return self.renderer.render_square(self.side)

    def resize(self, factor: float) -> None:
        self.side = round(self.side * factor)


if __name__ == '__main__':
    vector, raster = VectorRenderer(), RasterRenderer()
    circle = Circle(3, vector)
    square = Square(2, raster)
    print(circle.draw())
    print(square.draw())
    circle.resize(2)
    circle.set_renderer(raster)
    print(circle.draw())