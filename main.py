from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import random

class YilanOyun(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hucre = 40
        self.yilan = [[400, 800], [360, 800], [320, 800]]
        self.yon = [self.hucre, 0]
        self.elma = [400, 400]
        Clock.schedule_interval(self.guncelle, 0.15)

    def guncelle(self, dt):
        yeni_kafa = [self.yilan[0][0] + self.yon[0], self.yilan[0][1] + self.yon[1]]
        if abs(yeni_kafa[0] - self.elma[0]) < self.hucre and abs(yeni_kafa[1] - self.elma[1]) < self.hucre:
            self.elma = [random.randint(1, 15) * self.hucre, random.randint(5, 20) * self.hucre]
        else:
            self.yilan.pop()
        self.yilan.insert(0, yeni_kafa)
        self.canvas.clear()
        with self.canvas:
            Color(1, 0, 0) # Elma (Kırmızı)
            Rectangle(pos=self.elma, size=(self.hucre-2, self.hucre-2))
            Color(0, 1, 0) # Yılan (Yeşil)
            for p in self.yilan:
                Rectangle(pos=p, size=(self.hucre-2, self.hucre-2))

    def on_touch_down(self, touch):
        if abs(touch.x - self.yilan[0][0]) > abs(touch.y - self.yilan[0][1]):
            self.yon = [self.hucre if touch.x > self.yilan[0][0] else -self.hucre, 0]
        else:
            self.yon = [0, self.hucre if touch.y > self.yilan[0][1] else -self.hucre]

class YilanApp(App):
    def build(self): return YilanOyun()

if __name__ == '__main__':
    YilanApp().run()
