import sys

print('Testing 123.')

class TTRInjector:
    def __init__(self):
        self.ttr = sys.hook(process='ppython', window='Toontown Rewritten [BETA]', lib='python27')
        self.openInjector()

    def openInjector(self):
        window = sys.c_api.register_win('Toontown Rewritten Injector')
        window.set_fields(w=800, h=600, x=0, y=0)

        window.show_instace()
        window.text_box = sys.c_api.register_input_field(window)
        window.text_box.set_fields(w=750, h=500, x=0, y=0)

        window.input_button = sys.c_api.register_input_button(window)
        window.input_button.set_field(w=100, h=100, x=0, y=550, command=self.inject)

    def inject(self, code):
        sys.execute(self.ttr, code)