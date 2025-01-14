from manim import *
import pathlib, os

# manim -pql basis_transform.py BasisTransform

SAVE_PATH = pathlib.Path(__file__).parent.absolute() / "media"
print(SAVE_PATH)
if not SAVE_PATH.exists():
    SAVE_PATH.mkdir(parents=True)


class BasisTransform(Scene):
    def construct(self):
        number_plane = NumberPlane()
        dot = Dot(ORIGIN)
        v1 = Arrow(ORIGIN, [2, -1, 0], color=RED)
        v2 = Arrow(ORIGIN, [-1, 2, 0], color=BLUE)
        v1_label = MathTex(r"\vec{v}_1").next_to(v1.get_end(), RIGHT)
        v1_text = Text("(2, -1)").next_to(v1_label, RIGHT)
        v2_label = MathTex(r"\vec{v}_2").next_to(v2.get_end(), UP)
        v2_text = Text("(-1, 2)").next_to(v2_label, UP)
        self.add(number_plane, dot, v1, v2, v1_label, v2_label, v1_text, v2_text)
        self.wait()

        self.play(
            number_plane.animate.apply_matrix([[2, -1], [-1, 2]]),
        )
        self.wait()


# BasisTransform().render(True)
if __name__ == "__main__":
    class_name = "BasisTransform"
    file_name = f"{pathlib.Path(__file__).absolute()}"
    output_file = f"{SAVE_PATH}/{class_name}.mp4"
    os.system(f"manim -pql {file_name} {class_name} -o {output_file}")
