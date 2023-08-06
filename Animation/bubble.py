from manimlib import *

class bubble(Scene):
        def construct(self):
                Num = VGroup(
                        Text('3',color=BLACK, fill_opacity=1),
                        Text('2',color=BLACK, fill_opacity=1),
                        Text('5',color=BLACK, fill_opacity=1),
                        Text('1',color=BLACK, fill_opacity=1),
                        Text('4',color=BLACK, fill_opacity=1),
                )
                Num.scale(5)
                Num.arrange(RIGHT,buff=2)

                self.play(
                        *[FadeIn(mob) for mob in Num],
                        run_time=2
                )
                self.play(CyclicReplace(Num[0], Num[1]))
                self.play(CyclicReplace(Num[2], Num[3]))
                self.play(CyclicReplace(Num[2], Num[4]))
                self.play(CyclicReplace(Num[3], Num[0]))
                self.play(CyclicReplace(Num[3], Num[1]))
                self.wait()

if __name__ == "__main__":
        from os import system
        system(f"manimgl {__file__} bubble -c \"#eeeeee\" --hd -r 350x240 -a -oi")
