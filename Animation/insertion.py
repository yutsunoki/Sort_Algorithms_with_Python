from manimlib import *

class Insertion(Scene):
        def construct(self):
                Num = VGroup(
                        Text('2',color=BLACK, fill_opacity=1),
                        Text('5',color=BLACK, fill_opacity=1),
                        Text('3',color=BLACK, fill_opacity=1),
                        Text('4',color=BLACK, fill_opacity=1),
                        Text('1',color=BLACK, fill_opacity=1),
                )
                Num.scale(5)
                Num.arrange(RIGHT,buff=2)

                self.play(
                        *[FadeIn(mob) for mob in Num],
                        run_time=2
                )
                self.play(
                        Num[2].animate.move_to(DOWN*2),
                )
                self.play(Succession(
                        Num[1].animate.next_to(Num[3],LEFT,buff=2),
                        Num[2].animate.next_to(Num[0],RIGHT,buff=2),
                ))
                self.play(
                        Num[3].animate.move_to(DOWN*2),
                )
                self.play(Succession(
                        Num[1].animate.next_to(Num[4],LEFT,buff=2),
                        Num[3].animate.move_to(Num[1])
                ))
                self.play(
                        Num[4].animate.move_to(DOWN*2),
                )
                self.play(Succession(
                        Num[1].animate.next_to(Num[1],RIGHT,buff=2),
                        Num[3].animate.move_to(Num[1]),
                        Num[2].animate.move_to(Num[3]),
                        Num[0].animate.move_to(Num[2]),
                        Num[4].animate.move_to(Num[0])
                ))
                self.wait()

if __name__ == "__main__":
        from os import system
        system(f"manimgl {__file__} Insertion -c \"#eeeeee\" --hd -r 350x240 -a -oi")
