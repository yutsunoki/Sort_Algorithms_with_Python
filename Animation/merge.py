from manimlib import *
import numpy as np

class merge(Scene):
        def construct(self):
                T3 = Text('3', color=BLACK, fill_opacity=1)
                T2 = Text('2', color=BLACK, fill_opacity=1)
                T5 = Text('5', color=BLACK, fill_opacity=1)
                T1 = Text('1', color=BLACK, fill_opacity=1)
                T6 = Text('6', color=BLACK, fill_opacity=1)
                T4 = Text('4', color=BLACK, fill_opacity=1)

                Num = VGroup(
                        T3,T2,T5,T1,T6,T4
                )
                Num.scale(3)
                Num.arrange(RIGHT,buff=1.5)

                self.play(
                        *[FadeIn(mob) for mob in Num],
                        Num.animate.to_edge(UP),
                        run_time=2
                )

                self.play(
                        Num[0].animate.shift(DOWN),
                        Num[1].animate.shift(DOWN),
                )
                self.play(
                        CyclicReplace(Num[1],Num[0])
                )
                self.play(
                        Num[2].animate.shift(DOWN),
                        Num[3].animate.shift(DOWN),
                )
                self.play(
                        CyclicReplace(Num[3],Num[2])
                )
                self.play(
                        Num[4].animate.shift(DOWN),
                        Num[5].animate.shift(DOWN),
                )
                self.play(
                        CyclicReplace(Num[5],Num[4])
                )

                self.play(
                        Num[1].animate.shift(DOWN),
                        Num[0].animate.shift(DOWN),
                        Num[3].animate.shift(DOWN),
                )
                self.play(CyclicReplace(Num[3],Num[0]))
                self.play(CyclicReplace(Num[3],Num[1]))
                self.play(
                        Num[2].animate.shift(DOWN),
                        Num[5].animate.shift(DOWN),
                        Num[4].animate.shift(DOWN),
                )
                self.play(CyclicReplace(Num[5],Num[2]))

                self.play(
                        Num.animate.shift(DOWN),
                )

                self.wait()

if __name__ == "__main__":
        from os import system
        system(f"manimgl {__file__} merge -c \"#eeeeee\" --hd -r 350x240 -a -oi")
